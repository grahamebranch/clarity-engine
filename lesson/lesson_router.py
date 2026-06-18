"""
Lesson Router — decides what kind of lesson to build.
"""

class LessonRouter:
    def route(self, text: str) -> str:
        """
        Return a simple lesson_type string based on keywords.
        Deterministic, no AI guessing.
        """

        t = text.strip().lower()

        # Conversation-focused lessons
        convo_keywords = ["conversation", "speaking", "dialogue", "role play", "role-play"]
        if any(k in t for k in convo_keywords):
            return "conversation"

        # Vocabulary-focused lessons
        vocab_keywords = ["vocabulary", "words", "phrases", "lexis"]
        if any(k in t for k in vocab_keywords):
            return "vocabulary"

        # Grammar-focused lessons
        grammar_keywords = ["grammar", "tense", "conditionals", "articles", "prepositions"]
        if any(k in t for k in grammar_keywords):
            return "grammar"

        # Default lesson type
        return "conversation"
