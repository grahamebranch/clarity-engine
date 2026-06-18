class DIS1DetectStructure:
    def run(self, text: str) -> dict:
        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

        units = []
        for idx, p in enumerate(paragraphs):
            units.append({
                "id": f"p{idx+1}",
                "raw": p,
                "type": "paragraph"
            })

        return {
            "stage": "DIS1",
            "units": units
        }
