# conversation_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Conversation Domain Pack (v1)

from typing import Dict, Any

class ConversationDomainPack:
    """
    ConversationDomainPack
    Generates conceptual content for a conversational lesson.
    Uses the LessonGenerator to produce raw text, then structures it
    into section payloads expected by the LessonComposer.
    """

    def __init__(self, generator):
        self.generator = generator
        self.version = "1.0"

    # ---------------------------------------------------------
    # MAIN ENTRY POINT
    # ---------------------------------------------------------
    def generate(self, topic: str) -> Dict[str, Dict[str, Any]]:
        """
        Returns a dictionary mapping section roles to payloads.
        Each payload contains:
        - 'text': main explanation
        - 'points': optional bullet points
        """

        raw = self.generator.generate_raw(topic)

        return {
            "introduction": {
                "text": raw.get("introduction", ""),
                "points": raw.get("intro_points", []),
            },
            "core_concepts": {
                "text": raw.get("core", ""),
                "points": raw.get("core_points", []),
            },
            "examples": {
                "text": raw.get("examples", ""),
                "points": raw.get("example_points", []),
            },
            "practice": {
                "text": raw.get("practice", ""),
                "points": raw.get("practice_points", []),
            },
            "summary": {
                "text": raw.get("summary", ""),
                "points": raw.get("summary_points", []),
            },
        }
