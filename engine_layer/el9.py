"""
EL9Deterministic - v1.0

Purpose:
- Perform the final coherence pass before Governance.
- Ensure the text is internally consistent, stable, and free of structural anomalies.
- Deterministic only — no rewriting of meaning, no LLM behaviour.
"""

class EL9Deterministic:
    def __init__(self):
        pass

    def el9(self, text: str) -> str:
        """
        Responsibilities:
        - Ensure consistent punctuation spacing
        - Normalize repeated punctuation
        - Remove accidental double spaces
        - Stabilize sentence boundaries
        """

        # 1. Normalize double spaces
        while "  " in text:
            text = text.replace("  ", " ")

        # 2. Normalize repeated punctuation (e.g., "!!" → "!")
        replacements = {
            "!!": "!",
            "??": "?",
            "..": ".",
            "...": "…",   # ellipsis normalization
        }
        for k, v in replacements.items():
            while k in text:
                text = text.replace(k, v)

        # 3. Ensure space after punctuation if missing
        fixed = []
        for i, ch in enumerate(text):
            fixed.append(ch)
            if ch in ".!?,":
                # Add space if next char exists and is a letter
                if i + 1 < len(text) and text[i+1].isalpha():
                    fixed.append(" ")
        text = "".join(fixed)

        # 4. Final newline guarantee
        if not text.endswith("\n"):
            text += "\n"

        return text
