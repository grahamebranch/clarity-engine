"""
Edition Applier — shapes sections for student/trainer editions.
Upgraded to align with the new LessonGenerator engine.
"""

from typing import List, Dict
from .guidance.guidance_enricher import GuidanceEnricher
from .guidance.guidance_router import GuidanceRouter


class EditionApplier:
    """
    Applies edition-specific transformations to lesson sections.

    IMPORTANT:
    - The upgraded LessonGenerator expects a *single* edition string,
      not a list of editions.
    - This applier now returns a single list of sections, not a dict.
    """

    def __init__(self) -> None:
        self.guidance = GuidanceEnricher()
        self.guidance_router = GuidanceRouter()

    # ---------------------------------------------------------
    # PUBLIC API (aligned with LessonGenerator)
    # ---------------------------------------------------------

    def apply(
        self,
        sections: List[Dict[str, str]],
        edition: str,
        domain: str,
        level: str = "intermediate",
    ) -> List[Dict[str, str]]:
        """
        Returns a single edition-specific version of the sections.
        Domain-aware: guidance is applied only if the router approves.
        """

        if edition == "student_core":
            return self._build_student_core(sections)

        if edition == "student_plus":
            return self._build_student_plus(sections, level, domain)

        if edition == "trainer_lite":
            return self._build_trainer_lite(sections, level, domain)

        if edition == "trainer":
            return self._build_trainer_edition(sections, level, domain)

        # fallback: return unchanged
        return sections

    # ---------------------------------------------------------
    # Edition Builders
    # ---------------------------------------------------------

    def _build_student_core(self, sections: List[Dict[str, str]]) -> List[Dict[str, str]]:
        return sections

    def _build_student_plus(
        self,
        sections: List[Dict[str, str]],
        level: str,
        domain: str,
    ) -> List[Dict[str, str]]:
        enriched = sections

        if self.guidance_router.should_apply(["student_plus"], domain):
            enriched = self.guidance.apply(enriched, level, domain)

        return enriched

    def _build_trainer_lite(
        self,
        sections: List[Dict[str, str]],
        level: str,
        domain: str,
    ) -> List[Dict[str, str]]:
        enriched = sections

        if self.guidance_router.should_apply(["trainer_lite"], domain):
            enriched = self.guidance.apply(enriched, level, domain)

        return enriched

    def _build_trainer_edition(
        self,
        sections: List[Dict[str, str]],
        level: str,
        domain: str,
    ) -> List[Dict[str, str]]:
        enriched = sections

        if self.guidance_router.should_apply(["trainer"], domain):
            enriched = self.guidance.apply(enriched, level, domain)

        trainer_sections = []
        for s in enriched:
            trainer_section = dict(s)
            base = trainer_section.get("content", "")
            trainer_section["content"] = (
                base
                + "\n\n[Trainer Note]\n"
                "- Clarify the aim of this section.\n"
                "- Adjust difficulty based on the learner.\n"
                "- Add extra examples or prompts if needed."
            )
            trainer_sections.append(trainer_section)

        return trainer_sections
