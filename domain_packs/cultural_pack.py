# cultural_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Domain Pack: Cultural (v1)

from typing import List, Dict

class CulturalPack:
    """
    Domain Pack: Cultural
    Provides culturally aware, globally sensitive explanations.
    Ideal for topics involving norms, values, communication styles,
    and cross-cultural interpretation.
    """

    def __init__(self):
        self.domain_name = "cultural"
        self.version = "1.0"

    # ---------------------------------------------------------
    # SECTION TEMPLATES
    # ---------------------------------------------------------
    def get_sections(self, topic: str) -> List[Dict]:
        """
        Defines the structure of a cultural-style lesson.
        Emphasis on context, nuance, and global awareness.
        """
        return [
            {
                "title": f"Cultural Context: {topic}",
                "content": (
                    f"This section introduces '{topic}' through a cultural lens. "
                    f"We outline how different societies may view or interpret it."
                )
            },
            {
                "title": "Norms & Values",
                "content": (
                    f"Here we explore the norms, values, and expectations that shape "
                    f"how '{topic}' is understood across cultures."
                )
            },
            {
                "title": "Communication Styles",
                "content": (
                    f"This section examines how people from different cultural backgrounds "
                    f"might discuss or express ideas related to '{topic}'."
                )
            },
            {
                "title": "Potential Misunderstandings",
                "content": (
                    f"We highlight common cross-cultural misunderstandings involving '{topic}', "
                    f"and how to navigate them respectfully."
                )
            },
            {
                "title": "Bridging Perspectives",
                "content": (
                    f"A set of practical suggestions for connecting viewpoints and fostering "
                    f"mutual understanding around '{topic}'."
                )
            }
        ]

    # ---------------------------------------------------------
    # TONE RULES
    # ---------------------------------------------------------
    def get_tone(self) -> str:
        """
        Cultural pack uses a respectful, globally aware tone.
        """
        return "cultural"

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
        Returns a structured cultural lesson dictionary.
        """
        return {
            "engine_version": "1.0",
            "domain": self.domain_name,
            "tone": self.get_tone(),
            "sections": self.get_sections(topic)
        }
