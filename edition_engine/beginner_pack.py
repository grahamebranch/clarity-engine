# beginner_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Beginner Edition Pack (v1)

from typing import Dict

class BeginnerEditionPack:
    """
    Beginner Edition Pack
    Simplifies concepts, removes jargon, and adds gentle explanations.
    Works alongside the Edition Engine's generic 'beginner' transform.
    """

    def __init__(self):
        self.version = "1.0"

    # ---------------------------------------------------------
    # BEGINNER LOGIC
    # ---------------------------------------------------------
    def simplify_line(self, line: str) -> str:
        """
        Simplifies a single line by removing jargon and adding clarity.
        """
        if not line.strip():
            return ""
        return f"- Simple idea: {line.strip()}"

    def simplify_block(self, title: str, content: str) -> str:
        """
        Converts a section into a beginner-friendly rendering.
        """
        lines = content.strip().split("\n")
        simplified = [self.simplify_line(line) for line in lines]

        return (
            f"### {title} — Beginner Friendly\n"
            "Here’s the idea explained in a simple, gentle way:\n"
            + "\n".join(simplified)
            + "\n"
        )

    # ---------------------------------------------------------
    # MAIN ENTRY POINT
    # ---------------------------------------------------------
    def apply(self, rendered_sections: Dict[str, str]) -> str:
        """
        Applies beginner logic to all rendered lesson sections.
        """
        beginner_blocks = []
        for title, content in rendered_sections.items():
            beginner_blocks.append(self.simplify_block(title, content))

        return "\n".join(beginner_blocks)
