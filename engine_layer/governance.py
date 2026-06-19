"""
Governance Layer - v1.0

Purpose:
- Enforce deterministic safety and meaning-preservation rules
- Block disallowed transformations
- Ensure output remains within permitted behavioural boundaries
- Provide final guardrails before returning text to the user
"""

import re


class GovernanceLayer:
    def __init__(self):
        # Patterns that must never appear in output
        self.banned_patterns = [
            r"\bI predict\b",
            r"\bI guarantee\b",
            r"\bI promise\b",
            r"\bthe model thinks\b",
            r"\bthis system believes\b",
        ]

        # Tone constraints
        self.disallowed_tones = [
            "hostile",
            "insulting",
            "abusive",
            "demeaning",
        ]

    # ---------------------------------------------------------
    # BANNED PATTERN CHECKS
    # ---------------------------------------------------------

    def _remove_banned_patterns(self, text: str) -> str:
        for pattern in self.banned_patterns:
            text = re.sub(pattern, "", text, flags=re.IGNORECASE)
        return text

    # ---------------------------------------------------------
    # TONE NORMALISATION
    # ---------------------------------------------------------

    def _normalise_tone(self, text: str) -> str:
        """
        Deterministic tone softening:
        - Replace harsh constructions with neutral equivalents
        """
        replacements = [
            ("stupid", "unwise"),
            ("idiotic", "misguided"),
            ("nonsense", "incorrect"),
            ("ridiculous", "unreasonable"),
        ]

        for src, dst in replacements:
            text = re.sub(rf"\b{re.escape(src)}\b", dst, text, flags=re.IGNORECASE)

        return text

    # ---------------------------------------------------------
    # MEANING PRESERVATION CHECK
    # ---------------------------------------------------------

    def _ensure_meaning_preservation(self, text: str) -> str:
        """
        Placeholder for future semantic checks.
        Currently deterministic no-op.
        """
        return text

    # ---------------------------------------------------------
    # PUBLIC ENTRYPOINT
    # ---------------------------------------------------------

    def governance(self, text: str) -> str:
        text = self._remove_banned_patterns(text)
        text = self._normalise_tone(text)
        text = self._ensure_meaning_preservation(text)
        return text
