# concise_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Concise Edition Pack (v1)

from typing import Dict

class ConciseEditionPack:
    """
    Concise Edition Pack
    Provides topic-aware summarization logic for the 'concise' edition.
    This is layered on top of the Edition Engine's generic concise transform.
    """

    def __init__(self):
        self.version = "1.0"

    # ---------------------------------------------------------
    # SUMMARY LOGIC
    # ---------------------------------------------------------
    def summarize(self, topic: str, sections: Dict[str, str]) -> str:
        """
        Produces a topic-aware concise summary of the lesson.
        """
        summary_lines = [f"## Concise Summary of {topic}\n"]

        # Include only the most essential lines from each section
        for title, content in sections.items():
            first_line = content.strip().split("\n")[0]
            summary_lines.append(f"- **{title}** — {first_line}")

        return "\n".join(summary_lines)

    # ---------------------------------------------------------
    # MAIN ENTRY POINT
    # ---------------------------------------------------------
    def apply(self, topic: str, rendered_sections: Dict[str, str]) -> str:
        """
        Applies the concise edition logic to the rendered lesson sections.
        """
        return self.summarize(topic, rendered_sections)
