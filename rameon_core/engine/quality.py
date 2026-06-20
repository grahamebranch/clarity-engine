"""
Quality Scoring Layer (EL-12)
Simple deterministic heuristics for text quality.
"""

class QualityScorer:
    def __init__(self):
        pass

    def score(self, text: str, sections: list):
        scores = []

        # Length score
        length_score = min(len(text) / 500, 1.0)
        scores.append({
            "metric": "length",
            "value": round(length_score, 2),
            "details": f"Text length: {len(text)} chars"
        })

        # Section count score
        section_score = min(len(sections) / 5, 1.0)
        scores.append({
            "metric": "section_count",
            "value": round(section_score, 2),
            "details": f"Sections: {len(sections)}"
        })

        # Average section length score
        if sections:
            avg_len = sum(len(s['content']) for s in sections) / len(sections)
            avg_score = min(avg_len / 300, 1.0)
        else:
            avg_score = 0

        scores.append({
            "metric": "avg_section_length",
            "value": round(avg_score, 2),
            "details": f"Average section length: {round(avg_len, 2) if sections else 0}"
        })

        # Final composite score
        composite = round(
            (length_score + section_score + avg_score) / 3, 2
        )

        return {
            "composite": composite,
            "metrics": scores
        }
