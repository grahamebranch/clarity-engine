"""
EL5 - Deterministic Rewrite Layer - v2.0

Purpose:
- Perform slightly stronger clarity + concision rewrites
- Preserve paragraph boundaries
- Preserve list blocks (bullet, numbered, lettered)
- Operate only inside non-list paragraphs
- No structural flattening, no list merging
"""

import re


class EL5Rewrite:
    def __init__(self):
        # List item patterns
        self.list_markers = [
            r"^\s*[-*]\s+",
            r"^\s*\d+\.\s+",
            r"^\s*[a-zA-Z]\)\s+",
        ]

        # Simple phrase tightening patterns (deterministic)
        self.replacements = [
            (r"\bat this point in time\b", "now"),
            (r"\bthere is a need to\b", "we need to"),
            (r"\bin order to\b", "to"),
            (r"\bit is important to note that\b", ""),
            (r"\bit is important to\b", "we should"),
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
    # REWRITE NON-LIST PARAGRAPHS
    # ---------------------------------------------------------

    def _apply_replacements(self, text: str) -> str:
        for pattern, repl in self.replacements:
            text = re.sub(pattern, repl, text, flags=re.IGNORECASE)
        return text

    def _normalise_spaces(self, text: str) -> str:
        text = re.sub(r"\s{2,}", " ", text)
        text = re.sub(r"\s+([,.!?;:])", r"\1", text)
        text = re.sub(r"([,.!?;:])([A-Za-z])", r"\1 \2", text)
        return text.strip()

    def _capitalise_start(self, text: str) -> str:
        text = text.lstrip()
        if not text:
            return text
        return text[0].upper() + text[1:]

    def _rewrite_paragraph(self, lines):
        if any(self._is_list_item(line) for line in lines):
            return "\n".join(line.rstrip() for line in lines)

        merged = " ".join(line.strip() for line in lines)
        merged = self._apply_replacements(merged)
        merged = self._normalise_spaces(merged)
        merged = self._capitalise_start(merged)
        return merged

    # ---------------------------------------------------------
    # PUBLIC ENTRYPOINT
    # ---------------------------------------------------------

    def el5(self, text: str) -> str:
        paragraphs = self._split_paragraphs(text)
        rewritten = [self._rewrite_paragraph(p) for p in paragraphs]
        return "\n\n".join(rewritten).strip()
