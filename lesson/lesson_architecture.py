"""
Lesson Architecture — defines the skeleton for each lesson type.
"""

from typing import List, Dict


class LessonArchitecture:
    def get_architecture(self, lesson_type: str) -> List[Dict[str, str]]:
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
        return self.get_architecture("conversation")
