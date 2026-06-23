# narrative_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Domain Pack: Narrative (v1)

from typing import List, Dict

class NarrativePack:
    """
    Domain Pack: Narrative
    Provides story-driven, scene-based, character-oriented content.
    Ideal for storytelling, narrative framing, and turning ideas into stories.
    """

    def __init__(self):
        self.domain_name = "narrative"
        self.version = "1.0"

    # ---------------------------------------------------------
    # SECTION TEMPLATES
    # ---------------------------------------------------------
    def get_sections(self, topic: str) -> List[Dict]:
        """
        Defines the structure of a narrative-style lesson.
        Emphasis on story, characters, scenes, and emotional movement.
        """
        return [
            {
                "title": f"Story Setup: {topic}",
                "content": (
                    f"This section introduces '{topic}' as the seed of a story. "
                    f"We establish the setting, tone, and initial tension."
                )
            },
            {
                "title": "Characters & Motivations",
                "content": (
                    f"Here we identify the key characters connected to '{topic}', "
                    f"their motivations, and what drives them forward."
                )
            },
            {
                "title": "Rising Action",
                "content": (
                    f"This section explores how the tension around '{topic}' builds. "
                    f"We highlight challenges, turning points, and emotional stakes."
                )
            },
            {
                "title": "Climax or Insight",
                "content": (
                    f"The pivotal moment where the meaning of '{topic}' becomes clear. "
                    f"A breakthrough, confrontation, or moment of truth."
                )
            },
            {
                "title": "Resolution",
                "content": (
                    f"A closing scene that ties the narrative threads together and "
                    f"reveals what has changed because of '{topic}'."
                )
            }
        ]

    # ---------------------------------------------------------
    # TONE RULES
    # ---------------------------------------------------------
    def get_tone(self) -> str:
        """
        Narrative pack uses a vivid, story-driven tone.
        """
        return "narrative"

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
        Returns a structured narrative lesson dictionary.
        """
        return {
            "engine_version": "1.0",
            "domain": self.domain_name,
            "tone": self.get_tone(),
            "sections": self.get_sections(topic)
        }
