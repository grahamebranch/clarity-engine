"""
EL6 - Deterministic Instruction → Structured Rewrite Layer (v3.0)

Purpose:
- Detect when the user is giving multiple imperative instructions
- Rewrite them into a structured, numbered explanation
- Preserve all upstream shaping (OSF, EL3, EL4, EL5)
- Deterministic, no model calls
"""

import re
import textwrap


class EL6Rewrite:
    def _split_sentences(self, text: str):
        parts = re.split(r"([.!?])", text)
        sentences = []
        buf = ""

        for part in parts:
            if not part:
                continue
            buf += part
            if part in ".!?":
                s = buf.strip()
                if s:
                    sentences.append(s)
                buf = ""

        tail = buf.strip()
        if tail:
            sentences.append(tail)

        return sentences

    def _looks_like_instruction_block(self, sentences):
        if not (2 <= len(sentences) <= 10):
            return False

        score = 0
        for s in sentences:
            s_stripped = s.strip()

            if re.match(r"^[A-Z]", s_stripped):
                score += 1

            if re.match(r"^(I|We|You)\b", s_stripped):
                score -= 1

            if len(s_stripped) > 180:
                score -= 1

        return score >= max(1, len(sentences) // 2)

    def el6(self, text: str) -> str:
        base = text.strip()
        sentences = self._split_sentences(base)

        if self._looks_like_instruction_block(sentences):
            summary = (
                "This request outlines several actions intended to improve or restructure a piece of writing."
            )

            explanation = [
                "Here is a clearer, structured interpretation of the requested actions:"
            ]

            for i, s in enumerate(sentences, start=1):
                explanation.append(f"{i}. {s}")

            rewritten = summary + "\n\n" + "\n".join(explanation)
            return textwrap.dedent(rewritten).strip()

        return text
