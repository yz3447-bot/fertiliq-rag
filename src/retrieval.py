"""
FertiliQ Hybrid Retrieval
For each query, searches all three ChromaDB collections in parallel using:
  - Vector search  : top-10 per collection (Gemini embeddings)
  - BM25 search    : top-10 per collection (rank_bm25 on full collection corpus)
  - RRF fusion     : Reciprocal Rank Fusion (k=60) to merge both ranking lists
Returns up to 10 fused candidates per collection (30 total).
"""

from concurrent.futures import ThreadPoolExecutor
from typing import Any

import numpy as np
from rank_bm25 import BM25Okapi

from src.gemini_client import embed_one


# ─── Embedding helper ────────────────────────────────────────────────────────

def embed_query(text: str) -> list[float]:
    """Embed a query string using gemini-embedding-001.

    Args:
        text: The user's query.

    Returns:
        A list of floats representing the embedding vector.
    """
    return embed_one(text)


# ─── Individual search methods ────────────────────────────────────────────────

def vector_search(
    collection: Any,
    query_embedding: list[float],
    top_k: int = 10,
) -> list[dict]:
    """Run ChromaDB vector search and return structured results.

    Args:
        collection: A ChromaDB collection object.
        query_embedding: Pre-computed query embedding vector.
        top_k: Number of nearest neighbours to retrieve.

    Returns:
        List of result dicts with keys: id, content, metadata, distance.
    """
    n = min(top_k, collection.count())
    if n == 0:
        return []

    res = collection.query(
        query_embeddings=[query_embedding],
        n_results=n,
        include=["documents", "metadatas", "distances"],
    )

    results = []
    for i, doc_id in enumerate(res["ids"][0]):
        results.append({
            "id": doc_id,
            "content": res["documents"][0][i],
            "metadata": res["metadatas"][0][i],
            "distance": float(res["distances"][0][i]),
        })
    return results


def bm25_search(
    collection: Any,
    query: str,
    top_k: int = 10,
) -> list[dict]:
    """Run BM25 keyword search over the entire collection corpus.

    Fetches all documents from ChromaDB, builds a BM25Okapi model,
    ranks by query relevance, and returns the top-k results.

    Args:
        collection: A ChromaDB collection object.
        query: The raw query string.
        top_k: Number of top BM25 results to return.

    Returns:
        List of result dicts with keys: id, content, metadata, bm25_score.
    """
    all_data = collection.get(include=["documents", "metadatas"])
    ids = all_data["ids"]
    docs = all_data["documents"]
    metas = all_data["metadatas"]

    if not ids:
        return []

    tokenized_corpus = [d.lower().split() for d in docs]
    bm25 = BM25Okapi(tokenized_corpus)
    tokenized_query = query.lower().split()
    scores = bm25.get_scores(tokenized_query)

    top_k_actual = min(top_k, len(ids))
    top_indices = np.argsort(scores)[::-1][:top_k_actual]

    return [
        {
            "id": ids[i],
            "content": docs[i],
            "metadata": metas[i],
            "bm25_score": float(scores[i]),
        }
        for i in top_indices
    ]


# ─── RRF Fusion ──────────────────────────────────────────────────────────────

def rrf_fusion(
    vector_results: list[dict],
    bm25_results: list[dict],
    k: int = 60,
    top_k: int = 10,
) -> list[dict]:
    """Merge vector and BM25 ranked lists using Reciprocal Rank Fusion.

    Score for each document = sum of 1/(k + rank) across both lists.
    Documents appearing in only one list still receive their single contribution.

    Args:
        vector_results: Ordered list from vector search (rank 0 = best).
        bm25_results: Ordered list from BM25 search (rank 0 = best).
        k: RRF smoothing constant (default 60 per the paper).
        top_k: Number of fused results to return.

    Returns:
        Top-k fused result dicts sorted by descending RRF score, each with
        an added 'rrf_score' field.
    """
    scores: dict[str, dict] = {}

    for rank, result in enumerate(vector_results):
        doc_id = result["id"]
        if doc_id not in scores:
            scores[doc_id] = {"rrf_score": 0.0, "data": result}
        scores[doc_id]["rrf_score"] += 1.0 / (k + rank + 1)

    for rank, result in enumerate(bm25_results):
        doc_id = result["id"]
        if doc_id not in scores:
            scores[doc_id] = {"rrf_score": 0.0, "data": result}
        scores[doc_id]["rrf_score"] += 1.0 / (k + rank + 1)

    sorted_entries = sorted(
        scores.values(), key=lambda x: x["rrf_score"], reverse=True
    )

    fused = []
    for entry in sorted_entries[:top_k]:
        result = {**entry["data"], "rrf_score": entry["rrf_score"]}
        fused.append(result)
    return fused


# ─── Per-collection hybrid search ────────────────────────────────────────────

def search_collection(
    collection: Any,
    query: str,
    query_embedding: list[float],
    top_k: int = 10,
) -> list[dict]:
    """Run hybrid search (vector + BM25 + RRF) on a single collection.

    Args:
        collection: ChromaDB collection.
        query: Raw query string (for BM25).
        query_embedding: Pre-computed query vector (for vector search).
        top_k: Final number of fused results.

    Returns:
        List of up to top_k fused result dicts.
    """
    v_results = vector_search(collection, query_embedding, top_k)
    b_results = bm25_search(collection, query, top_k)
    return rrf_fusion(v_results, b_results, k=60, top_k=top_k)


# ─── Multi-collection parallel search ────────────────────────────────────────

def hybrid_search(
    query: str,
    doc_col: Any,
    forum_col: Any,
    blog_col: Any,
    top_k_per_col: int = 10,
) -> list[dict]:
    """Search all three collections in parallel and return combined candidates.

    Each collection is searched with vector + BM25 + RRF. The three ranked
    lists are concatenated (not re-fused) to give 30 total candidates, each
    tagged with its source collection via metadata.

    Args:
        query: The user's question.
        doc_col: Documentation ChromaDB collection.
        forum_col: Forum ChromaDB collection.
        blog_col: Blog ChromaDB collection.
        top_k_per_col: Candidates to retrieve per collection (default 10).

    Returns:
        Combined list of up to 3 × top_k_per_col candidate dicts.
    """
    query_embedding = embed_query(query)

    with ThreadPoolExecutor(max_workers=3) as pool:
        doc_future = pool.submit(
            search_collection, doc_col, query, query_embedding, top_k_per_col
        )
        forum_future = pool.submit(
            search_collection, forum_col, query, query_embedding, top_k_per_col
        )
        blog_future = pool.submit(
            search_collection, blog_col, query, query_embedding, top_k_per_col
        )

        doc_results = doc_future.result()
        forum_results = forum_future.result()
        blog_results = blog_future.result()

    return doc_results + forum_results + blog_results
