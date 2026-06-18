    # ============================================================
    # ===================== START: OUTPUT FORMATTING =============
    # ============================================================

    def _output_formatting(self, text: str) -> str:
        """
        Final formatting pass:
        - normalises whitespace
        - fixes bullet alignment
        - ensures consistent heading spacing
        - removes accidental double newlines
        - trims trailing spaces
        - ensures deterministic formatting
        """

        if not text:
            return ""

        lines = text.split("\n")
        cleaned = []

        for line in lines:
            # Trim whitespace
            l = line.rstrip()

            # Normalise bullets
            if l.startswith("-  "):
                l = "- " + l[3:]
            if l.startswith("*  "):
                l = "* " + l[3:]

            # Normalise heading spacing
            if l.startswith("#"):
                l = l.replace("  ", " ")

            cleaned.append(l)

        # Rejoin with deterministic spacing
        output = "\n".join(cleaned)

        # Remove excessive blank lines
        while "\n\n\n" in output:
            output = output.replace("\n\n\n", "\n\n")

        return output.strip()

    # ============================================================
    # ===================== END: OUTPUT FORMATTING ===============
    # ============================================================
