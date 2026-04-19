"""
FertiliQ Reranking Pipeline
Three-stage post-retrieval pipeline:

1. Deduplication   — cosine similarity > 0.85 → keep higher-scored chunk
2. Contradiction detection — LLM identifies contradicting pairs; each pair becomes
                             a single ContradictionUnit before reranking
3. LLM Reranking   — selects top 3 slots (units count as one slot each) considering
                     relevance, source credibility, recency, and diversity

Source credibility order: documentation > blog > forum
"""

import json
import re
from dataclasses import dataclass, field
from typing import Optional

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from src.gemini_client import embed_texts, generate

CREDIBILITY_RANK = {"documentation": 3, "blog": 2, "forum": 1}


# ─── Data structures ─────────────────────────────────────────────────────────

@dataclass
class Chunk:
    """A single retrieved knowledge chunk."""
    id: str
    content: str
    metadata: dict
    rrf_score: float = 0.0
    embedding: Optional[list] = None


@dataclass
class ContradictionUnit:
    """A pair of mutually contradicting chunks packaged as a single reranking slot."""
    chunk_a: Chunk
    chunk_b: Chunk
    contradiction_type: str          # "temporal" | "version" | "credibility"
    description: str                 # LLM-generated explanation of the contradiction
    confidence: float = 0.0          # computed after reranking selection


# ─── Deduplication ────────────────────────────────────────────────────────────

def embed_chunks(chunks: list[Chunk]) -> None:
    """Compute and attach Gemini embeddings to each chunk in-place (batch).

    Args:
        chunks: List of Chunk objects; their .embedding field will be populated.
    """
    unembedded = [c for c in chunks if c.embedding is None]
    if not unembedded:
        return
    texts = [c.content for c in unembedded]
    vectors = embed_texts(texts)
    for chunk, vec in zip(unembedded, vectors):
        chunk.embedding = vec


def deduplicate(chunks: list[Chunk], threshold: float = 0.85) -> list[Chunk]:
    """Remove near-duplicate chunks using pairwise cosine similarity.

    For any pair with similarity > threshold, the chunk with the lower
    RRF score is dropped. This is a purely mechanical, rule-based step.

    Args:
        chunks: List of Chunk objects with embeddings populated.
        threshold: Cosine similarity threshold for deduplication (default 0.85).

    Returns:
        De-duplicated list of Chunk objects.
    """
    if len(chunks) <= 1:
        return chunks

    # Ensure embeddings are available
    embed_chunks(chunks)

    matrix = np.array([c.embedding for c in chunks])
    sim_matrix = cosine_similarity(matrix)

    keep = [True] * len(chunks)
    for i in range(len(chunks)):
        if not keep[i]:
            continue
        for j in range(i + 1, len(chunks)):
            if not keep[j]:
                continue
            if sim_matrix[i, j] > threshold:
                # Drop the one with the lower RRF score
                if chunks[i].rrf_score >= chunks[j].rrf_score:
                    keep[j] = False
                else:
                    keep[i] = False
                    break

    return [c for c, k in zip(chunks, keep) if k]


# ─── Contradiction Detection ──────────────────────────────────────────────────

CONTRADICTION_PROMPT_TEMPLATE = """You are a medical knowledge curator for FertiliQ, a preconception health platform.

Below are {n} retrieved knowledge chunks. Analyse them for FACTUAL CONTRADICTIONS — cases where two chunks make opposing specific claims about the same topic (e.g., different supplement doses, conflicting biomarker thresholds, opposing clinical recommendations).

Chunks:
{chunks_text}

Identify any contradicting PAIRS. For each pair output a JSON object in this exact format:
{{
  "contradictions": [
    {{
      "chunk_a_id": "<id>",
      "chunk_b_id": "<id>",
      "contradiction_type": "<temporal|version|credibility>",
      "description": "<one sentence describing what specifically contradicts>"
    }}
  ]
}}

Contradiction type definitions:
- temporal: Chunks are from different time periods and the newer one supersedes the older recommendation
- version: Chunks are from different software/guideline versions (e.g. v1.0 vs v2.1)
- credibility: Chunks are from sources of different credibility levels that disagree

If no contradictions exist, return: {{"contradictions": []}}

Return ONLY the JSON object. No commentary before or after.
"""


def detect_contradictions(
    chunks: list[Chunk],
) -> tuple[list[ContradictionUnit], list[Chunk]]:
    """Use the LLM to identify contradicting chunk pairs before reranking.

    Args:
        chunks: De-duplicated list of Chunk objects.

    Returns:
        Tuple of:
          - List of ContradictionUnit objects (one per detected pair)
          - List of remaining Chunk objects not involved in any contradiction
    """
    if len(chunks) < 2:
        return [], chunks

    chunks_text = ""
    for i, c in enumerate(chunks):
        src = c.metadata.get("source_type", "unknown")
        date = c.metadata.get("date", "unknown")
        title = c.metadata.get("title", "untitled")
        version = c.metadata.get("version", "")
        ver_str = f" ({version})" if version else ""
        chunks_text += (
            f"\n--- Chunk {i+1} [ID: {c.id}] ---\n"
            f"Source: {src}{ver_str} | Date: {date} | Title: {title}\n"
            f"Content: {c.content[:600]}\n"
        )

    prompt = CONTRADICTION_PROMPT_TEMPLATE.format(
        n=len(chunks),
        chunks_text=chunks_text,
    )

    raw = generate(prompt).strip()

    # Strip markdown fences if present
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)

    try:
        data = json.loads(raw)
        detected = data.get("contradictions", [])
    except (json.JSONDecodeError, AttributeError):
        detected = []

    chunk_map = {c.id: c for c in chunks}
    contradiction_units: list[ContradictionUnit] = []
    involved_ids: set[str] = set()

    for item in detected:
        id_a = item.get("chunk_a_id", "")
        id_b = item.get("chunk_b_id", "")
        if id_a in chunk_map and id_b in chunk_map and id_a != id_b:
            unit = ContradictionUnit(
                chunk_a=chunk_map[id_a],
                chunk_b=chunk_map[id_b],
                contradiction_type=item.get("contradiction_type", "temporal"),
                description=item.get("description", ""),
            )
            contradiction_units.append(unit)
            involved_ids.add(id_a)
            involved_ids.add(id_b)

    clean_chunks = [c for c in chunks if c.id not in involved_ids]
    return contradiction_units, clean_chunks


# ─── LLM Reranking ───────────────────────────────────────────────────────────

RERANK_PROMPT_TEMPLATE = """You are a senior knowledge curator for FertiliQ, a preconception health platform.

User Question: "{query}"

You have {n_slots} candidate items below (each is either a single chunk or a contradiction unit — two contradicting chunks packaged together). Select the TOP 3 items that best answer the user's question.

Ranking criteria (in order of importance):
1. Relevance to the question
2. Source credibility: documentation > blog > forum
3. Recency: newer dates preferred
4. Query intent coverage: the top 3 should cover DIFFERENT dimensions of the answer (no pure duplicates)
5. A contradiction unit should be selected if it directly addresses the question and the contradiction is important for the user to know

Items:
{items_text}

Return a JSON object in this EXACT format:
{{
  "top3_ids": ["<slot_id_1>", "<slot_id_2>", "<slot_id_3>"],
  "reasoning": "<one sentence explaining your selection>"
}}

Use slot IDs exactly as shown. If fewer than 3 items exist, return as many as available.
Return ONLY the JSON. No other text.
"""


def llm_rerank(
    contradiction_units: list[ContradictionUnit],
    clean_chunks: list[Chunk],
    query: str,
) -> tuple[list, list[str]]:
    """Select the top 3 items using LLM-based reranking.

    Contradiction units and regular chunks are presented together. Each unit
    counts as a single slot. The LLM selects by relevance, credibility,
    recency and diversity.

    Args:
        contradiction_units: List of ContradictionUnit objects.
        clean_chunks: List of non-contradicting Chunk objects.
        query: The user's question.

    Returns:
        Tuple of:
          - List of up to 3 selected items (Chunk or ContradictionUnit)
          - List of 3 slot IDs in order (for logging rank comparison)
    """
    items = []
    items_text = ""

    # Add contradiction units
    for i, unit in enumerate(contradiction_units):
        slot_id = f"UNIT_{i}"
        items.append(("unit", slot_id, unit))
        ca, cb = unit.chunk_a, unit.chunk_b
        items_text += (
            f"\n[{slot_id}] CONTRADICTION UNIT — {unit.contradiction_type}\n"
            f"  Chunk A [{ca.id}]: Source={ca.metadata.get('source_type')} "
            f"({ca.metadata.get('version','')}) Date={ca.metadata.get('date')} "
            f"| {ca.content[:300]}\n"
            f"  Chunk B [{cb.id}]: Source={cb.metadata.get('source_type')} "
            f"({cb.metadata.get('version','')}) Date={cb.metadata.get('date')} "
            f"| {cb.content[:300]}\n"
            f"  Contradiction: {unit.description}\n"
        )

    # Add regular chunks
    for chunk in clean_chunks:
        slot_id = chunk.id
        items.append(("chunk", slot_id, chunk))
        items_text += (
            f"\n[{slot_id}] CHUNK — Source={chunk.metadata.get('source_type')} "
            f"Date={chunk.metadata.get('date')} Title={chunk.metadata.get('title','')}\n"
            f"  {chunk.content[:400]}\n"
        )

    if not items:
        return [], []

    prompt = RERANK_PROMPT_TEMPLATE.format(
        query=query,
        n_slots=len(items),
        items_text=items_text,
    )

    raw = generate(prompt).strip()
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)

    try:
        data = json.loads(raw)
        top3_ids = data.get("top3_ids", [])
    except (json.JSONDecodeError, AttributeError):
        top3_ids = [it[1] for it in items[:3]]

    id_to_item = {it[1]: it for it in items}
    selected = []
    selected_ids = []
    for slot_id in top3_ids[:3]:
        if slot_id in id_to_item:
            selected.append(id_to_item[slot_id][2])
            selected_ids.append(slot_id)

    return selected, selected_ids
