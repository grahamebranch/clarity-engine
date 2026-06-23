# strategic_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Domain Pack: Strategic (v1)

from typing import List, Dict

class StrategicPack:
    """
    Domain Pack: Strategic
    Provides long-term, high-level, leverage-oriented thinking.
    Ideal for planning, positioning, decision-making, and trade-off analysis.
    """

    def __init__(self):
        self.domain_name = "strategic"
        self.version = "1.0"

    # ---------------------------------------------------------
    # SECTION TEMPLATES
    # ---------------------------------------------------------
    def get_sections(self, topic: str) -> List[Dict]:
        """
        Defines the structure of a strategic-style lesson.
        Emphasis on clarity, leverage, and long-term reasoning.
        """
        return [
            {
                "title": f"Strategic Overview: {topic}",
                "content": (
                    f"This section introduces '{topic}' from a strategic perspective. "
                    f"We define the long-term significance and the broader landscape."
                )
            },
            {
                "title": "Forces & Dynamics",
                "content": (
                    f"Here we identify the major forces, incentives, constraints, and "
                    f"environmental dynamics that shape '{topic}'."
                )
            },
            {
                "title": "Leverage Points",
                "content": (
                    f"This section highlights the areas where small, well-placed actions "
                    f"create outsized impact within '{topic}'."
                )
            },
            {
                "title": "Trade-Offs & Choices",
                "content": (
                    f"We examine the key trade-offs involved in '{topic}', helping clarify "
                    f"what must be prioritized, sacrificed, or sequenced."
                )
            },
            {
                "title": "Strategic Recommendations",
                "content": (
                    f"A set of high-level recommendations for navigating '{topic}' "
                    f"with clarity, leverage, and long-term alignment."
                )
            }
        ]

    # ---------------------------------------------------------
    # TONE RULES
    # ---------------------------------------------------------
    def get_tone(self) -> str:
        """
        Strategic pack uses a high-level, analytical tone.
        """
        return "strategic"

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
        Returns a structured strategic lesson dictionary.
        """
        return {
            "engine_version": "1.0",
            "domain": self.domain_name,
            "tone": self.get_tone(),
            "sections": self.get_sections(topic)
        }
