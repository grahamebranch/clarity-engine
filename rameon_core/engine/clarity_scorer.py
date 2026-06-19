"""
ClarityScorer — deterministic clarity scoring for generated lessons.
"""

from typing import Dict, Any


class ClarityScorer:
    """
    Provides a simple, deterministic clarity score for a generated lesson.
    """

    def score(self, lesson: Dict[str, Any]) -> Dict[str, Any]:
        """
        Returns a clarity score object:
        {
            "score": float,
            "explanation": str
        }
        """

        # Basic deterministic scoring based on section completeness
        sections = lesson.get("sections", [])
        num_sections = len(sections)

        if num_sections == 0:
            return {
                "score": 0.0,
                "explanation": "No sections were generated, so clarity cannot be assessed."
            }

        # Simple heuristic: more complete sections = higher clarity
        completeness = sum(
            1 for s in sections
            if s.get("title") and s.get("content")
        )

        score = round((completeness / num_sections) * 10, 2)

        return {
            "score": score,
            "explanation": (
                f"The lesson contains {completeness} fully-formed sections "
                f"out of {num_sections}, resulting in a clarity score of {score}."
            )
        }
