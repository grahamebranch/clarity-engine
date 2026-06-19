"""
LessonGenerator — builds the full lesson object from topic, level, and domain.
"""

from typing import Dict, Any, List
from .lesson_sections import LessonSectionsBuilder


class LessonGenerator:
    """
    Generates a complete lesson:
    - architecture (section list)
    - concrete section content
    """

    def __init__(self):
        self.sections_builder = LessonSectionsBuilder()

    # ------------------------------------------------------------------
    # MAIN ENTRY POINT (required by SimpleEngine)
    # ------------------------------------------------------------------
    def generate_lesson(self, topic: str, level: str, domain: str) -> Dict[str, Any]:
        """
        Returns a full lesson object:
        {
            "topic": ...,
            "level": ...,
            "domain": ...,
            "sections": [...]
        }
        """

        architecture = self._build_architecture(topic, level, domain)

        sections = self.sections_builder.build_sections(
            architecture=architecture,
            topic=topic
        )

        return {
            "topic": topic,
            "level": level,
            "domain": domain,
            "sections": sections,
        }

    # ------------------------------------------------------------------
    # INTERNAL: deterministic architecture
    # ------------------------------------------------------------------
    def _build_architecture(self, topic: str, level: str, domain: str) -> List[Dict[str, str]]:
        """
        Returns a deterministic list of section specs.
        """

        return [
            {"id": "warmup", "title": "Warm‑Up Discussion"},
            {"id": "dialogue", "title": "Model Dialogue"},
            {"id": "questions", "title": "Discussion Questions"},
            {"id": "vocab", "title": "Useful Vocabulary"},
            {"id": "practice", "title": "Practice Activities"},
            {"id": "reflection", "title": "Reflection"},
        ]
