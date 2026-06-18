"""
Grammar Profile — defines grammar targets per CEFR level.
"""

from typing import Dict


class GrammarProfile:
    def get_profile(self, level: str) -> Dict[str, str]:
        """
        Returns the grammar focus for the given level.
        """

        profiles = {
            "A2": "Present simple, present continuous, basic past.",
            "B1": "Past simple vs past continuous, comparatives, modals of advice.",
            "B2": "Present perfect, conditionals (0–2), relative clauses.",
            "C1": "Mixed conditionals, advanced modals, complex noun phrases.",
        }

        return {"focus": profiles.get(level, profiles["B1"])}
