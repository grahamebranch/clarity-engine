"""
Clarity Scoring v1.0 — FastPath Version
Deterministic, explainable, section-level scoring.
"""

def score_sections(sections: list[dict]) -> dict:
    """
    Produces:
      - overall score (0–100)
      - per-section scores
    """

    if not sections:
        return {"score": 0, "per_section": []}

    per_section = []

    for sec in sections:
        blocks = sec.get("blocks", []) or []
        text = "\n".join(b.get("text", "") for b in blocks)

        score = 0

        # ----------------------------------------------------
        # 1. Length fitness (ideal: 40–180 chars)
        # ----------------------------------------------------
        length = len(text)
        if 40 <= length <= 180:
            score += 30
        elif 20 <= length <= 300:
            score += 20
        else:
            score += 10

        # ----------------------------------------------------
        # 2. Structure clarity
        # ----------------------------------------------------
        if blocks:
            score += 20
        if any(b.get("text", "").startswith(("-", "*", "•")) for b in blocks):
            score += 10

        # ----------------------------------------------------
        # 3. Sentence clarity
        # ----------------------------------------------------
        sentences = [s.strip() for s in text.split(".") if s.strip()]
        if sentences:
            avg_len = sum(len(s) for s in sentences) / len(sentences)
            if avg_len <= 120:
                score += 20
            elif avg_len <= 200:
                score += 10

        # ----------------------------------------------------
        # 4. Noise penalty
        # ----------------------------------------------------
        noise_tokens = ["???", "lorem", "asdf", "xxxx"]
        if any(tok in text.lower() for tok in noise_tokens):
            score -= 10

        # Clamp
        score = max(0, min(100, score))

        sec["clarity_score"] = score
        per_section.append({"id": sec.get("id"), "score": score})

    # --------------------------------------------------------
    # Overall score = weighted average
    # --------------------------------------------------------
    overall = int(sum(s["score"] for s in per_section) / len(per_section))

    return {
        "score": overall,
        "per_section": per_section
    }
