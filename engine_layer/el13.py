"""
EL13 - Deterministic Diagnostics Layer (v1.0)

Purpose:
- Generate simple, rule-based diagnostics from clarity score + text
- No rewriting, no semantic changes
"""

from dataclasses import dataclass, asdict


@dataclass
class Diagnostics:
    suggestions: list
    summary: str


class EL13Diagnostics:
    def el13(self, text: str, clarity: dict) -> dict:
        score = clarity.get("score", 50)
        details = clarity.get("details", {})
        suggestions = []

        sc = details.get("sentence_count", 0)
        avg_len = details.get("avg_sentence_length", 0)
        has_structure = details.get("has_structure", False)

        if score < 60:
            suggestions.append("Overall clarity is low; consider simplifying sentences and reducing redundancy.")
        if avg_len > 25:
            suggestions.append("Sentences are quite long; try splitting complex sentences into shorter ones.")
        if sc < 2:
            suggestions.append("Very few sentences detected; consider adding more structure.")
        if not has_structure:
            suggestions.append("No numbered structure detected; consider using lists or sections for clarity.")

        if not suggestions:
            summary = "Text is generally clear and well-structured."
        else:
            summary = "There are opportunities to improve clarity and structure."

        return asdict(Diagnostics(suggestions=suggestions, summary=summary))
