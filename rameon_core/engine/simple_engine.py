"""
SimpleEngine — orchestrates the full lesson generation pipeline.
"""

from typing import Dict, Any

from routing.domain_router import DomainRouter
from lesson.lesson_generator import LessonGenerator
from .clarity_scorer import ClarityScorer
from .output_formatting import format_output


class SimpleEngine:
    """
    The high-level orchestrator for generating a complete lesson.
    """

    def __init__(self):
        self.domain_router = DomainRouter()
        self.lesson_generator = LessonGenerator()
        self.clarity_scorer = ClarityScorer()

    # ------------------------------------------------------------------
    # MAIN ENTRY POINT
    # ------------------------------------------------------------------

    def generate(self, user_request: str) -> Dict[str, Any]:
        """
        Full pipeline:
        1. Route domain
        2. Generate lesson architecture + content
        3. Score clarity
        4. Format final output
        """

        # 1. Domain routing
        routing_result = self.domain_router.route(user_request)

        # 2. Lesson generation
        lesson_result = self.lesson_generator.generate_lesson(
            topic=routing_result["topic"],
            level=routing_result["level"],
            domain=routing_result["domain"],
        )

        # 3. Clarity scoring
        clarity_score = self.clarity_scorer.score(lesson_result)

        # 4. Final formatting
        final_output = format_output(
            lesson=lesson_result,
            routing=routing_result,
            clarity=clarity_score,
        )

        return final_output

    # ------------------------------------------------------------------
    # Compatibility wrapper
    # ------------------------------------------------------------------
    def run(self, user_request: str):
        return self.generate(user_request)
