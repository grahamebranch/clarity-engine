"""
FinalOutputLayer - v2.1

Purpose:
- Preserve paragraph boundaries
- Preserve list blocks
- Perform only light, safe cleanup
- Capitalise sentence starts inside paragraphs
- No reflow, no merging, no structural changes
"""

import re


class FinalOutputLayer:
    def __init__(self):
        self.list_markers = [
            r"^\s*[-*]\s+",
            r"^\s*\d+\.\s+",
            r"^\s*[a-zA-Z]\)\s+",
        ]

    def _is_list_item(self, line: str) -> bool:
        for pattern in self.list_markers:
            if re.match(pattern, line):
                return True
        return False

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

    def _clean_line(self, line: str) -> str:
        line = line.rstrip()
        line = re.sub(r"\s{2,}", " ", line)
        return line

    def _capitalise_sentence_starts(self, text: str) -> str:
        def repl(match):
            before = match.group(1)
            letter = match.group(2)
            return before + letter.upper()

        text = re.sub(r"([.!?]\s+)([a-z])", repl, text)
        return text

    def _clean_paragraph(self, lines):
        if any(self._is_list_item(line) for line in lines):
            return "\n".join(self._clean_line(line) for line in lines)

        merged = " ".join(line.strip() for line in lines)
        merged = re.sub(r"\s{2,}", " ", merged)
        merged = re.sub(r"\s+([,.!?;:])", r"\1", merged)
        merged = re.sub(r"([,.!?;:])([A-Za-z])", r"\1 \2", merged)
        merged = self._capitalise_sentence_starts(merged)
        return merged.strip()

    def final_output(self, text: str) -> str:
        paragraphs = self._split_paragraphs(text)
        cleaned = [self._clean_paragraph(p) for p in paragraphs]
        return "\n\n".join(cleaned).strip()
