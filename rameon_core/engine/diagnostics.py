"""
Diagnostics Layer (EL-10)
Produces structural metrics about the processed text.
Deterministic, zero‑LLM, zero‑probability.
"""

class DiagnosticsEngine:
    def __init__(self):
        pass

    def run(self, text: str, sections: list):
        # Count characters
        char_count = len(text)

        # Count words
        word_count = len(text.split())

        # Count sections
        section_count = len(sections)

        # Count bullets
        bullet_count = sum(
            s["content"].count("- ") + s["content"].count("* ")
            for s in sections
        )

        # Section lengths
        section_lengths = [
            {
                "title": s["title"],
                "length": len(s["content"])
            }
            for s in sections
        ]

        return {
            "characters": char_count,
            "words": word_count,
            "sections": section_count,
            "bullets": bullet_count,
            "section_lengths": section_lengths
        }
