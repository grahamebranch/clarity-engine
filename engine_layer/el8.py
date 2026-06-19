"""
EL8Deterministic - v1.0

Purpose:
- Perform deterministic validation checks before GovernanceLayer.
- Ensure the text is structurally safe, non-empty, and well-formed.
- No rewriting, no semantic changes — validation only.
"""

class EL8Deterministic:
    def __init__(self):
        pass

    def el8(self, text: str) -> str:
        """
        Deterministic validation layer.
        Responsibilities:
        - Ensure text is not empty
        - Ensure no illegal characters
        - Ensure no broken Unicode
        - Ensure no null bytes
        - Ensure text is safe for governance processing
        """

        # 1. Guarantee non-empty text
        if not text or text.strip() == "":
            text = "[EMPTY_OUTPUT]"

        # 2. Remove null bytes (safety)
        text = text.replace("\x00", "")

        # 3. Remove any control characters except newline + tab
        cleaned = []
        for ch in text:
            if ch == "\n" or ch == "\t":
                cleaned.append(ch)
            elif ord(ch) >= 32:
                cleaned.append(ch)
        text = "".join(cleaned)

        # 4. Ensure final newline for consistency
        if not text.endswith("\n"):
            text += "\n"

        return text
