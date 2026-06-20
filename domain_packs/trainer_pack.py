# trainer_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Domain Pack: Trainer (v1)

from typing import List, Dict

class TrainerPack:
    """
    Domain Pack: Trainer
    Provides structured, instructional lessons with clear steps,
    practical exercises, and a confident trainer-style tone.
    """

    def __init__(self):
        self.domain_name = "trainer"
        self.version = "1.0"

    # ---------------------------------------------------------
    # SECTION TEMPLATES
    # ---------------------------------------------------------
    def get_sections(self, topic: str) -> List[Dict]:
        """
        Defines the structure of a trainer-style lesson.
        """
        return [
            {
                "title": f"Understanding {topic}",
                "content": (
                    f"This section gives a clear, structured explanation of '{topic}'. "
                    f"The goal is to ensure you understand the core idea before moving on."
                )
            },
            {
                "title": "Key Principles",
                "content": (
                    f"Here are the essential principles behind '{topic}'. "
                    f"These are the foundations you must understand to apply the concept effectively."
                )
            },
            {
                "title": "Step-by-Step Breakdown",
                "content": (
                    f"This section walks you through '{topic}' in a sequence of simple, "
                    f"actionable steps. Follow them in order for best results."
                )
            },
            {
                "title": "Try It Yourself",
                "content": (
                    f"Here is a practical exercise: Apply '{topic}' to a real or imagined scenario. "
                    f"Write down your steps and reflect on what worked well."
                )
            },
            {
                "title": "Trainer’s Tip",
                "content": (
                    f"A helpful insight: Most people struggle with '{topic}' because they "
                    f"overcomplicate the early steps. Keep it simple and build confidence gradually."
                )
            }
        ]

    # ---------------------------------------------------------
    # TONE RULES
    # ---------------------------------------------------------
    def get_tone(self) -> str:
        """
        Trainer pack uses a confident, structured tone.
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
        Returns a structured lesson dictionary.
        """
        return {
            "engine_version": "1.0",
            "domain": self.domain_name,
            "tone": self.get_tone(),
            "sections": self.get_sections(topic)
        }
