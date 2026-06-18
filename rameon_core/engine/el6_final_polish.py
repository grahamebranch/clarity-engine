"""
EL6 - Final Polishing (FastPath Version)
Mechanical cleanup of the final text output.
"""

import re

class EL6FinalPolish:
    def run(self, data: dict) -> dict:
        text = data.get("text", "")

        # 1. Normalize line endings
        text = text.replace("\r\n", "\n").replace("\r", "\n")

        # 2. Remove trailing spaces on each line
        lines = [line.rstrip() for line in text.split("\n")]

        # 3. Collapse multiple blank lines → max 1
        cleaned = []
        blank = False
        for line in lines:
            if not line.strip():
                if not blank:
                    cleaned.append("")
                blank = True
            else:
                cleaned.append(line)
                blank = False

        text = "\n".join(cleaned)

        # 4. Fix double punctuation
        text = re.sub(r"([.!?]){2,}", r"\1", text)

        # 5. Ensure bullets have a space after marker
        text = re.sub(r"^([-*•])(?=\S)", r"\1 ", text, flags=re.MULTILINE)

        # 6. Ensure headers have a blank line after them
        text = re.sub(r"^(#+ .+)\n(?!\n)", r"\1\n\n", text, flags=re.MULTILINE)

        # 7. Remove trailing blank lines
        text = text.rstrip()

        return {
            "stage": "EL6",
            "text": text
        }
