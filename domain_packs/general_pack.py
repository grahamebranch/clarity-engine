# general_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Domain Pack: General (v1)

from typing import List, Dict

class GeneralPack:
    """
    Domain Pack: General
    Provides balanced, neutral‑tone lessons suitable for broad topics.
    This is the “default” domain: clear, structured, and universally applicable.
    """

    def __init__(self):
        self.domain_name = "general"
        self.version = "1.0"

    # ---------------------------------------------------------
    # SECTION TEMPLATES
    # ---------------------------------------------------------
    def get_sections(self, topic: str) -> List[Dict]:
        """
        Defines the structure of a general-purpose lesson.
        Balanced tone, clear explanations, practical examples.
        """
        return [
            {
                "title": f"Overview of {topic}",
                "content": (
                    f"This section provides a clear, neutral introduction to '{topic}'. "
                    f"It explains what it is, why it matters, and where it typically appears."
                )
            },
            {
                "title": "Core Concepts",
                "content": (
                    f"Here we outline the essential ideas behind '{topic}'. "
                    f"These concepts form the foundation for deeper understanding."
                )
            },
            {
                "title": "How It Works",
                "content": (
                    f"This section explains the mechanics of '{topic}' in a simple, "
                    f"step-by-step way. The goal is clarity without oversimplification."
                )
            },
            {
                "title": "Real‑World Example",
                "content": (
                    f"To make '{topic}' concrete, we walk through a realistic example. "
                    f"This helps connect theory to practice."
                )
            },
            {
                "title": "Key Takeaways",
                "content": (
                    f"A concise summary of the most important points about '{topic}'. "
                    f"Useful for quick revision or reinforcement."
                )
            }
        ]

    # ---------------------------------------------------------
    # TONE RULES
    # ---------------------------------------------------------
    def get_tone(self) -> str:
        """
        General pack uses a neutral, balanced tone.
        """
        return "neutral"

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
        Returns a structured lesson dictionary.
        """
        return {
            "engine_version": "1.0",
            "domain": self.domain_name,
            "tone": self.get_tone(),
            "sections": self.get_sections(topic)
        }
