"""
Level Applier — adjusts section content based on CEFR level.
"""

from typing import List, Dict


class LevelApplier:
    def apply(self, sections: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
        """
        Apply level-based shaping to each section.
        """

        shaped = []
        for s in sections:
            shaped.append(self._shape_section(s, level))
        return shaped

    def _shape_section(self, section: Dict[str, str], level: str) -> Dict[str, str]:
        """
        Deterministic shaping rules per level.
        """

        content = section.get("content", "")

        if level == "A2":
            content += (
                "\n\n[Level A2 Notes]\n"
                "- Use simple sentences.\n"
                "- Avoid idioms.\n"
                "- Keep vocabulary basic.\n"
            )

        elif level == "B1":
            content += (
                "\n\n[Level B1 Notes]\n"
                "- Use everyday vocabulary.\n"
                "- Include 1 useful phrase.\n"
                "- Keep grammar straightforward.\n"
            )

        elif level == "B2":
            content += (
                "\n\n[Level B2 Notes]\n"
                "- Add 2–3 advanced phrases.\n"
                "- Include 1 idiom.\n"
                "- Encourage longer responses.\n"
            )

        elif level == "C1":
            content += (
                "\n\n[Level C1 Notes]\n"
                "- Add nuanced vocabulary.\n"
                "- Include 2 idioms.\n"
                "- Encourage complex reasoning.\n"
            )

        shaped = dict(section)
        shaped["content"] = content
        return shaped
