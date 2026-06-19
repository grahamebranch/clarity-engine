"""
output_formatting — final assembly of the engine output.
"""

from typing import Dict, Any


def format_output(lesson: Dict[str, Any],
                  routing: Dict[str, Any],
                  clarity: Dict[str, Any]) -> Dict[str, Any]:
    """
    Combines all pipeline components into a single final output object.
    """

    return {
        "topic": routing.get("topic"),
        "level": routing.get("level"),
        "domain": routing.get("domain"),

        "lesson": lesson,
        "clarity": clarity,

        "summary": {
            "sections": len(lesson.get("sections", [])),
            "clarity_score": clarity.get("score"),
        }
    }
