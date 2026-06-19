"""
EL3 - Deterministic Structural Normalisation - v3.0

Purpose:
- Preserve paragraph boundaries
- Preserve list blocks (bullet, numbered, lettered)
- Merge broken lines only inside non-list paragraphs
- Maintain connector-aware sentence boundaries
- No rewriting, no clarity edits, no semantic changes
"""

import re


class EL3Deterministic:
    def __init__(self):
        # List item patterns
        self.list_markers = [
            r"^\s*[-*]\s+",
            r"^\s*\d+\.\s+",
            r"^\s*[a-zA-Z]\)\s+",
        ]

        # Sentence connectors that should NOT trigger capitalisation
        self.connectors = {
            "and", "or", "but", "so", "yet", "nor",
            "because", "although", "however", "therefore",
            "moreover", "furthermore", "meanwhile",
        }

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
    # MERGE NON-LIST PARAGRAPHS
    # ---------------------------------------------------------

    def _merge_paragraph(self, lines):
        if any(self._is_list_item(line) for line in lines):
            return "\n".join(line.rstrip() for line in lines)

        merged = " ".join(line.strip() for line in lines)
        merged = re.sub(r"\s{2,}", " ", merged)
        return merged.strip()

    # ---------------------------------------------------------
    # CONNECTOR-AWARE SENTENCE NORMALISATION
    # ---------------------------------------------------------

    def _fix_sentence_starts(self, text: str) -> str:
        def repl(match):
            before = match.group(1)
            word = match.group(2)
            if word.lower() in self.connectors:
                return before + word.lower()
            return before + word.capitalize()

        return re.sub(r"([.!?]\s+)([A-Za-z]+)", repl, text)

    # ---------------------------------------------------------
    # PUBLIC ENTRYPOINT
    # ---------------------------------------------------------

    def el3(self, text: str) -> str:
        paragraphs = self._split_paragraphs(text)
        shaped = [self._merge_paragraph(p) for p in paragraphs]
        shaped = [self._fix_sentence_starts(p) for p in shaped]
        return "\n\n".join(shaped).strip()
