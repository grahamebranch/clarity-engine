"""
Topic Extractor — determines the core topic of a lesson request.
Deterministic, rule-based, no AI guessing.
"""

from typing import Optional


class TopicExtractor:
    def extract(self, text: str) -> Optional[str]:
        """
        Extract a clean topic from the user's input.
        Strategy:
        - If the user writes "lesson on X", extract X.
        - If the user writes "teach me about X", extract X.
        - If the user writes "topic: X", extract X.
        - Otherwise, fall back to the first 6–8 words.
        """

        t = text.strip()

        lower = t.lower()

        # Pattern 1: "lesson on X"
        if "lesson on" in lower:
            return t.lower().split("lesson on", 1)[1].strip().capitalize()

        # Pattern 2: "teach me about X"
        if "teach me about" in lower:
            return t.lower().split("teach me about", 1)[1].strip().capitalize()

        # Pattern 3: "topic: X"
        if "topic:" in lower:
            return t.split("topic:", 1)[1].strip().capitalize()

        # Fallback: first 6–8 words
        words = t.split()
        if len(words) <= 8:
            return t.capitalize()
        return " ".join(words[:8]).capitalize()
