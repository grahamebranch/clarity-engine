def score_text(text: str) -> int:
    """
    Simple deterministic clarity score (0–100).
    v0.1 heuristic:
    - penalize very long or very short text
    - penalize excessive punctuation
    - reward moderate length and clean structure
    """
    if not text or not text.strip():
        return 0

    length = len(text)

    if length < 50:
        base = 40
    elif length < 200:
        base = 70
    elif length < 800:
        base = 85
    else:
        base = 60

    punct = sum(text.count(p) for p in "!?;:")
    penalty = min(punct * 2, 20)

    score = base - penalty
    return max(0, min(100, score))
