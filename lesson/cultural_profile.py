"""
Cultural Profile — defines cultural note density per CEFR level.
"""

from typing import Dict


class CulturalProfile:
    def get_profile(self, level: str) -> Dict[str, int]:
        """
        Returns cultural note targets for the given level.
        """

        profiles = {
            "A2": {"notes": 1},
            "B1": {"notes": 2},
            "B2": {"notes": 3},
            "C1": {"notes": 4},
        }

        return profiles.get(level, profiles["B1"])
