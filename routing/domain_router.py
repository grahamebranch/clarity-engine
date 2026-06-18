"""
Domain Routing Layer — FastPath Version
Determines what type of request the engine should process.
"""

class DomainRouter:
    def route(self, text: str) -> str:
        """
        Determine the request type based on simple deterministic rules.
        No AI interpretation. No semantic guessing.
        """

        t = text.strip().lower()

        # Console commands (start with /)
        if t.startswith("/"):
            return "console"

        # Safety rewrite triggers
        if "rewrite safely" in t or "safety rewrite" in t:
            return "safety"

        # Lesson generation triggers
        lesson_keywords = [
            "lesson", "teach", "explain", "topic", "esl", "exercise",
            "vocabulary", "dialogue", "practice", "student edition",
            "trainer edition"
        ]
        if any(k in t for k in lesson_keywords):
            return "lesson"

        # Default: raw text processing
        return "raw"
