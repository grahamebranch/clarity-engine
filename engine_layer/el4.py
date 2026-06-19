"""
EL4 - Deterministic Clarity Layer - v3.0

Purpose:
- Perform light, deterministic clarity tightening
- Preserve paragraph boundaries
- Preserve list blocks (bullet, numbered, lettered)
- Operate only inside non-list paragraphs
- No structural flattening, no semantic jumps
"""

import re


class EL4Deterministic:
    def __init__(self):
        # List item patterns
        self.list_markers = [
            r"^\s*[-*]\s+",
            r"^\s*\d+\.\s+",
            r"^\s*[a-zA-Z]\)\s+",
        ]

        # Hedging phrases to soften/remove
        self.hedges = [
            r"\bpossibly\b",
            r"\bprobably\b",
            r"\bperhaps\b",
            r"\bmaybe\b",
            r"\bseems to\b",
            r"\bappears to\b",
            r"\bkind of\b",
            r"\bsort of\b",
        ]

        # Weak openers to trim
        self.weak_openers = [
            r"^\s*in order to\s+",
            r"^\s*it is important to note that\s+",
            r"^\s*it is important to\s+",
        ]

    # ---------------------------------------------------------
    # LIST DETECTION
    # ---------------------------------------------------------

    def _is_list_item(self, line: str) -> bool:
        for pattern in self.list_markers:
            if re.match(pattern, line):
                return True
        return False

    # ---------------------------------------------------------
    # PARAGRAPH SPLITTING
    # ---------------------------------------------------------

    def _split_paragraphs(self, text: str):
        raw = text.split("\n")
        paragraphs = []
        buffer = []

        for line in raw:
            if line.strip() == "":
                if buffer:
                    paragraphs.append(buffer)
                    buffer = []
            else:
                buffer.append(line)

        if buffer:
            paragraphs.append(buffer)

        return paragraphs

    # ---------------------------------------------------------
    # CLARITY TIGHTENING FOR NON-LIST PARAGRAPHS
    # ---------------------------------------------------------

    def _strip_hedging(self, text: str) -> str:
        for pattern in self.hedges:
            text = re.sub(pattern, "", text, flags=re.IGNORECASE)
        text = re.sub(r"\s{2,}", " ", text)
        return text.strip()

    def _strip_weak_openers(self, text: str) -> str:
        for pattern in self.weak_openers:
            text = re.sub(pattern, "", text, flags=re.IGNORECASE)
        return text.strip()

    def _normalise_spaces(self, text: str) -> str:
        text = re.sub(r"\s{2,}", " ", text)
        text = re.sub(r"\s+([,.!?;:])", r"\1", text)
        text = re.sub(r"([,.!?;:])([A-Za-z])", r"\1 \2", text)
        return text.strip()

    def _clarify_paragraph(self, lines):
        if any(self._is_list_item(line) for line in lines):
            return "\n".join(line.rstrip() for line in lines)

        merged = " ".join(line.strip() for line in lines)
        merged = self._strip_weak_openers(merged)
        merged = self._strip_hedging(merged)
        merged = self._normalise_spaces(merged)
        return merged

    # ---------------------------------------------------------
    # PUBLIC ENTRYPOINT
    # ---------------------------------------------------------

    def el4(self, text: str) -> str:
        paragraphs = self._split_paragraphs(text)
        clarified = [self._clarify_paragraph(p) for p in paragraphs]
        return "\n\n".join(clarified).strip()
