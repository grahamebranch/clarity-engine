"""
EL5 - Output Composer (FastPath Version)
Turns fused units into final formatted text.
"""

class EL5OutputComposer:
    def run(self, data: dict) -> dict:
        sections = data.get("sections", [])

        final_lines = []
        for sec in sections:
            # Section header (if present)
            header = self._extract_header(sec)
            if header:
                final_lines.append(header)
                final_lines.append("")  # blank line after header

            # Compose units
            for u in sec.get("units", []):
                text = u.get("text", "").strip()

                # Bullet formatting
                if text.lstrip().startswith(("-", "*", "•")):
                    final_lines.append(text)
                    continue

                # Transition formatting
                if u.get("role") == "transition":
                    final_lines.append(text)
                    continue

                # Narrative paragraph
                final_lines.append(text)
                final_lines.append("")  # blank line after paragraph

        # Clean trailing blanks
        while final_lines and not final_lines[-1].strip():
            final_lines.pop()

        final_text = "\n".join(final_lines)

        return {
            "stage": "EL5",
            "text": final_text,
            "sections": sections
        }

    # ------------------------------------------------------------
    # Extract section header if present
    # ------------------------------------------------------------
    def _extract_header(self, sec):
        for u in sec.get("units", []):
            t = u.get("text", "").strip()
            if t.startswith("#"):
                return t
        return None
