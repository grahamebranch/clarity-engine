"""
Level Router — determines the CEFR level for the lesson.
"""

from typing import Optional


class LevelRouter:
    def route(self, text: str) -> Optional[str]:
        """
        Determine the level based on keywords.
        Returns one of: "A2", "B1", "B2", "C1".
        Default: B1 (safe middle ground).
        """

        t = text.strip().lower()

        if "a2" in t or "elementary" in t:
            return "A2"

        if "b1" in t or "intermediate" in t:
            return "B1"

        if "b2" in t or "upper intermediate" in t:
            return "B2"

        if "c1" in t or "advanced" in t:
            return "C1"

        # Default level
        return "B1"
