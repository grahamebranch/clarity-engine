# rameon_core/engine/clarity_scorer.py

from typing import List, Dict

def score_section(text: str, section_type: str) -> int:
    """
    Very simple clarity scoring v0.1
    Returns a score 0–100 based on length + basic heuristics.
    """
    length = len(text)

    # Base score
    score = 100

    # Penalise very short sections
    if length < 20:
        score -= 20

    # Penalise very long sections
    if length > 300:
        score -= 25

    # Penalise ALL CAPS
    if text.isupper():
        score -= 30

    # Lists get a small penalty (less narrative clarity)
    if section_type == "list":
        score -= 10

    # Clamp to 0–100
    return max(0, min(100, score))


def score_sections(sections: List[Dict]) -> Dict:
    """
    Returns:
    {
        "score": overall_score,
        "per_section": [
            {"id": 1, "score": 80},
            ...
        ]
    }
    """
    per_section = []
    total = 0

    for s in sections:
        sec_score = score_section(s["text"], s["type"])
        per_section.append({"id": s["id"], "score": sec_score})
        total += sec_score

    overall = int(total / len(sections)) if sections else 0

    return {
        "score": overall,
        "per_section": per_section
    }
