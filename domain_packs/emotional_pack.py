# emotional_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Domain Pack: Emotional (v1)

from typing import List, Dict

class EmotionalPack:
    """
    Domain Pack: Emotional
    Provides empathetic, supportive, reflective content.
    Ideal for emotional understanding, personal reflection,
    and gentle guidance.
    """

    def __init__(self):
        self.domain_name = "emotional"
        self.version = "1.0"

    # ---------------------------------------------------------
    # SECTION TEMPLATES
    # ---------------------------------------------------------
    def get_sections(self, topic: str) -> List[Dict]:
        """
        Defines the structure of an emotional-style lesson.
        Emphasis on empathy, reflection, and emotional clarity.
        """
        return [
            {
                "title": f"Emotional Context: {topic}",
                "content": (
                    f"This section gently introduces '{topic}' from an emotional perspective. "
                    f"It acknowledges the feelings, challenges, or sensitivities that may arise."
                )
            },
            {
                "title": "What You Might Be Feeling",
                "content": (
                    f"We explore common emotional responses related to '{topic}'. "
                    f"This helps normalize the experience and create space for reflection."
                )
            },
            {
                "title": "Understanding the Deeper Layers",
                "content": (
                    f"This section looks beneath the surface of '{topic}' to uncover deeper "
                    f"needs, motivations, or emotional patterns that may be involved."
                )
            },
            {
                "title": "Supportive Guidance",
                "content": (
                    f"Here we offer gentle, practical suggestions for navigating '{topic}' "
                    f"with clarity and self-compassion."
                )
            },
            {
                "title": "A Grounding Thought",
                "content": (
                    f"A closing reflection designed to bring calm, perspective, "
                    f"and emotional steadiness around '{topic}'."
                )
            }
        ]

    # ---------------------------------------------------------
    # TONE RULES
    # ---------------------------------------------------------
    def get_tone(self) -> str:
        """
        Emotional pack uses a warm, empathetic tone.
        """
        return "empathetic"

    # ---------------------------------------------------------
    # METADATA
    # ---------------------------------------------------------
    def get_metadata(self) -> Dict:
        return {
            "domain": self.domain_name,
            "version": self.version
        }

    # ---------------------------------------------------------
    # MAIN ENTRY POINT
    # ---------------------------------------------------------
    def generate(self, topic: str) -> Dict:
        """
        Main method called by the engine.
        Returns a structured emotional lesson dictionary.
        """
        return {
            "engine_version": "1.0",
            "domain": self.domain_name,
            "tone": self.get_tone(),
            "sections": self.get_sections(topic)
        }
