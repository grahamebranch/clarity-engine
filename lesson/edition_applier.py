"""
Edition Applier — shapes sections for student/trainer editions.
"""

from typing import List, Dict
from .guidance.guidance_enricher import GuidanceEnricher
from .guidance.guidance_router import GuidanceRouter


class EditionApplier:
    def __init__(self) -> None:
        self.guidance = GuidanceEnricher()
        self.guidance_router = GuidanceRouter()

    def apply(
        self,
        sections: List[Dict[str, str]],
        editions: List[str],
        level: str,
        domain: str = "lesson",
    ) -> Dict[str, List[Dict[str, str]]]:
        """
        Returns edition-specific versions of the sections.
        Domain-aware: guidance is applied only if the router approves for (editions, domain).
        """

        result: Dict[str, List[Dict[str, str]]] = {}

        # --- Student Core (no guidance) ---
        if "student_core" in editions:
            result["student_core"] = self._build_student_core(sections)

        # --- Student Plus ---
        if "student_plus" in editions:
            result["student_plus"] = self._build_student_plus(sections, level, domain)

        # --- Trainer Lite ---
        if "trainer_lite" in editions:
            result["trainer_lite"] = self._build_trainer_lite(sections, level, domain)

        # --- Full Trainer Edition ---
        if "trainer" in editions:
            result["trainer"] = self._build_trainer_edition(sections, level, domain)

        return result

    # -------------------------------------------------------------------------
    # Edition Builders
    # -------------------------------------------------------------------------

    def _build_student_core(self, sections: List[Dict[str, str]]) -> List[Dict[str, str]]:
        return sections

    def _build_student_plus(
        self,
        sections: List[Dict[str, str]],
        level: str,
        domain: str,
    ) -> List[Dict[str, str]]:
        enriched = sections

        # Domain-aware guidance
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

        # Domain-aware guidance
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

        # Domain-aware guidance
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
