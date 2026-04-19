"""
FertiliQ Performance Analysis Module
Reads logs/query_log.json and prints a summary report including:
  - Source distribution in top-3
  - Contradiction detection rate
  - Average latency
  - Reranking impact (slot IDs before vs after reranking)
  - Per-query summary table
"""

import json
from collections import Counter
from pathlib import Path

LOG_PATH = Path(__file__).parent / "logs" / "query_log.json"


def load_log() -> list[dict]:
    """Load all query log entries from query_log.json.

    Returns:
        List of log entry dicts. Empty list if file not found or invalid.
    """
    if not LOG_PATH.exists() or LOG_PATH.stat().st_size == 0:
        return []
    with open(LOG_PATH, encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def source_distribution(entries: list[dict]) -> dict[str, int]:
    """Count how often each source type appears in top-3 across all queries.

    Args:
        entries: List of log entry dicts.

    Returns:
        Dict mapping source_type to count.
    """
    counts: Counter = Counter()
    for entry in entries:
        for src in entry.get("top3_sources", []):
            src_type = src.get("type", "unknown")
            counts[src_type] += 1
    return dict(counts)


def contradiction_rate(entries: list[dict]) -> float:
    """Calculate the percentage of queries that triggered contradiction handling.

    Args:
        entries: List of log entry dicts.

    Returns:
        Float in [0, 1]; 0 if no entries.
    """
    if not entries:
        return 0.0
    triggered = sum(1 for e in entries if e.get("contradictions_detected", False))
    return triggered / len(entries)


def average_latency(entries: list[dict]) -> float:
    """Compute the mean query latency in milliseconds.

    Args:
        entries: List of log entry dicts.

    Returns:
        Average latency in ms; 0.0 if no entries.
    """
    latencies = [e.get("latency_ms", 0) for e in entries if e.get("latency_ms")]
    return sum(latencies) / len(latencies) if latencies else 0.0


def print_report(entries: list[dict]) -> None:
    """Print a formatted performance report to stdout.

    Args:
        entries: List of log entry dicts.
    """
    if not entries:
        print("No log entries found. Run some queries first.")
        return

    print("=" * 70)
    print("  FERTILIQ RAG — PERFORMANCE ANALYSIS REPORT")
    print("=" * 70)
    print(f"  Total queries logged : {len(entries)}")
    print()

    # Source distribution
    dist = source_distribution(entries)
    total_src = sum(dist.values()) or 1
    print("SOURCE DISTRIBUTION IN TOP-3:")
    for src_type in ["documentation", "blog", "forum"]:
        count = dist.get(src_type, 0)
        pct = count / total_src * 100
        bar = "#" * int(pct / 5)
        print(f"  {src_type:<16} {count:>4} appearances  ({pct:5.1f}%)  {bar}")
    print()

    # Contradiction rate
    rate = contradiction_rate(entries)
    print(f"CONTRADICTION DETECTION RATE : {rate*100:.1f}% "
          f"({int(rate*len(entries))}/{len(entries)} queries)")
    if any(e.get("contradictions_detected") for e in entries):
        conf_vals = [
            e.get("contradiction_confidence", 0)
            for e in entries
            if e.get("contradictions_detected")
        ]
        avg_conf = sum(conf_vals) / len(conf_vals) if conf_vals else 0
        print(f"  Avg contradiction confidence : {avg_conf:.3f}")
        all_types: Counter = Counter()
        for e in entries:
            for t in e.get("contradiction_types", []):
                all_types[t] += 1
        if all_types:
            print(f"  Contradiction types detected : {dict(all_types)}")
    print()

    # Latency
    avg_lat = average_latency(entries)
    print(f"AVERAGE LATENCY : {avg_lat:.0f} ms  ({avg_lat/1000:.1f}s)")
    latencies = [e.get("latency_ms", 0) for e in entries if e.get("latency_ms")]
    if latencies:
        print(f"  Min: {min(latencies)} ms   Max: {max(latencies)} ms")
    print()

    # Per-query summary
    print("PER-QUERY SUMMARY:")
    print(f"  {'#':<4} {'Contradiction':>13} {'Confidence':>10} {'Latency':>9} {'After dedup':>11}  Query (truncated)")
    print("  " + "-" * 75)
    for i, e in enumerate(entries, 1):
        contradiction = "YES" if e.get("contradictions_detected") else "no"
        conf = f"{e.get('contradiction_confidence', 0):.2f}"
        lat = f"{e.get('latency_ms', 0)} ms"
        dedup = e.get("after_dedup", 0)
        q = e.get("query", "")[:48]
        print(f"  {i:<4} {contradiction:>13} {conf:>10} {lat:>9} {dedup:>11}  {q}")

    print()

    # Dedup efficiency
    total_before = sum(e.get("candidates_retrieved", 30) for e in entries)
    total_after = sum(e.get("after_dedup", 0) for e in entries)
    if total_before:
        reduction = (1 - total_after / total_before) * 100
        print(f"DEDUPLICATION: {reduction:.1f}% average reduction "
              f"({total_before // len(entries)} -> {total_after // len(entries)} candidates avg)")

    print()
    print("=" * 70)


if __name__ == "__main__":
    data = load_log()
    print_report(data)
