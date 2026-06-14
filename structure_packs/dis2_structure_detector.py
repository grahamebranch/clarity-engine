"""
DIS2 - Structure Detector (MVP)
Identifies high‑level structural units in the text.
"""

class DIS2StructureDetector:
    def run(self, text: str) -> dict:
        """
        MVP behaviour:
        - Split text into paragraphs
        - Treat each paragraph as a structural unit
        """

        paragraphs = [
            p.strip() for p in text.split("\n\n") if p.strip()
        ]

        units = []
        for idx, p in enumerate(paragraphs):
            units.append({
                "id": f"unit_{idx+1}",
                "raw": p,
                "type": "paragraph"
            })

        return {
            "stage": "DIS2",
            "units": units
        }
