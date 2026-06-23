# poetic_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Poetic Edition Pack (v1)

from typing import Dict

class PoeticEditionPack:
    """
    Poetic Edition Pack
    Transforms lesson sections into lyrical, metaphor-rich renderings.
    Works alongside the Edition Engine's generic 'poetic' transform.
    """

    def __init__(self):
        self.version = "1.0"

    # ---------------------------------------------------------
    # POETIC LOGIC
    # ---------------------------------------------------------
    def poeticize_line(self, line: str) -> str:
        """
        Adds gentle poetic shaping to a single line.
        """
        if not line.strip():
            return ""
        return f"{line.strip()}, as if carried on a quiet breeze."

    def poeticize_block(self, title: str, content: str) -> str:
        """
        Converts a section into a poetic rendering.
        """
        lines = content.strip().split("\n")
        shaped = [self.poeticize_line(line) for line in lines]

        return (
            f"### {title} — Poetic Rendering\n"
            + "\n".join(shaped)
            + "\n"
        )

    # ---------------------------------------------------------
    # MAIN ENTRY POINT
    # ---------------------------------------------------------
    def apply(self, rendered_sections: Dict[str, str]) -> str:
        """
        Applies poetic logic to all rendered lesson sections.
        """
        poetic_blocks = []
        for title, content in rendered_sections.items():
            poetic_blocks.append(self.poeticize_block(title, content))

        return "\n".join(poetic_blocks)
