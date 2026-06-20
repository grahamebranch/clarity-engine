"""
Rewrite Layer (EL-13)
Deterministic, rule-based rewrite (no LLM).
Currently: simple clarity pass.
"""

class RewriteEngine:
    def __init__(self):
        pass

    def run(self, text: str, sections: list):
        # For now: very conservative rewrite.
        # - Trim whitespace
        # - Collapse multiple blank lines
        # - Preserve content exactly otherwise.

        lines = text.split("\n")
        cleaned = []

        for line in lines:
            stripped = line.rstrip()
            cleaned.append(stripped)

        # Collapse multiple blank lines
        final_lines = []
        blank_streak = 0

        for line in cleaned:
            if line.strip() == "":
                blank_streak += 1
                if blank_streak <= 1:
                    final_lines.append("")
            else:
                blank_streak = 0
                final_lines.append(line)

        rewritten = "\n".join(final_lines).strip()

        return rewritten
