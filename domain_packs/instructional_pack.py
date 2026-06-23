# instructional_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Domain Pack: Instructional (v1)

from typing import List, Dict

class InstructionalPack:
    """
    Domain Pack: Instructional
    Provides clear, structured, step-by-step teaching content.
    Ideal for explanations, tutorials, walkthroughs, and guided learning.
    """

    def __init__(self):
        self.domain_name = "instructional"
        self.version = "1.0"

    # ---------------------------------------------------------
    # SECTION TEMPLATES
    # ---------------------------------------------------------
    def get_sections(self, topic: str) -> List[Dict]:
        """
        Defines the structure of an instructional-style lesson.
        Emphasis on clarity, sequencing, and practical understanding.
        """
        return [
            {
                "title": f"Introduction to {topic}",
                "content": (
                    f"This section introduces '{topic}' in a clear, accessible way. "
                    f"We outline what it is and why it matters."
                )
            },
            {
                "title": "Core Concepts",
                "content": (
                    f"Here we break '{topic}' into its essential ideas. "
                    f"Each concept is explained simply and directly."
                )
            },
            {
                "title": "Step-by-Step Guide",
                "content": (
                    f"A practical walkthrough showing how to apply or understand '{topic}' "
                    f"in a clear sequence of steps."
                )
            },
            {
                "title": "Examples",
                "content": (
                    f"This section provides concrete examples that demonstrate how '{topic}' "
                    f"works in real situations."
                )
            },
            {
                "title": "Practice & Application",
                "content": (
                    f"Simple exercises or prompts to help reinforce your understanding of '{topic}'."
                )
            }
        ]

    # ---------------------------------------------------------
    # TONE RULES
    # ---------------------------------------------------------
    def get_tone(self) -> str:
        """
        Instructional pack uses a clear, structured teaching tone.
        """
        return "instructional"

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
        Returns a structured instructional lesson dictionary.
        """
        return {
            "engine_version": "1.0",
            "domain": self.domain_name,
            "tone": self.get_tone(),
            "sections": self.get_sections(topic)
        }
