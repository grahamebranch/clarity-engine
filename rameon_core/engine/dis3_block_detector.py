"""
DIS3 - Block Detector (MVP)
Groups structural units into blocks.
"""

class DIS3BlockDetector:
    def run(self, data: dict) -> dict:
        """
        MVP behaviour:
        - Each DIS2 unit becomes a block
        """

        units = data.get("units", [])

        blocks = []
        for idx, u in enumerate(units):
            blocks.append({
                "id": f"block_{idx+1}",
                "content": u["raw"],
                "source_unit": u["id"]
            })

        return {
            "stage": "DIS3",
            "blocks": blocks
        }
