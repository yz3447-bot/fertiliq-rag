"""
FertiliQ Ingest Pipeline
Reads JSON knowledge-base files, applies chunking strategies, embeds content,
and stores chunks in three separate ChromaDB collections.

Chunking strategies:
  - Documentation : header-based parent-child (child enriched with parent content)
  - Forum         : QA-pair chunks (vote + date embedded in text)
  - Blog          : semantic paragraph chunks (title + date prepended)

Run: python src/ingest.py
"""

import json
import sys
from pathlib import Path
from typing import Any

import chromadb
from chromadb import EmbeddingFunction, Documents, Embeddings

from src.gemini_client import embed_texts

# ─── Paths ────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "data"
CHROMA_DIR = ROOT / "chroma_db"

# ─── ChromaDB collection names ────────────────────────────────────────────────
COL_DOCS = "fertiliq_docs"
COL_FORUMS = "fertiliq_forums"
COL_BLOGS = "fertiliq_blogs"


# ─── Gemini Embedding Function ────────────────────────────────────────────────

class GeminiEmbeddingFunction(EmbeddingFunction):
    """ChromaDB-compatible embedding function backed by gemini-embedding-001."""

    def __init__(self):
        pass

    def __call__(self, input: Documents) -> Embeddings:  # noqa: A002
        """Embed a batch of documents using gemini-embedding-001.

        Args:
            input: List of text strings to embed.

        Returns:
            List of embedding vectors (list of floats).
        """
        return embed_texts(list(input))


# ─── ChromaDB helpers ─────────────────────────────────────────────────────────

def get_chroma_client() -> chromadb.PersistentClient:
    """Return a persistent ChromaDB client stored under chroma_db/."""
    CHROMA_DIR.mkdir(exist_ok=True)
    return chromadb.PersistentClient(path=str(CHROMA_DIR))


def get_collections(
    client: chromadb.PersistentClient,
    embedding_fn: GeminiEmbeddingFunction,
) -> tuple:
    """Get or create the three FertiliQ collections.

    Args:
        client: An active ChromaDB persistent client.
        embedding_fn: The GeminiEmbeddingFunction instance.

    Returns:
        Tuple (doc_collection, forum_collection, blog_collection).
    """
    doc_col = client.get_or_create_collection(
        COL_DOCS, embedding_function=embedding_fn,
        metadata={"hnsw:space": "cosine"},
    )
    forum_col = client.get_or_create_collection(
        COL_FORUMS, embedding_function=embedding_fn,
        metadata={"hnsw:space": "cosine"},
    )
    blog_col = client.get_or_create_collection(
        COL_BLOGS, embedding_function=embedding_fn,
        metadata={"hnsw:space": "cosine"},
    )
    return doc_col, forum_col, blog_col


# ─── Documentation ingestion (parent-child chunking) ─────────────────────────

def ingest_documentation(col: Any, raw: list[dict]) -> int:
    """Ingest documentation chunks with parent-child enrichment.

    For each child chunk, the parent section's full content is attached to the
    chunk metadata so retrieval can return the broader context.

    Args:
        col: ChromaDB collection for documentation.
        raw: List of raw doc dicts from documentation.json.

    Returns:
        Number of chunks added to the collection.
    """
    # Build parent_id → parent_content lookup
    parent_map: dict[str, str] = {}
    for entry in raw:
        if entry.get("is_parent"):
            parent_map[entry["id"]] = entry["content"]

    ids, documents, metadatas = [], [], []

    for entry in raw:
        if entry.get("is_parent"):
            continue  # parents are not stored as retrievable chunks

        pid = entry["metadata"].get("parent_id")
        parent_content = parent_map.get(pid, "") if pid else ""

        meta = {**entry["metadata"]}
        meta["parent_content"] = parent_content          # full section context
        meta["chunk_type"] = "child"

        ids.append(entry["id"])
        documents.append(entry["content"])
        metadatas.append(meta)

    if ids:
        col.upsert(ids=ids, documents=documents, metadatas=metadatas)
    return len(ids)


# ─── Forum ingestion (QA-pair chunking) ──────────────────────────────────────

def ingest_forums(col: Any, raw: list[dict]) -> int:
    """Ingest forum QA-pair chunks.

    Vote count and date are already embedded in the content text so the LLM
    can factor them into credibility assessment without extra prompting.

    Args:
        col: ChromaDB collection for forums.
        raw: List of raw forum dicts from forums.json.

    Returns:
        Number of chunks added.
    """
    ids, documents, metadatas = [], [], []

    for entry in raw:
        meta = {**entry["metadata"]}
        meta["votes"] = int(meta.get("votes", 0))
        meta["is_accepted"] = bool(meta.get("is_accepted", False))

        ids.append(entry["id"])
        documents.append(entry["content"])
        metadatas.append(meta)

    if ids:
        col.upsert(ids=ids, documents=documents, metadatas=metadatas)
    return len(ids)


# ─── Blog ingestion (semantic paragraph chunking) ────────────────────────────

def ingest_blogs(col: Any, raw: list[dict]) -> int:
    """Ingest blog semantic-paragraph chunks.

    Each chunk already has the article title and date prepended in its content
    (format: [Article: <title> | Date: <date>]) so the LLM always knows the
    source context.

    Args:
        col: ChromaDB collection for blogs.
        raw: List of raw blog dicts from blogs.json.

    Returns:
        Number of chunks added.
    """
    ids, documents, metadatas = [], [], []

    for entry in raw:
        ids.append(entry["id"])
        documents.append(entry["content"])
        metadatas.append(entry["metadata"])

    if ids:
        col.upsert(ids=ids, documents=documents, metadatas=metadatas)
    return len(ids)


# ─── Entry point ─────────────────────────────────────────────────────────────

def main() -> None:
    """Configure Gemini, load JSON data, and ingest all three collections."""
    embed_fn = GeminiEmbeddingFunction()
    client = get_chroma_client()
    doc_col, forum_col, blog_col = get_collections(client, embed_fn)

    # Load JSON data
    with open(DATA_DIR / "documentation.json", encoding="utf-8") as f:
        doc_data = json.load(f)
    with open(DATA_DIR / "forums.json", encoding="utf-8") as f:
        forum_data = json.load(f)
    with open(DATA_DIR / "blogs.json", encoding="utf-8") as f:
        blog_data = json.load(f)

    print("Ingesting documentation...")
    n_docs = ingest_documentation(doc_col, doc_data)
    print(f"  {n_docs} child chunks added to '{COL_DOCS}'")

    print("Ingesting forums...")
    n_forums = ingest_forums(forum_col, forum_data)
    print(f"  {n_forums} QA-pair chunks added to '{COL_FORUMS}'")

    print("Ingesting blogs...")
    n_blogs = ingest_blogs(blog_col, blog_data)
    print(f"  {n_blogs} paragraph chunks added to '{COL_BLOGS}'")

    print(f"\nIngestion complete. Total: {n_docs + n_forums + n_blogs} chunks.")
    print(f"ChromaDB stored at: {CHROMA_DIR}")


if __name__ == "__main__":
    main()
