"""
EL3 - Expression Shaping
Improves readability and expression without changing meaning.

Goals:
- Smooth awkward phrasing
- Improve flow between units
- Light grammar and style adjustments
- Preserve meaning (no hallucination, no rewriting intent)

This is a deterministic, rule-based shaper.
"""

import re

class EL3ExpressionShaping:
    def run(self, data: dict) -> dict:
        sections = data.get("sections", [])

        shaped = []
        for sec in sections:
            shaped_units = []
            for u in sec.get("units", []):
                text = u.get("text", "")
                shaped_text = self._shape_text(text)
                shaped_units.append({
                    **u,
                    "text": shaped_text
                })

            shaped.append({
                **sec,
                "units": shaped_units
            })

        return {
            "stage": "EL3",
            "sections": shaped
        }

    # ------------------------------------------------------------
    # Core text shaping logic
    # ------------------------------------------------------------
    def _shape_text(self, text: str) -> str:
        if not text:
            return text

        # 1. Normalize spacing
        text = re.sub(r"\s+", " ", text).strip()

        # 2. Fix common awkward patterns
        replacements = {
            "in order to": "to",
            "due to the fact that": "because",
            "at this point in time": "now",
            "in the event that": "if",
            "for the purpose of": "to",
            "with regard to": "about",
            "in terms of": "regarding",
            "it is important to note that": "notably",
        }

        for bad, good in replacements.items():
            text = re.sub(rf"\b{bad}\b", good, text, flags=re.IGNORECASE)

        # 3. Capitalize first letter if missing
        if text and text[0].islower():
            text = text[0].upper() + text[1:]

        # 4. Ensure sentence ends cleanly
        if text[-1] not in ".!?":
            text += "."

        return text
