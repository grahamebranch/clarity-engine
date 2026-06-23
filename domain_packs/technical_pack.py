# technical_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Domain Pack: Technical (v1)

from typing import List, Dict

class TechnicalPack:
    """
    Domain Pack: Technical
    Provides precise, structured, engineering‑style explanations.
    Ideal for programming, architecture, systems, and technical concepts.
    """

    def __init__(self):
        self.domain_name = "technical"
        self.version = "1.0"

    # ---------------------------------------------------------
    # SECTION TEMPLATES
    # ---------------------------------------------------------
    def get_sections(self, topic: str) -> List[Dict]:
        """
        Defines the structure of a technical-style lesson.
        Emphasis on clarity, accuracy, and step-by-step explanation.
        """
        return [
            {
                "title": f"Technical Overview: {topic}",
                "content": (
                    f"This section introduces '{topic}' from a technical perspective. "
                    f"We define the concept clearly and outline its purpose and scope."
                )
            },
            {
                "title": "Key Components",
                "content": (
                    f"Here we break '{topic}' into its fundamental parts. "
                    f"Each component is explained with precision and relevance."
                )
            },
            {
                "title": "How It Works",
                "content": (
                    f"This section explains the internal mechanics of '{topic}'. "
                    f"We walk through the logic, flow, or architecture step-by-step."
                )
            },
            {
                "title": "Common Pitfalls",
                "content": (
                    f"We highlight typical mistakes, misunderstandings, or failure modes "
                    f"that occur when working with '{topic}'."
                )
            },
            {
                "title": "Best Practices",
                "content": (
                    f"A concise set of recommendations for using or implementing '{topic}' "
                    f"effectively and reliably."
                )
            }
        ]

    # ---------------------------------------------------------
    # TONE RULES
    # ---------------------------------------------------------
    def get_tone(self) -> str:
        """
        Technical pack uses a precise, structured tone.
        """
        return "technical"

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
        Returns a structured technical lesson dictionary.
        """
        return {
            "engine_version": "1.0",
            "domain": self.domain_name,
            "tone": self.get_tone(),
            "sections": self.get_sections(topic)
        }
