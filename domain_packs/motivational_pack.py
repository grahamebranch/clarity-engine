# motivational_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Domain Pack: Motivational (v1)

from typing import List, Dict

class MotivationalPack:
    """
    Domain Pack: Motivational
    Provides energising, confidence-building, forward-moving content.
    Ideal for encouragement, momentum, and positive framing.
    """

    def __init__(self):
        self.domain_name = "motivational"
        self.version = "1.0"

    # ---------------------------------------------------------
    # SECTION TEMPLATES
    # ---------------------------------------------------------
    def get_sections(self, topic: str) -> List[Dict]:
        """
        Defines the structure of a motivational-style lesson.
        Emphasis on energy, confidence, and forward momentum.
        """
        return [
            {
                "title": f"Why {topic} Matters",
                "content": (
                    f"This section highlights the importance and potential of '{topic}'. "
                    f"It sets a positive, energising frame for what comes next."
                )
            },
            {
                "title": "Your Strengths",
                "content": (
                    f"We identify the strengths, qualities, and capabilities you already "
                    f"bring to '{topic}', reinforcing confidence and momentum."
                )
            },
            {
                "title": "Overcoming Barriers",
                "content": (
                    f"This section acknowledges the challenges around '{topic}' and offers "
                    f"encouraging, practical ways to move through them."
                )
            },
            {
                "title": "Momentum Boost",
                "content": (
                    f"A burst of motivation designed to help you take the next step with "
                    f"energy, clarity, and belief in your ability to succeed with '{topic}'."
                )
            },
            {
                "title": "Forward Action",
                "content": (
                    f"A simple, empowering action you can take right now to build progress "
                    f"and reinforce your momentum around '{topic}'."
                )
            }
        ]

    # ---------------------------------------------------------
    # TONE RULES
    # ---------------------------------------------------------
    def get_tone(self) -> str:
        """
        Motivational pack uses an energising, encouraging tone.
        """
        return "motivational"

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
        Returns a structured motivational lesson dictionary.
        """
        return {
            "engine_version": "1.0",
            "domain": self.domain_name,
            "tone": self.get_tone(),
            "sections": self.get_sections(topic)
        }
