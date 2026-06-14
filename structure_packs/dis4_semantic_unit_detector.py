"""
DIS4 - Semantic Unit Detector (MVP)
Splits blocks into simple semantic units (sentences).
"""

import re

class DIS4SemanticUnitDetector:
    def run(self, data: dict) -> dict:
        """
        MVP behaviour:
        - Split each block into sentences
        """

        blocks = data.get("blocks", [])

        semantic_units = []
        counter = 1

        for block in blocks:
            sentences = re.split(r'(?<=[.!?]) +', block["content"])
            for s in sentences:
                s = s.strip()
                if not s:
                    continue

                semantic_units.append({
                    "id": f"sem_{counter}",
                    "text": s,
                    "source_block": block["id"]
                })
                counter += 1

        return {
            "stage": "DIS4",
            "semantic_units": semantic_units
        }
