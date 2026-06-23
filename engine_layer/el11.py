"""
EL11 - Deterministic Clarity Scoring Layer (v1.0)

Purpose:
- Provide a clarity score based on deterministic heuristics
- No rewriting, no semantic changes
- Score reflects structural clarity, sentence quality, and conciseness
"""

import re
from dataclasses import dataclass, asdict


@dataclass
class ClarityScore:
    score: int
    details: dict


class EL11Clarity:
    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    def _sentence_count(self, text):
        return len([s for s in re.split(r"[.!?]+", text) if s.strip()])

    def _avg_sentence_length(self, text):
        sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
        if not sentences:
            return 0
        lengths = [len(s.split()) for s in sentences]
        return sum(lengths) / len(lengths)

    def _has_structure(self, text):
        return bool(re.search(r"^\d+\.", text, flags=re.MULTILINE))

    def _redundancy_penalty(self, text):
        words = text.lower().split()
        unique = len(set(words))
        total = len(words)
        if total == 0:
            return 0
        ratio = unique / total
        return 0 if ratio > 0.6 else -5

    # ---------------------------------------------------------
    # Public entrypoint
    # ---------------------------------------------------------

    def el11(self, text: str) -> dict:
        score = 50  # baseline

        # 1. Sentence count bonus
        sc = self._sentence_count(text)
        if 2 <= sc <= 8:
            score += 10
        elif sc > 12:
            score -= 5

        # 2. Average sentence length
        avg_len = self._avg_sentence_length(text)
        if 8 <= avg_len <= 20:
            score += 10
        elif avg_len > 30:
            score -= 10

        # 3. Structural clarity (numbered list)
        if self._has_structure(text):
            score += 10

        # 4. Redundancy penalty
        score += self._redundancy_penalty(text)

        # Clamp score
        score = max(0, min(100, score))

        details = {
            "sentence_count": sc,
            "avg_sentence_length": avg_len,
            "has_structure": self._has_structure(text),
        }

        return asdict(ClarityScore(score=score, details=details))
