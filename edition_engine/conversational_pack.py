# conversational_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Conversational Edition Pack (v1)

from typing import Dict

class ConversationalEditionPack:
    """
    Conversational Edition Pack
    Makes the lesson warmer, more human, and more dialog-like.
    Works alongside the Edition Engine's generic 'conversational' transform.
    """

    def __init__(self):
        self.version = "1.0"

    # ---------------------------------------------------------
    # CONVERSATIONAL LOGIC
    # ---------------------------------------------------------
    def soften_headings(self, text: str) -> str:
        """
        Converts rigid headings into softer, more conversational ones.
        """
        lines = text.split("\n")
        softened = []
        for line in lines:
            if line.startswith("### "):
                softened.append("#### Let's talk about " + line[4:].strip())
            else:
                softened.append(line)
        return "\n".join(softened)

    def add_transitions(self, text: str) -> str:
        """
        Adds gentle transitions between sections.
        """
        blocks = text.split("\n### ")
        conversational = []
        for i, block in enumerate(blocks):
            if i == 0:
                conversational.append(block)
            else:
                conversational.append(
                    "\nBefore we move on, here's something else worth exploring:\n\n### " + block
                )
        return "\n".join(conversational)

    # ---------------------------------------------------------
    # MAIN ENTRY POINT
    # ---------------------------------------------------------
    def apply(self, rendered_sections: Dict[str, str]) -> str:
        """
        Applies conversational logic to all rendered lesson sections.
        """
        combined = "\n".join(rendered_sections.values())
        softened = self.soften_headings(combined)
        transitioned = self.add_transitions(softened)
        return transitioned
