"""
FertiliQ Response Generation
Generates the final user-facing answer from the top-3 reranked items.

If any ContradictionUnit is in the top 3:
  - Compute contradiction_confidence = f(credibility_gap, time_gap, specificity)
  - High confidence (>0.7): give clear directive recommendation with full reasoning
  - Low confidence (≤0.7): give directional recommendation acknowledging uncertainty

Never gives "consult a doctor" as primary response — always a concrete recommendation first.
Always appends formatted source citations.
"""

import re

from src.gemini_client import generate
from src.reranking import Chunk, ContradictionUnit

CREDIBILITY_SCORE = {"documentation": 1.0, "blog": 0.67, "forum": 0.33}


# ─── Contradiction confidence ─────────────────────────────────────────────────

def _parse_year(date_str: str) -> int:
    """Extract the year from a date string (YYYY-MM-DD or YYYY format).

    Args:
        date_str: A date string, possibly 'unknown'.

    Returns:
        Integer year, or 2020 as fallback.
    """
    if not date_str or date_str == "unknown":
        return 2020
    try:
        return int(str(date_str)[:4])
    except ValueError:
        return 2020


def compute_contradiction_confidence(unit: ContradictionUnit) -> float:
    """Calculate the contradiction confidence score for a ContradictionUnit.

    Score = mean(credibility_gap, time_gap_norm, specificity_estimate)
    All components clamped to [0, 1].

    credibility_gap : absolute difference in source credibility scores
    time_gap_norm   : years between sources / 5 (capped at 1)
    specificity     : 0.9 if description contains numeric values, else 0.5

    Args:
        unit: A ContradictionUnit with two chunks.

    Returns:
        Confidence float in [0.0, 1.0].
    """
    src_a = unit.chunk_a.metadata.get("source_type", "forum")
    src_b = unit.chunk_b.metadata.get("source_type", "forum")
    cred_a = CREDIBILITY_SCORE.get(src_a, 0.33)
    cred_b = CREDIBILITY_SCORE.get(src_b, 0.33)
    credibility_gap = abs(cred_a - cred_b)

    year_a = _parse_year(unit.chunk_a.metadata.get("date", ""))
    year_b = _parse_year(unit.chunk_b.metadata.get("date", ""))
    time_gap_norm = min(abs(year_a - year_b) / 5.0, 1.0)

    # Specificity: higher if description contains digits (specific doses/values)
    has_numeric = bool(re.search(r"\d", unit.description))
    specificity = 0.9 if has_numeric else 0.5

    score = (credibility_gap + time_gap_norm + specificity) / 3.0
    return round(min(max(score, 0.0), 1.0), 3)


# ─── Source citation builder ──────────────────────────────────────────────────

def _format_citation(item) -> str:
    """Build a single formatted citation line for a Chunk or ContradictionUnit.

    Args:
        item: A Chunk or ContradictionUnit.

    Returns:
        A citation string.
    """
    if isinstance(item, ContradictionUnit):
        lines = []
        for chunk in [item.chunk_a, item.chunk_b]:
            lines.append(_chunk_citation(chunk) + " ⚠️ [CONTRADICTION]")
        return "\n".join(lines)
    return _chunk_citation(item)


def _chunk_citation(chunk: Chunk) -> str:
    """Format a citation for a single Chunk.

    Args:
        chunk: A Chunk object.

    Returns:
        A formatted citation string.
    """
    src = chunk.metadata.get("source_type", "unknown").capitalize()
    title = chunk.metadata.get("title", "Untitled")
    date = chunk.metadata.get("date", "unknown")
    version = chunk.metadata.get("version", "")

    extra = ""
    if src == "Forum":
        votes = chunk.metadata.get("votes", 0)
        accepted = chunk.metadata.get("is_accepted", False)
        extra = f" (👍 {votes}" + (" ✓ Accepted" if accepted else "") + ")"

    ver_str = f" {version}" if version else ""
    return f"[{src}] {title}{ver_str} ({date}){extra}"


# ─── Main generation function ─────────────────────────────────────────────────

DIRECT_ANSWER_PROMPT = """You are FertiliQ's AI health advisor. Answer the user's question using ONLY the provided source chunks. Be specific and actionable. Never give "consult a doctor" as the primary response — lead with a concrete recommendation.

User Question: {query}

Source Chunks:
{chunks_text}

Instructions:
- Give a clear, direct, evidence-based answer of 150–250 words
- Reference the most credible source (documentation > blog > forum)
- Note any key nuances (age, genetic variant, biomarker level)
- End with "---" on its own line (citations will be appended separately)
"""

CONTRADICTION_HIGH_CONF_PROMPT = """You are FertiliQ's AI health advisor. One of the sources directly contradicts another. Your job is to give the user a CLEAR directive recommendation, not hedge.

User Question: {query}

CONTRADICTION DETECTED ({contradiction_type}):
{contradiction_desc}

Newer/more credible source says: {newer_content}
Older/less credible source says: {older_content}

Other relevant sources:
{other_chunks_text}

Instructions:
- Lead with the correct, current recommendation based on the newer/more credible source
- Explain WHY the older recommendation is outdated (1–2 sentences)
- Be specific: include doses, values, or actions where relevant
- Do not hedge excessively — give a directive answer (150–250 words)
- End with "---" on its own line
"""

CONTRADICTION_LOW_CONF_PROMPT = """You are FertiliQ's AI health advisor. There is a disagreement between sources on this topic. Your job is to give the user directional guidance while acknowledging uncertainty.

User Question: {query}

CONFLICTING INFORMATION ({contradiction_type}):
{contradiction_desc}

Source A says: {content_a}
Source B says: {content_b}

Other relevant sources:
{other_chunks_text}

Instructions:
- Lead with the current best-evidence recommendation
- Acknowledge the uncertainty (1 sentence)
- Offer a practical starting point the user can act on
- Be specific: include doses, values, or actions where relevant
- Do not make the uncertainty paralyse the advice (150–250 words)
- End with "---" on its own line
"""


def _build_chunks_text(chunks: list[Chunk]) -> str:
    """Format a list of Chunk objects into readable prompt text.

    Args:
        chunks: List of Chunk objects.

    Returns:
        Multi-line formatted string.
    """
    out = ""
    for c in chunks:
        src = c.metadata.get("source_type", "unknown")
        date = c.metadata.get("date", "")
        title = c.metadata.get("title", "")
        out += f"\n[{src} | {date} | {title}]\n{c.content[:600]}\n"
    return out


def generate_response(
    query: str,
    top3: list,
) -> tuple[str, float, bool]:
    """Generate a response from the top-3 reranked items.

    Args:
        query: The user's original question.
        top3: List of up to 3 items (Chunk or ContradictionUnit).

    Returns:
        Tuple of:
          - response_text: The complete formatted response with citations
          - contradiction_confidence: Confidence score (0.0 if no contradiction)
          - contradictions_present: Whether any contradiction was in top3
    """
    contradiction_units = [i for i in top3 if isinstance(i, ContradictionUnit)]
    clean_chunks = [i for i in top3 if isinstance(i, Chunk)]
    contradictions_present = bool(contradiction_units)
    contradiction_confidence = 0.0

    # ── Case 1: No contradictions ─────────────────────────────────────────────
    if not contradiction_units:
        chunks_text = _build_chunks_text(clean_chunks)
        prompt = DIRECT_ANSWER_PROMPT.format(query=query, chunks_text=chunks_text)
        answer = generate(prompt).strip()
        if "---" in answer:
            answer = answer[:answer.rfind("---")].strip()

    # ── Case 2: Contradiction present ─────────────────────────────────────────
    else:
        unit = contradiction_units[0]
        contradiction_confidence = compute_contradiction_confidence(unit)
        unit.confidence = contradiction_confidence

        other_chunks_text = _build_chunks_text(clean_chunks)

        # Determine which chunk is newer / more credible
        cred_a = CREDIBILITY_SCORE.get(unit.chunk_a.metadata.get("source_type", "forum"), 0.33)
        cred_b = CREDIBILITY_SCORE.get(unit.chunk_b.metadata.get("source_type", "forum"), 0.33)
        year_a = _parse_year(unit.chunk_a.metadata.get("date", ""))
        year_b = _parse_year(unit.chunk_b.metadata.get("date", ""))

        # Prefer credibility; use recency as tiebreaker
        if cred_a > cred_b or (cred_a == cred_b and year_a >= year_b):
            newer, older = unit.chunk_a, unit.chunk_b
        else:
            newer, older = unit.chunk_b, unit.chunk_a

        if contradiction_confidence > 0.7:
            prompt = CONTRADICTION_HIGH_CONF_PROMPT.format(
                query=query,
                contradiction_type=unit.contradiction_type,
                contradiction_desc=unit.description,
                newer_content=newer.content[:600],
                older_content=older.content[:400],
                other_chunks_text=other_chunks_text,
            )
        else:
            prompt = CONTRADICTION_LOW_CONF_PROMPT.format(
                query=query,
                contradiction_type=unit.contradiction_type,
                contradiction_desc=unit.description,
                content_a=unit.chunk_a.content[:500],
                content_b=unit.chunk_b.content[:500],
                other_chunks_text=other_chunks_text,
            )

        answer = generate(prompt).strip()
        if "---" in answer:
            answer = answer[:answer.rfind("---")].strip()

    # ── Append citations ──────────────────────────────────────────────────────
    citations = "\n\n**Sources:**"
    for item in top3:
        citations += "\n" + _format_citation(item)

    full_response = answer + citations

    return full_response, contradiction_confidence, contradictions_present


def get_top3_source_metadata(top3: list) -> list[dict]:
    """Extract source metadata dicts for logging from the top-3 items.

    Args:
        top3: List of Chunk or ContradictionUnit objects.

    Returns:
        List of dicts with 'type', 'title', 'date'.
    """
    sources = []
    for item in top3:
        if isinstance(item, ContradictionUnit):
            for chunk in [item.chunk_a, item.chunk_b]:
                sources.append({
                    "type": chunk.metadata.get("source_type", "unknown"),
                    "title": chunk.metadata.get("title", ""),
                    "date": chunk.metadata.get("date", ""),
                })
        else:
            sources.append({
                "type": item.metadata.get("source_type", "unknown"),
                "title": item.metadata.get("title", ""),
                "date": item.metadata.get("date", ""),
            })
    return sources[:4]  # cap at 4 for log readability
