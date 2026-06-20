# business_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Domain Pack: Business (v1)

from typing import List, Dict

class BusinessPack:
    """
    Domain Pack: Business
    Provides structured, analytical, outcome-focused lessons suitable
    for business topics, strategy, operations, leadership, and decision-making.
    """

    def __init__(self):
        self.domain_name = "business"
        self.version = "1.0"

    # ---------------------------------------------------------
    # SECTION TEMPLATES
    # ---------------------------------------------------------
    def get_sections(self, topic: str) -> List[Dict]:
        """
        Defines the structure of a business-style lesson.
        Clear, analytical, and focused on practical outcomes.
        """
        return [
            {
                "title": f"Business Context: {topic}",
                "content": (
                    f"This section explains '{topic}' from a business perspective. "
                    f"We outline the context, relevance, and typical scenarios where it matters."
                )
            },
            {
                "title": "Key Drivers",
                "content": (
                    f"Here we identify the main forces that influence '{topic}'. "
                    f"These may include market trends, customer expectations, operational constraints, "
                    f"or competitive pressures."
                )
            },
            {
                "title": "Strategic Implications",
                "content": (
                    f"This section explores how '{topic}' affects strategy, decision-making, "
                    f"and long-term planning. We highlight risks, opportunities, and trade-offs."
                )
            },
            {
                "title": "Operational Application",
                "content": (
                    f"Here we translate '{topic}' into practical actions. "
                    f"This includes processes, workflows, tools, and measurable outcomes."
                )
            },
            {
                "title": "Executive Summary",
                "content": (
                    f"A concise summary of the most important insights about '{topic}'. "
                    f"Useful for leadership briefings or quick reference."
                )
            }
        ]

    # ---------------------------------------------------------
    # TONE RULES
    # ---------------------------------------------------------
    def get_tone(self) -> str:
        """
        Business pack uses a structured, analytical tone.
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
        Returns a structured lesson dictionary.
        """
        return {
            "engine_version": "1.0",
            "domain": self.domain_name,
            "tone": self.get_tone(),
            "sections": self.get_sections(topic)
        }
