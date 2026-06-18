"""
Guidance Profile — defines guidance density per user level.
"""

from typing import Dict


class GuidanceProfile:
    def get_profile(self, level: str) -> Dict[str, int]:
        """
        Returns guidance density for the given level.
        """

        profiles = {
            "A2": {"steps": 1},
            "B1": {"steps": 2},
            "B2": {"steps": 3},
            "C1": {"steps": 4},
        }

        return profiles.get(level, profiles["B1"])
