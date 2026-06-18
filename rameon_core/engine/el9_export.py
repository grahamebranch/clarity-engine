"""
EL9 - Export Layer (FastPath Version)
Produces final export formats: markdown, plain text, and JSON passthrough.
"""

class EL9Export:
    def run(self, data: dict) -> dict:
        text = data.get("text", "")
        sections = data.get("sections", [])

        # Markdown export (same as text, but guaranteed LF endings)
        markdown = text.replace("\r\n", "\n").replace("\r", "\n")

        # Plain text export (strip markdown symbols)
        plain = self._to_plain_text(markdown)

        return {
            "stage": "EL9",
            "markdown": markdown,
            "text": plain,
            "sections": sections
        }

    # ------------------------------------------------------------
    # Convert markdown → plain text (minimal, deterministic)
    # ------------------------------------------------------------
    def _to_plain_text(self, md: str) -> str:
        import re

        # Remove headers
        md = re.sub(r"^#+\s*", "", md, flags=re.MULTILINE)

        # Remove bullet markers
        md = re.sub(r"^\s*[-*•]\s*", "", md, flags=re.MULTILINE)

        # Remove bold/italic markers
        md = md.replace("**", "").replace("*", "").replace("_", "")

        # Normalize spacing
        lines = [line.rstrip() for line in md.split("\n")]
        return "\n".join(lines).strip()
