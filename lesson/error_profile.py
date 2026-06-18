"""
Error Profile — defines number of error patterns per CEFR level.
"""

from typing import Dict


class ErrorProfile:
    def get_profile(self, level: str) -> Dict[str, int]:
        """
        Returns error pattern density for the given level.
        """

        profiles = {
            "A2": {"errors": 1},
            "B1": {"errors": 2},
            "B2": {"errors": 3},
            "C1": {"errors": 4},
        }

        return profiles.get(level, profiles["B1"])
