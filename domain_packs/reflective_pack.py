# reflective_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Domain Pack: Reflective (v1)

from typing import List, Dict

class ReflectivePack:
    """
    Domain Pack: Reflective
    Provides introspective, thoughtful, self-awareness-oriented content.
    Ideal for personal insight, meaning-making, and reflective processing.
    """

    def __init__(self):
        self.domain_name = "reflective"
        self.version = "1.0"

    # ---------------------------------------------------------
    # SECTION TEMPLATES
    # ---------------------------------------------------------
    def get_sections(self, topic: str) -> List[Dict]:
        """
        Defines the structure of a reflective-style lesson.
        Emphasis on introspection, meaning, and personal insight.
        """
        return [
            {
                "title": f"Reflective Introduction: {topic}",
                "content": (
                    f"This section gently introduces '{topic}' in a reflective way. "
                    f"It invites you to slow down and consider your personal relationship to it."
                )
            },
            {
                "title": "Inner Landscape",
                "content": (
                    f"Here we explore the internal thoughts, patterns, or experiences "
                    f"that may shape how you relate to '{topic}'."
                )
            },
            {
                "title": "Meaning & Interpretation",
                "content": (
                    f"This section examines what '{topic}' might represent in a deeper sense—"
                    f"its significance, symbolism, or personal meaning."
                )
            },
            {
                "title": "Self‑Inquiry Prompts",
                "content": (
                    f"A set of thoughtful questions designed to help you explore '{topic}' "
                    f"more deeply and with greater clarity."
                )
            },
            {
                "title": "Closing Reflection",
                "content": (
                    f"A final moment of reflection to integrate your insights about '{topic}' "
                    f"and consider how they might guide you going forward."
                )
            }
        ]

    # ---------------------------------------------------------
    # TONE RULES
    # ---------------------------------------------------------
    def get_tone(self) -> str:
        """
        Reflective pack uses a calm, introspective tone.
        """
        return "reflective"

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
        Returns a structured reflective lesson dictionary.
        """
        return {
            "engine_version": "1.0",
            "domain": self.domain_name,
            "tone": self.get_tone(),
            "sections": self.get_sections(topic)
        }
