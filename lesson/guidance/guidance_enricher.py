"""
Guidance Enricher — applies domain‑aware guidance transformations to lesson sections.
Deterministic, production‑safe version with real learner guidance.
"""

from typing import List, Dict


class GuidanceEnricher:
    def __init__(self) -> None:
        pass

    def apply(
        self,
        sections: List[Dict[str, str]],
        level: str,
        domain: str = "lesson",
    ) -> List[Dict[str, str]]:
        """
        Apply guidance transformations to sections.
        Domain-aware: the router decides *whether* this runs; this function
        simply performs the enrichment.
        """

        enriched_sections: List[Dict[str, str]] = []

        for section in sections:
            new_section = dict(section)
            base = new_section.get("content", "")

            # ------------------------------------------------------------------
            # REAL GUIDANCE CONTENT (deterministic)
            # ------------------------------------------------------------------

            guidance_bank = [
                "Read the section once for general meaning, then again for details.",
                "Underline or highlight any new or useful expressions.",
                "Say key phrases aloud to build fluency and confidence.",
                "Connect the content to a real situation in your own life.",
                "Note one question you would like to ask your teacher.",
                "Summarise the main idea in one clear sentence.",
                "Practise one example using your own information.",
            ]

            # Level‑aware but deterministic: shorter guidance for A‑levels, fuller for B/C
            if level.lower().startswith("a"):
                selected = guidance_bank[:3]
            elif level.lower().startswith("b"):
                selected = guidance_bank[:5]
            else:
                selected = guidance_bank  # full set for C‑levels

            # ------------------------------------------------------------------
            # Build block
            # ------------------------------------------------------------------
            block_lines = ["\n\n[Guidance]"]
            for i, step in enumerate(selected, start=1):
                block_lines.append(f"- Step {i}: {step}")

            # Domain tag (kept because your router uses it)
            block_lines.append(f"- Domain context: {domain}")

            new_section["content"] = base + "\n".join(block_lines)
            enriched_sections.append(new_section)

        return enriched_sections
