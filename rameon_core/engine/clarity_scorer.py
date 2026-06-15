"""
Clarity Scorer v1.0
-------------------
Computes a clarity score for each section and an overall document score.

Inputs (from DIS5 + EL2 + EL4 + EL3):
- length
- avg_sentence_length
- density
- cohesion_score
- keywords

Outputs:
- overall score (0–100)
- per-section scores
"""

def score_sections(sections: list[dict]) -> dict:
    if not sections:
        return {"score": 0, "per_section": []}

    per_section = []

    for sec in sections:
        meta = sec.get("metadata", {})

        length = meta.get("length", 1)
        avg_len = meta.get("avg_sentence_length", 1)
        density = meta.get("density", 1)
        cohesion = meta.get("cohesion_score", 0)

        # -------------------------------
        # Scoring components (0–100 each)
        # -------------------------------

        # 1. Cohesion (strongest signal)
        cohesion_score = max(0, min(100, cohesion * 20))

        # 2. Sentence length (shorter = clearer)
        if avg_len <= 80:
            sentence_score = 100
        elif avg_len <= 140:
            sentence_score = 70
        elif avg_len <= 200:
            sentence_score = 40
        else:
            sentence_score = 10

        # 3. Density (lower = clearer)
        if density <= 80:
            density_score = 100
        elif density <= 140:
            density_score = 70
        elif density <= 200:
            density_score = 40
        else:
            density_score = 10

        # 4. Length (ideal ≈ 3 units)
        length_penalty = abs(length - 3) * 10
        length_score = max(0, 100 - length_penalty)

        # -------------------------------
        # Weighted final score
        # -------------------------------
        final_score = (
            cohesion_score * 0.4 +
            sentence_score * 0.25 +
            density_score * 0.2 +
            length_score * 0.15
        )

        per_section.append({
            "id": sec.get("id"),
            "score": round(final_score, 2)
        })

    # Overall score = average of section scores
    overall = sum(s["score"] for s in per_section) / len(per_section)

    return {
        "score": round(overall, 2),
        "per_section": per_section
    }
