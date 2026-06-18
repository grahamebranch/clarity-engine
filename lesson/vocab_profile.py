"""
Vocabulary Profile — defines lexical richness per CEFR level.
"""

from typing import Dict, List


class VocabularyProfile:
    def get_profile(self, level: str) -> Dict[str, int]:
        """
        Returns lexical richness targets for the given level.
        """

        profiles = {
            "A2": {
                "synonyms": 1,
                "collocations": 1,
                "idioms": 0,
                "contrast_pairs": 0,
                "stretch_vocab": 0,
            },
            "B1": {
                "synonyms": 2,
                "collocations": 2,
                "idioms": 1,
                "contrast_pairs": 1,
                "stretch_vocab": 1,
            },
            "B2": {
                "synonyms": 3,
                "collocations": 3,
                "idioms": 1,
                "contrast_pairs": 2,
                "stretch_vocab": 2,
            },
            "C1": {
                "synonyms": 4,
                "collocations": 4,
                "idioms": 2,
                "contrast_pairs": 2,
                "stretch_vocab": 3,
            },
        }

        return profiles.get(level, profiles["B1"])
