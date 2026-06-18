"""
DIS2 - Structure Detector (Improved)
Splits text into paragraphs AND separates bullet lines into individual units.
"""

import re

class DIS2StructureDetector:
    def run(self, text: str) -> dict:
        """
        Improved behaviour:
        - Split text into paragraphs
        - Within each paragraph, split bullet lines into separate units
        """

        raw_paragraphs = [
            p for p in text.split("\n\n") if p.strip()
        ]

        units = []
        unit_counter = 1

        bullet_pattern = re.compile(r"^\s*([-*•] |\d+[.)]\s+)")

        for para in raw_paragraphs:
            lines = para.split("\n")

            for line in lines:
                stripped = line.strip()
                if not stripped:
                    continue

                # If it's a bullet → separate unit
                if bullet_pattern.match(stripped):
                    units.append({
                        "id": f"unit_{unit_counter}",
                        "raw": stripped,
                        "type": "bullet"
                    })
                    unit_counter += 1
                else:
                    # Normal paragraph line → keep as paragraph unit
                    units.append({
                        "id": f"unit_{unit_counter}",
                        "raw": stripped,
                        "type": "paragraph"
                    })
                    unit_counter += 1

        return {
            "stage": "DIS2",
            "units": units
        }
