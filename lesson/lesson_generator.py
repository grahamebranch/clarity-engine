"""
Lesson Generator — orchestrates lesson routing, topic extraction, architecture,
sections, level scaling, vocabulary enrichment, grammar enrichment,
cultural enrichment, error pattern enrichment, and editions.
"""

from typing import Dict, Any

from .lesson_router import LessonRouter
from .lesson_architecture import LessonArchitecture
from .lesson_sections import LessonSectionsBuilder
from .topic_extractor import TopicExtractor
from .edition_router import EditionRouter
from .edition_applier import EditionApplier
from .level_router import LevelRouter
from .level_applier import LevelApplier
from .vocab_enricher import VocabularyEnricher
from .grammar_enricher import GrammarEnricher
from .cultural_enricher import CulturalEnricher
from .error_enricher import ErrorEnricher


class LessonGenerator:
    def __init__(self) -> None:
        self.router = LessonRouter()
        self.arch = LessonArchitecture()
        self.sections_builder = LessonSectionsBuilder()
        self.topic_extractor = TopicExtractor()
        self.edition_router = EditionRouter()
        self.edition_applier = EditionApplier()
        self.level_router = LevelRouter()
        self.level_applier = LevelApplier()
        self.vocab_enricher = VocabularyEnricher()
        self.grammar_enricher = GrammarEnricher()
        self.cultural_enricher = CulturalEnricher()
        self.error_enricher = ErrorEnricher()

    def run(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Full lesson generation pipeline.
        """

        text = data.get("text", "")
        mode = data.get("mode", "raw")

        if mode != "lesson":
            return data

        # 1) Lesson type
        lesson_type = self.router.route(text)

        # 2) Topic
        topic = self.topic_extractor.extract(text)

        # 3) Architecture
        architecture = self.arch.get_architecture(lesson_type)

        # 4) Base sections
        base_sections = self.sections_builder.build_sections(architecture, topic)

        # 5) Level
        level = self.level_router.route(text)

        # 6) Level shaping
        leveled_sections = self.level_applier.apply(base_sections, level)

        # 7) Vocabulary enrichment
        vocab_sections = self.vocab_enricher.apply(leveled_sections, level, topic)

        # 8) Grammar enrichment
        grammar_sections = self.grammar_enricher.apply(vocab_sections, level, topic)

        # 9) Cultural enrichment
        cultural_sections = self.cultural_enricher.apply(grammar_sections, level, topic)

        # 10) Error pattern enrichment
        error_sections = self.error_enricher.apply(cultural_sections, level, topic)

        # 11) Editions
        editions = self.edition_router.route(text)

        # ⭐ Updated: EditionApplier now receives domain="lesson"
        edition_sections = self.edition_applier.apply(
            error_sections,
            editions,
            level,
            domain="lesson",
        )

        # 12) Primary edition
        if "student" in edition_sections:
            primary_sections = edition_sections["student"]
        elif "trainer" in edition_sections:
            primary_sections = edition_sections["trainer"]
        else:
            primary_sections = error_sections

        # 13) Write into data
        data["lesson_type"] = lesson_type
        data["topic"] = topic
        data["level"] = level
        data["editions"] = editions
        data["sections"] = primary_sections
        data["edition_sections"] = edition_sections

        # 14) Trace snapshot
        data["lesson_trace"] = {
            "lesson_type": lesson_type,
            "topic": topic,
            "level": level,
            "editions": editions,
            "section_ids": [s["id"] for s in primary_sections],
            "section_titles": [s["title"] for s in primary_sections]
        }

        # 15) Combined text
        data["text"] = self._combine_sections_to_text(primary_sections)

        return data

    def _combine_sections_to_text(self, sections):
        parts = []
        for s in sections:
            parts.append(f"# {s['title']}\n\n{s['content']}")
        return "\n\n".join(parts)
