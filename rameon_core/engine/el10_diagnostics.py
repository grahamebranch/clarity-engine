"""
EL10 - Engine Summary & Diagnostics (FastPath Version)
Produces a structured diagnostic summary of the entire edition pipeline.
"""

class EL10Diagnostics:
    def run(self, data: dict) -> dict:
        text = data.get("text", "")
        sections = data.get("sections", [])

        diagnostics = {
            "total_sections": len(sections),
            "total_units": 0,
            "total_bullets": 0,
            "total_transitions": 0,
            "clarity_scores": {},
            "section_lengths": {},
            "export_formats": {
                "markdown": "present" if "markdown" in data else "missing",
                "text": "present" if "text" in data else "missing",
                "json": "present"
            }
        }

        for sec in sections:
            sid = sec.get("id")
            units = sec.get("units", [])

            diagnostics["clarity_scores"][sid] = sec.get("clarity_score")
            diagnostics["section_lengths"][sid] = len(units)
            diagnostics["total_units"] += len(units)

            for u in units:
                t = u.get("text", "").lstrip()
                if t.startswith(("-", "*", "•")):
                    diagnostics["total_bullets"] += 1
                if u.get("role") == "transition":
                    diagnostics["total_transitions"] += 1

        return {
            "stage": "EL10",
            "text": text,
            "sections": sections,
            "diagnostics": diagnostics
        }
