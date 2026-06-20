"""
LessonGenerator — upgraded engine that produces a full structured lesson
with:
- deterministic architecture
- real section content
- edition logic (integrated)
- pack logic
- structured LessonObject
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
from datetime import datetime
import uuid

from .lesson_sections import LessonSectionsBuilder
from .lesson_architecture import LessonArchitectureBuilder
from .edition_applier import EditionApplier
from .vocab_enricher import VocabularyEnricher
from .grammar_enricher import GrammarEnricher
from .error_enricher import ErrorEnricher
from .cultural_enricher import CulturalEnricher
from .guidance.guidance_enricher import GuidanceEnricher


# ---------------------------------------------------------
# DATA MODELS
# ---------------------------------------------------------

@dataclass
class LessonSection:
    key: str
    title: str
    content: str
    order: int


@dataclass
class LessonAnnex:
    key: str
    title: str
    content: str
    annex_type: str
    order: int


@dataclass
class LessonMetadata:
    id: str
    topic: str
    level: str
    domain: str
    edition: str
    packs: List[str]
    created_at: datetime
    updated_at: datetime
    version: str = "1.0.0"


@dataclass
class LessonObject:
    metadata: LessonMetadata
    sections: List[LessonSection] = field(default_factory=list)
    annexes: List[LessonAnnex] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "metadata": {
                "id": self.metadata.id,
                "topic": self.metadata.topic,
                "level": self.metadata.level,
                "domain": self.metadata.domain,
                "edition": self.metadata.edition,
                "packs": self.metadata.packs,
                "created_at": self.metadata.created_at.isoformat(),
                "updated_at": self.metadata.updated_at.isoformat(),
                "version": self.metadata.version,
            },
            "sections": [
                {
                    "key": s.key,
                    "title": s.title,
                    "content": s.content,
                    "order": s.order,
                }
                for s in self.sections
            ],
            "annexes": [
                {
                    "key": a.key,
                    "title": a.title,
                    "content": a.content,
                    "annex_type": a.annex_type,
                    "order": a.order,
                }
                for a in self.annexes
            ],
        }


# ---------------------------------------------------------
# MAIN ENGINE
# ---------------------------------------------------------

class LessonGenerator:
    """
    Upgraded lesson engine:
    - builds architecture
    - generates section content
    - applies edition rules
    - applies pack enrichers
    - returns a structured LessonObject
    """

    def __init__(
        self,
        llm_client: Optional[Any] = None,
        storage_client: Optional[Any] = None,
    ):
        self.llm_client = llm_client
        self.storage_client = storage_client

        self.arch_builder = LessonArchitectureBuilder()
        self.sections_builder = LessonSectionsBuilder()
        self.edition_applier = EditionApplier()

        # enrichers
        self.vocab = VocabularyEnricher()
        self.grammar = GrammarEnricher()
        self.errors = ErrorEnricher()
        self.culture = CulturalEnricher()
        self.guidance = GuidanceEnricher()

    # -----------------------------------------------------
    # PUBLIC API
    # -----------------------------------------------------

    def generate_lesson(
        self,
        topic: str,
        level: str,
        domain: str,
        edition: str = "trainer",
        packs: Optional[List[str]] = None,
    ) -> Dict[str, Any]:

        packs = packs or []

        # 1. architecture
        architecture = self.arch_builder.build(topic, level, domain)

        # 2. concrete sections
        raw_sections = self.sections_builder.build_sections(
            architecture=architecture,
            topic=topic,
        )

        # 3. edition rules
        edition_sections = self.edition_applier.apply(
            sections=raw_sections,
            edition=edition,
            domain=domain,
        )

        # 4. pack enrichers
        annexes = self._build_annexes(topic, level, domain, packs)

        # 5. build structured object
        lesson = self._build_lesson_object(
            topic=topic,
            level=level,
            domain=domain,
            edition=edition,
            packs=packs,
            sections=edition_sections,
            annexes=annexes,
        )

        # 6. optional save
        if self.storage_client:
            self.storage_client.save_lesson(lesson.metadata.id, lesson.to_dict())

        return lesson.to_dict()

    # -----------------------------------------------------
    # INTERNAL HELPERS
    # -----------------------------------------------------

    def _build_annexes(
        self,
        topic: str,
        level: str,
        domain: str,
        packs: List[str],
    ) -> List[LessonAnnex]:

        annexes = []

        if "vocab" in packs:
            annexes.append(
                LessonAnnex(
                    key="vocab_pack",
                    title="Vocabulary Expansion",
                    content=self.vocab.enrich(topic, level, domain),
                    annex_type="vocab",
                    order=len(annexes),
                )
            )

        if "grammar" in packs:
            annexes.append(
                LessonAnnex(
                    key="grammar_pack",
                    title="Grammar Focus",
                    content=self.grammar.enrich(topic, level, domain),
                    annex_type="grammar",
                    order=len(annexes),
                )
            )

        if "errors" in packs:
            annexes.append(
                LessonAnnex(
                    key="error_pack",
                    title="Common Errors",
                    content=self.errors.enrich(topic, level, domain),
                    annex_type="errors",
                    order=len(annexes),
                )
            )

        if "culture" in packs:
            annexes.append(
                LessonAnnex(
                    key="culture_pack",
                    title="Cultural Notes",
                    content=self.culture.enrich(topic, level, domain),
                    annex_type="culture",
                    order=len(annexes),
                )
            )

        if "guidance" in packs:
            annexes.append(
                LessonAnnex(
                    key="guidance_pack",
                    title="Guidance Notes",
                    content=self.guidance.enrich(topic, level, domain),
                    annex_type="guidance",
                    order=len(annexes),
                )
            )

        return annexes

    def _build_lesson_object(
        self,
        topic: str,
        level: str,
        domain: str,
        edition: str,
        packs: List[str],
        sections: List[Dict[str, Any]],
        annexes: List[LessonAnnex],
    ) -> LessonObject:

        now = datetime.utcnow()

        metadata = LessonMetadata(
            id=str(uuid.uuid4()),
            topic=topic,
            level=level,
            domain=domain,
            edition=edition,
            packs=packs,
            created_at=now,
            updated_at=now,
        )

        section_objs = [
            LessonSection(
                key=s["id"],
                title=s["title"],
                content=s["content"],
                order=i,
            )
            for i, s in enumerate(sections)
        ]

        return LessonObject(
            metadata=metadata,
            sections=section_objs,
            annexes=annexes,
        )
