"""
Engine Init — exposes engine-level subsystems for external import.
"""

# Lesson routing and architecture
from .lesson_router import LessonRouter
from .lesson_architecture import LessonArchitecture
from .lesson_sections import LessonSectionsBuilder

# Level logic
from .level_router import LevelRouter
from .level_applier import LevelApplier

# Edition logic
from .edition_router import EditionRouter
from .edition_applier import EditionApplier

# Topic extraction
from .topic_extractor import TopicExtractor

# Enrichment layers
from .vocab_enricher import VocabularyEnricher
from .grammar_enricher import GrammarEnricher
from .cultural_enricher import CulturalEnricher
from .error_enricher import ErrorEnricher

# Guidance subsystem
from ...lesson.guidance.guidance_profile import GuidanceProfile
from ...lesson.guidance.guidance_enricher import GuidanceEnricher
from ...lesson.guidance.guidance_router import GuidanceRouter

__all__ = [
    "LessonRouter",
    "LessonArchitecture",
    "LessonSectionsBuilder",
    "LevelRouter",
    "LevelApplier",
    "EditionRouter",
    "EditionApplier",
    "TopicExtractor",
    "VocabularyEnricher",
    "GrammarEnricher",
    "CulturalEnricher",
    "ErrorEnricher",
    "GuidanceProfile",
    "GuidanceEnricher",
    "GuidanceRouter",
]
