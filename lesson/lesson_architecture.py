"""
Lesson Architecture — deterministic skeleton for each lesson type.
Upgraded to align with the new LessonGenerator engine.
"""

from typing import List, Dict


class LessonArchitectureBuilder:
    """
    Builds the deterministic architecture for a lesson.
    The upgraded LessonGenerator calls:
        architecture = builder.build(topic, level, domain)
    """

    def build(self, topic: str, level: str, domain: str) -> List[Dict[str, str]]:
        """
        Determine the lesson type from domain or fallback to conversation.
        Domain may later map to:
            - conversation
            - vocabulary
            - grammar
            - business
            - exam
            - etc.
        For now, we keep deterministic behaviour.
        """

        lesson_type = self._resolve_lesson_type(domain)
        return self._get_architecture(lesson_type)

    # ---------------------------------------------------------
    # INTERNAL RESOLUTION
    # ---------------------------------------------------------

    def _resolve_lesson_type(self, domain: str) -> str:
        """
        Maps domain → lesson type.
        This keeps the system extensible without guessing.
        """

        domain = domain.lower().strip()

        if domain in ("conversation", "general", "speaking"):
            return "conversation"

        if domain in ("vocabulary", "lexis"):
            return "vocabulary"

        if domain in ("grammar", "structure"):
            return "grammar"

        # fallback
        return "conversation"

    # ---------------------------------------------------------
    # ARCHITECTURE DEFINITIONS
    # ---------------------------------------------------------

    def _get_architecture(self, lesson_type: str) -> List[Dict[str, str]]:
        """
        Return a list of section specs:
        [{ "id": "warmup", "title": "Warm-up", "role": "..." }, ...]
        """

        if lesson_type == "conversation":
            return [
                {"id": "warmup", "title": "Warm-up", "role": "activate topic and prior knowledge"},
                {"id": "dialogue", "title": "Core Dialogue", "role": "model target language in context"},
                {"id": "questions", "title": "Discussion Questions", "role": "prompt speaking and opinion sharing"},
                {"id": "vocab", "title": "Vocabulary Focus", "role": "highlight useful phrases and expressions"},
                {"id": "reflection", "title": "Reflection Task", "role": "encourage personal connection to the topic"},
            ]

        if lesson_type == "vocabulary":
            return [
                {"id": "warmup", "title": "Warm-up", "role": "introduce the lexical field"},
                {"id": "input", "title": "Input Text", "role": "provide context for target vocabulary"},
                {"id": "items", "title": "Target Vocabulary", "role": "list and clarify key items"},
                {"id": "practice", "title": "Controlled Practice", "role": "use items in guided tasks"},
                {"id": "free", "title": "Freer Practice", "role": "use items in personal, open tasks"},
            ]

        if lesson_type == "grammar":
            return [
                {"id": "context", "title": "Context", "role": "show grammar in natural use"},
                {"id": "noticing", "title": "Noticing", "role": "draw attention to the form and meaning"},
                {"id": "clarification", "title": "Clarification", "role": "explain rules and patterns"},
                {"id": "practice", "title": "Practice", "role": "controlled exercises"},
                {"id": "production", "title": "Production", "role": "freer use in speaking or writing"},
            ]

        # Fallback: conversation skeleton
        return self._get_architecture("conversation")
