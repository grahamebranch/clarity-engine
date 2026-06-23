# analytical_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Domain Pack: Analytical (v1)

from typing import List, Dict

class AnalyticalPack:
    """
    Domain Pack: Analytical
    Provides structured, evidence-based, logic-driven analysis.
    Ideal for comparisons, evaluations, reasoning, and data-oriented clarity.
    """

    def __init__(self):
        self.domain_name = "analytical"
        self.version = "1.0"

    # ---------------------------------------------------------
    # SECTION TEMPLATES
    # ---------------------------------------------------------
    def get_sections(self, topic: str) -> List[Dict]:
        """
        Defines the structure of an analytical-style lesson.
        Emphasis on logic, structure, and evidence-based reasoning.
        """
        return [
            {
                "title": f"Analytical Overview: {topic}",
                "content": (
                    f"This section introduces '{topic}' through a structured analytical lens. "
                    f"We define the problem space and outline the key variables involved."
                )
            },
            {
                "title": "Key Factors & Variables",
                "content": (
                    f"Here we identify the major factors that influence '{topic}'. "
                    f"Each variable is explained clearly and logically."
                )
            },
            {
                "title": "Comparative Analysis",
                "content": (
                    f"This section compares different approaches, interpretations, or outcomes "
                    f"related to '{topic}', highlighting strengths and weaknesses."
                )
            },
            {
                "title": "Logical Evaluation",
                "content": (
                    f"We walk through the reasoning steps that lead to a clear understanding "
                    f"of '{topic}'. The goal is to make the logic explicit and traceable."
                )
            },
            {
                "title": "Conclusion & Insights",
                "content": (
                    f"A concise summary of the analytical findings, including the most "
                    f"important insights and implications related to '{topic}'."
                )
            }
        ]

    # ---------------------------------------------------------
    # TONE RULES
    # ---------------------------------------------------------
    def get_tone(self) -> str:
        """
        Analytical pack uses a structured, logical tone.
        """
        return "analytical"

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
        Returns a structured analytical lesson dictionary.
        """
        return {
            "engine_version": "1.0",
            "domain": self.domain_name,
            "tone": self.get_tone(),
            "sections": self.get_sections(topic)
        }
