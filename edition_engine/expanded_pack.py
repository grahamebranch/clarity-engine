# expanded_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Expanded Edition Pack (v1)

from typing import Dict

class ExpandedEditionPack:
    """
    Expanded Edition Pack
    Adds elaboration, connective tissue, and depth to each section.
    Works alongside the Edition Engine's generic 'expanded' transform.
    """

    def __init__(self):
        self.version = "1.0"

    # ---------------------------------------------------------
    # EXPANSION LOGIC
    # ---------------------------------------------------------
    def expand_section(self, title: str, content: str) -> str:
        """
        Expands a single section by adding elaboration and connective explanation.
        """
        lines = content.strip().split("\n")
        intro = lines[0] if lines else ""
        body = "\n".join(lines[1:]) if len(lines) > 1 else ""

        return (
            f"### {title} — Expanded\n"
            f"{intro}\n\n"
            "Here’s a deeper look at what this means:\n"
            f"{body}\n"
            "\nThis section has been expanded to provide more clarity and context.\n"
        )

    # ---------------------------------------------------------
    # MAIN ENTRY POINT
    # ---------------------------------------------------------
    def apply(self, rendered_sections: Dict[str, str]) -> str:
        """
        Applies expanded logic to all rendered lesson sections.
        """
        expanded_blocks = []
        for title, content in rendered_sections.items():
            expanded_blocks.append(self.expand_section(title, content))

        return "\n".join(expanded_blocks)
