"""
EL7 - Packaging & Metadata (FastPath Version)
Produces final structured output for UI/API consumption.
"""

class EL7Packaging:
    def run(self, data: dict) -> dict:
        text = data.get("text", "")
        sections = data.get("sections", [])

        packaged_sections = []
        for sec in sections:
            packaged_sections.append({
                "id": sec.get("id"),
                "clarity_score": sec.get("clarity_score"),
                "metadata": sec.get("metadata", {}),
                "units": [
                    {
                        "id": u.get("id"),
                        "text": u.get("text"),
                        "role": u.get("role", "content"),
                        "source_block": u.get("source_block")
                    }
                    for u in sec.get("units", [])
                ]
            })

        return {
            "stage": "EL7",
            "text": text,
            "sections": packaged_sections
        }
