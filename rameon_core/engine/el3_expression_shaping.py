"""
EL3 - Expression Shaping (FastPath Version)
Deterministic flow smoothing, bullet-aware shaping, and transition control.
"""

import re

class EL3ExpressionShaping:
    def run(self, data: dict) -> dict:
        sections = data.get("sections", [])

        shaped_sections = []
        for sec in sections:
            shaped_units = []
            last_was_transition = False

            for u in sec.get("units", []):
                text = u.get("text", "").strip()

                # Detect bullets
                is_bullet = text.lstrip().startswith(("-", "*", "•"))

                # Shape text
                shaped_text = self._shape_text(text, is_bullet)

                # Suppress duplicate transitions
                if u.get("role") == "transition":
                    if last_was_transition:
                        continue
                    last_was_transition = True
                else:
                    last_was_transition = False

                shaped_units.append({
                    **u,
                    "text": shaped_text
                })

            shaped_sections.append({
                **sec,
                "units": shaped_units
            })

        return {
            "stage": "EL3",
            "sections": shaped_sections
        }

    # ------------------------------------------------------------
    # Core text shaping logic (bullet-aware)
    # ------------------------------------------------------------
    def _shape_text(self, text: str, is_bullet: bool) -> str:
        if not text:
            return text

        # 1. Normalize spacing
        text = re.sub(r"\s+", " ", text).strip()

        # 2. Remove trailing punctuation before shaping
        text = re.sub(r"[.?!]+$", "", text)

        # 3. Micro-replacements (flow smoothing)
        replacements = {
            "in order to": "to",
            "due to the fact that": "because",
            "at this point in time": "now",
            "in the event that": "if",
            "for the purpose of": "to",
            "with regard to": "about",
            "in terms of": "regarding",
            "it is important to note that": "notably",
            "as well as": "and",
            "a bit": "slightly",
            "kind of": "somewhat",
            "sort of": "somewhat",
        }

        for bad, good in replacements.items():
            text = re.sub(rf"\b{bad}\b", good, text, flags=re.IGNORECASE)

        # 4. Capitalize first letter (but not bullets)
        if not is_bullet and text and text[0].islower():
            text = text[0].upper() + text[1:]

        # 5. Ensure clean ending
        if not text.endswith("."):
            text += "."

        return text
