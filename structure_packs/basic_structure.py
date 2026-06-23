# basic_structure.py — FastPath Whole-File Replacement
# Clarity Companion — Basic Structure Pack (v1)

from typing import List

class BasicStructurePack:
    """
    BasicStructurePack
    Defines the canonical lesson structure (ordered section roles).
    """

    def __init__(self):
        self.version = "1.0"

    def structure(self) -> List[str]:
        """
        Returns the ordered list of section roles for a standard lesson.
        """
        return [
            "introduction",
            "core_concepts",
            "examples",
            "practice",
            "summary",
        ]
