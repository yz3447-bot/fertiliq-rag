"""
FertiliQ Query Logger
Appends structured log entries to logs/query_log.json after each query.
"""

import json
import os
from datetime import datetime
from pathlib import Path

LOG_PATH = Path(__file__).parent.parent / "logs" / "query_log.json"


def log_query(
    query: str,
    candidates_retrieved: int,
    after_dedup: int,
    contradictions_detected: bool,
    contradiction_types: list,
    contradiction_confidence: float,
    top3_sources: list,
    response_generated: bool,
    latency_ms: int,
) -> None:
    """Append a single query record to the JSON log file.

    Args:
        query: The user's question string.
        candidates_retrieved: Total candidates from hybrid search (typically 30).
        after_dedup: Number of unique candidates after deduplication.
        contradictions_detected: Whether any contradiction units were found.
        contradiction_types: List of detected contradiction type strings.
        contradiction_confidence: Confidence score 0.0–1.0 (0 if none).
        top3_sources: List of dicts with 'type', 'title', 'date' for the top 3 sources.
        response_generated: Whether a response was successfully generated.
        latency_ms: Total end-to-end latency in milliseconds.
    """
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    existing: list = []
    if LOG_PATH.exists() and LOG_PATH.stat().st_size > 0:
        try:
            with open(LOG_PATH, "r", encoding="utf-8") as f:
                existing = json.load(f)
        except (json.JSONDecodeError, ValueError):
            existing = []

    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "query": query,
        "candidates_retrieved": candidates_retrieved,
        "after_dedup": after_dedup,
        "contradictions_detected": contradictions_detected,
        "contradiction_types": contradiction_types,
        "contradiction_confidence": round(contradiction_confidence, 3),
        "top3_sources": top3_sources,
        "response_generated": response_generated,
        "latency_ms": latency_ms,
    }
    existing.append(entry)

    with open(LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)


def read_log() -> list:
    """Return all log entries as a list of dicts."""
    if not LOG_PATH.exists() or LOG_PATH.stat().st_size == 0:
        return []
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
