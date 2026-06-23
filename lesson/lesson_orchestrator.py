# lesson_orchestrator.py — FastPath Whole-File Replacement
# Clarity Companion — Lesson Orchestrator (v1)

from typing import Any, Dict, Optional

from .lesson_composer import LessonComposer
from ..edition_engine.edition_engine import EditionEngine

# Packs (you will expand this list as your library grows)
from ..domain_packs.conversation_pack import ConversationDomainPack
from ..structure_packs.basic_structure import BasicStructurePack
from ..template_packs.standard_template import StandardTemplatePack
from ..flow_packs.linear_flow import LinearFlowPack


class LessonOrchestrator:
    """
    Lesson Orchestrator
    Selects the correct packs based on topic/level/domain/edition.
    Instantiates the composer and returns a fully assembled lesson.
    """

    def __init__(self, generator):
        self.generator = generator
        self.edition_engine = EditionEngine()
        self.composer = LessonComposer(self.edition_engine)

    # ---------------------------------------------------------
    # PACK SELECTION
    # ---------------------------------------------------------
    def select_domain_pack(self, domain: str):
        # Expand this as you add more domain packs
        return ConversationDomainPack(self.generator)

    def select_structure_pack(self, level: str):
        # Expand this as you add more structure packs
        return BasicStructurePack()

    def select_template_pack(self, level: str):
        # Expand this as you add more template packs
        return StandardTemplatePack()

    def select_flow_pack(self):
        # Expand this as you add more flow packs
        return LinearFlowPack()

    # ---------------------------------------------------------
    # MAIN ENTRY POINT
    # ---------------------------------------------------------
    def orchestrate(
        self,
        topic: str,
        level: str,
        domain: str,
        edition: str,
    ) -> Dict[str, Any]:
        """
        Selects packs, composes the lesson, and returns the final result.
        """

        domain_pack = self.select_domain_pack(domain)
        structure_pack = self.select_structure_pack(level)
        template_pack = self.select_template_pack(level)
        flow_pack = self.select_flow_pack()

        return self.composer.compose(
            topic=topic,
            domain_pack=domain_pack,
            structure_pack=structure_pack,
            template_pack=template_pack,
            flow_pack=flow_pack,
            edition=edition,
        )
