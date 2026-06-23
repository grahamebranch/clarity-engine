"""
LessonRouter — entry point for lesson generation.
Delegates to LessonOrchestrator.
"""

from typing import Dict, Any, List, Optional

from .lesson_generator import LessonGenerator
from .lesson_orchestrator import LessonOrchestrator


class LessonRouter:
    """
    Thin routing layer that:
    - receives lesson generation requests
    - forwards them to LessonOrchestrator
    - returns a structured lesson object
    """

    def __init__(
        self,
        llm_client: Optional[Any] = None,
        storage_client: Optional[Any] = None,
    ):
        self.generator = LessonGenerator(
            llm_client=llm_client,
            storage_client=storage_client,
        )
        self.orchestrator = LessonOrchestrator(self.generator)

    def generate(
        self,
        topic: str,
        level: str,
        domain: str,
        edition: str = "trainer",
        packs: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """
        Public entry point for lesson generation.
        Returns a structured lesson object.
        """

        return self.orchestrator.orchestrate(
            topic=topic,
            level=level,
            domain=domain,
            edition=edition,
        )
