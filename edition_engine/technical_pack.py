# technical_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Technical Edition Pack (v1)

from typing import Dict

class TechnicalEditionPack:
    """
    Technical Edition Pack
    Produces a more formal, precise, specification-like rendering of each section.
    Works alongside the Edition Engine's generic 'technical' transform.
    """

    def __init__(self):
        self.version = "1.0"

    # ---------------------------------------------------------
    # TECHNICAL LOGIC
    # ---------------------------------------------------------
    def formalize_line(self, line: str) -> str:
        """
        Converts a line into a more formal, specification-like statement.
        """
        if not line.strip():
            return ""
        return f"- REQUIREMENT: {line.strip()}"

    def formalize_block(self, title: str, content: str) -> str:
        """
        Converts a section into a technical rendering.
        """
        lines = content.strip().split("\n")
        formalized = [self.formalize_line(line) for line in lines]

        return (
            f"### {title} — Technical Specification\n"
            "The following requirements describe this section:\n"
            + "\n".join(formalized)
            + "\n"
        )

    # ---------------------------------------------------------
    # MAIN ENTRY POINT
    # ---------------------------------------------------------
    def apply(self, rendered_sections: Dict[str, str]) -> str:
        """
        Applies technical logic to all rendered lesson sections.
        """
        technical_blocks = []
        for title, content in rendered_sections.items():
            technical_blocks.append(self.formalize_block(title, content))

        return "\n".join(technical_blocks)
