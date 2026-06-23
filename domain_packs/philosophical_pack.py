# philosophical_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Domain Pack: Philosophical (v1)

from typing import List, Dict

class PhilosophicalPack:
    """
    Domain Pack: Philosophical
    Provides reflective, conceptual, meaning-oriented exploration.
    Ideal for deeper questions, reasoning, perspective, and insight.
    """

    def __init__(self):
        self.domain_name = "philosophical"
        self.version = "1.0"

    # ---------------------------------------------------------
    # SECTION TEMPLATES
    # ---------------------------------------------------------
    def get_sections(self, topic: str) -> List[Dict]:
        """
        Defines the structure of a philosophical-style lesson.
        Emphasis on meaning, reasoning, and conceptual clarity.
        """
        return [
            {
                "title": f"The Nature of {topic}",
                "content": (
                    f"This section explores what '{topic}' fundamentally is. "
                    f"We examine its essence, boundaries, and conceptual identity."
                )
            },
            {
                "title": "Underlying Assumptions",
                "content": (
                    f"Here we identify the assumptions, beliefs, or premises that shape "
                    f"how people think about '{topic}'."
                )
            },
            {
                "title": "Perspectives & Interpretations",
                "content": (
                    f"This section presents multiple philosophical viewpoints on '{topic}'. "
                    f"We compare interpretations and highlight their implications."
                )
            },
            {
                "title": "Reasoning Pathways",
                "content": (
                    f"We walk through the logical structures, arguments, or thought processes "
                    f"that help clarify '{topic}'."
                )
            },
            {
                "title": "A Reflective Question",
                "content": (
                    f"A closing question designed to deepen understanding and invite "
                    f"further contemplation of '{topic}'."
                )
            }
        ]

    # ---------------------------------------------------------
    # TONE RULES
    # ---------------------------------------------------------
    def get_tone(self) -> str:
        """
        Philosophical pack uses a reflective, conceptual tone.
        """
        return "philosophical"

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
        Returns a structured philosophical lesson dictionary.
        """
        return {
            "engine_version": "1.0",
            "domain": self.domain_name,
            "tone": self.get_tone(),
            "sections": self.get_sections(topic)
        }
