# creative_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Domain Pack: Creative (v1)

from typing import List, Dict

class CreativePack:
    """
    Domain Pack: Creative
    Produces expressive, imaginative, high‑energy content.
    Ideal for brainstorming, storytelling, ideation, and creative exploration.
    """

    def __init__(self):
        self.domain_name = "creative"
        self.version = "1.0"

    # ---------------------------------------------------------
    # SECTION TEMPLATES
    # ---------------------------------------------------------
    def get_sections(self, topic: str) -> List[Dict]:
        """
        Defines the structure of a creative-style lesson.
        Emphasis on imagination, exploration, and expressive thinking.
        """
        return [
            {
                "title": f"Creative Spark: {topic}",
                "content": (
                    f"This section introduces '{topic}' with energy and imagination. "
                    f"The goal is to spark curiosity and open creative pathways."
                )
            },
            {
                "title": "Idea Exploration",
                "content": (
                    f"Here we explore multiple angles, interpretations, and possibilities "
                    f"related to '{topic}'. No limits, no constraints — just ideas."
                )
            },
            {
                "title": "Story or Scenario",
                "content": (
                    f"This section presents a short, vivid story or scenario inspired by '{topic}'. "
                    f"It helps bring abstract ideas to life through narrative."
                )
            },
            {
                "title": "Creative Techniques",
                "content": (
                    f"We outline practical creative techniques you can use to expand on '{topic}'. "
                    f"These may include prompts, reframing, metaphor, or visual thinking."
                )
            },
            {
                "title": "Inspiration Boost",
                "content": (
                    f"A final burst of inspiration: a thought, image, or challenge designed "
                    f"to push your creativity further with '{topic}'."
                )
            }
        ]

    # ---------------------------------------------------------
    # TONE RULES
    # ---------------------------------------------------------
    def get_tone(self) -> str:
        """
        Creative pack uses an expressive, imaginative tone.
        """
        return "creative"

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
        Returns a structured creative lesson dictionary.
        """
        return {
            "engine_version": "1.0",
            "domain": self.domain_name,
            "tone": self.get_tone(),
            "sections": self.get_sections(topic)
        }
