"""
OSF (Organisational Shaping Framework) - v1.0

Purpose:
- Prepare text for downstream layers (EL3, EL4, EL5)
- Normalise whitespace, line breaks, and paragraph boundaries
- Detect and preserve list structures
- Stabilise block structure so later layers receive predictable input
- Deterministic: no rewriting, no clarity edits, no semantic changes
"""

import re


class OSFShaping:
    def __init__(self):
        # Patterns for list detection
        self.list_markers = [
            r"^\s*[-*]\s+",
            r"^\s*\d+\.\s+",
            r"^\s*[a-zA-Z]\)\s+",
        ]

    # ---------------------------------------------------------
    # BASIC NORMALISATION
    # ---------------------------------------------------------

    def _normalise_whitespace(self, text: str) -> str:
        """
        - Convert Windows/Mac line endings to Unix
        - Remove trailing spaces
        - Collapse excessive blank lines
        """
        text = text.replace("\r\n", "\n").replace("\r", "\n")
        text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()

    # ---------------------------------------------------------
    # PARAGRAPH SHAPING
    # ---------------------------------------------------------

    def _split_into_paragraphs(self, text: str):
        """
        Split on blank lines. Preserve order.
        """
        raw = text.split("\n")
        paragraphs = []
        buffer = []

        for line in raw:
            if line.strip() == "":
                if buffer:
                    paragraphs.append("\n".join(buffer).strip())
                    buffer = []
            else:
                buffer.append(line)

        if buffer:
            paragraphs.append("\n".join(buffer).strip())

        return paragraphs

    def _merge_broken_lines(self, paragraphs):
        """
        Merge lines inside paragraphs unless they are list items.
        """
        merged = []

        for p in paragraphs:
            lines = p.split("\n")
            if all(not self._is_list_item(line) for line in lines):
                merged.append(" ".join(line.strip() for line in lines))
            else:
                merged.append(p)

        return merged

    # ---------------------------------------------------------
    # LIST DETECTION
    # ---------------------------------------------------------

    def _is_list_item(self, line: str) -> bool:
        for pattern in self.list_markers:
            if re.match(pattern, line):
                return True
        return False

    def _shape_lists(self, paragraphs):
        """
        Ensure list items remain on separate lines.
        """
        shaped = []

        for p in paragraphs:
            if "\n" in p:
                shaped.append(p)
            else:
                shaped.append(p)

        return shaped

    # ---------------------------------------------------------
    # FINAL CLEANUP
    # ---------------------------------------------------------

    def _final_cleanup(self, paragraphs):
        cleaned = []
        for p in paragraphs:
            p = re.sub(r"\s{2,}", " ", p)
            cleaned.append(p.strip())
        return cleaned

    # ---------------------------------------------------------
    # PUBLIC ENTRYPOINT
    # ---------------------------------------------------------

    def osf(self, text: str) -> str:
        text = self._normalise_whitespace(text)
        paragraphs = self._split_into_paragraphs(text)
        paragraphs = self._merge_broken_lines(paragraphs)
        paragraphs = self._shape_lists(paragraphs)
        paragraphs = self._final_cleanup(paragraphs)
        return "\n\n".join(paragraphs).strip()
