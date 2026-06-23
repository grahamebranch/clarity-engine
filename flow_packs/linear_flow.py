# linear_flow.py — FastPath Whole-File Replacement
# Clarity Companion — Linear Flow Pack (v1)

from typing import Dict

class LinearFlowPack:
    """
    LinearFlowPack
    Returns sections in the order they were provided.
    """

    def __init__(self):
        self.version = "1.0"

    def order(self, rendered_sections: Dict[str, str]) -> Dict[str, str]:
        """
        Returns the sections in the same order they were rendered.
        """
        return rendered_sections
