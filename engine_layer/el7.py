"""
EL7Deterministic - v1.0

Purpose:
- Apply final structural packaging before governance.
- Ensure the text is cleanly segmented, stable, and ready for compliance checks.
- Perform deterministic, rule-based adjustments only (no LLM, no randomness).
"""

class EL7Deterministic:
    def __init__(self):
        pass

    def el7(self, text: str) -> str:
        """
        Deterministic packaging layer.
        Responsibilities:
        - Normalize spacing
        - Ensure paragraph boundaries are clean
        - Remove stray whitespace
        - Enforce consistent newline rules
        - Prepare text for GovernanceLayer
        """

        # 1. Strip leading/trailing whitespace
        text = text.strip()

        # 2. Normalize multiple blank lines → single blank line
        while "\n\n\n" in text:
            text = text.replace("\n\n\n", "\n\n")

        # 3. Ensure paragraphs don't start with spaces
        lines = text.split("\n")
        cleaned = [line.lstrip() for line in lines]
        text = "\n".join(cleaned)

        # 4. Remove trailing spaces on each line
        text = "\n".join(line.rstrip() for line in text.split("\n"))

        # 5. Guarantee final newline for consistency
        if not text.endswith("\n"):
            text += "\n"

        return text
