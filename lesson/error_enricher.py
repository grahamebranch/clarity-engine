"""
Error Enricher — injects common learner errors, corrections, and micro-practice.
Deterministic, production‑safe version with real error patterns.
"""

from typing import List, Dict
from .error_profile import ErrorProfile


class ErrorEnricher:
    def __init__(self) -> None:
        self.profile = ErrorProfile()

    def apply(self, sections: List[Dict[str, str]], level: str, topic: str) -> List[Dict[str, str]]:
        """
        Enrich each section with error patterns based on level.
        """
        profile = self.profile.get_profile(level)
        enriched = []

        for s in sections:
            enriched.append(self._enrich_section(s, profile, topic))

        return enriched

    def _enrich_section(self, section: Dict[str, str], profile: Dict[str, int], topic: str) -> Dict[str, str]:
        """
        Adds error pattern blocks to each section.
        Replaces placeholder text with real learner errors.
        """

        content = section.get("content", "")
        count = profile["errors"]
        topic_clean = topic.strip() if topic else "the topic"

        # ---------------------------------------------------------------------
        # REAL ERROR BANK (deterministic)
        # ---------------------------------------------------------------------

        error_bank = [
            {
                "error": "I very like travel.",
                "correction": "I really like travelling.",
                "why": "Learners often confuse intensifiers ('very') with adverbs ('really').",
                "practice": "Rewrite: 'I very like music.'"
            },
            {
                "error": "I want go to Italy.",
                "correction": "I want to go to Italy.",
                "why": "Learners forget the infinitive 'to' after 'want'.",
                "practice": "Rewrite: 'I want visit Spain.'"
            },
            {
                "error": "She don't like flying.",
                "correction": "She doesn't like flying.",
                "why": "Learners mix up auxiliary verbs in the present simple.",
                "practice": "Rewrite: 'He don't eat meat.'"
            },
            {
                "error": "I am agree.",
                "correction": "I agree.",
                "why": "Some languages use a verb + adjective structure; English uses a simple verb.",
                "practice": "Rewrite: 'I am disagree.'"
            },
            {
                "error": "He go to work by bus.",
                "correction": "He goes to work by bus.",
                "why": "Learners forget the -s ending for third person singular.",
                "practice": "Rewrite: 'She walk to school.'"
            },
        ]

        selected = error_bank[:count]

        # ---------------------------------------------------------------------
        # Build block
        # ---------------------------------------------------------------------
        error_block = ["\n\n[Common Learner Errors]"]

        for i, item in enumerate(selected, start=1):
            error_block.append(
                f"- Error {i}: {item['error']}\n"
                f"  Correction: {item['correction']}\n"
                f"  Why it happens: {item['why']}\n"
                f"  Micro-practice: {item['practice']}"
            )

        enriched = dict(section)
        enriched["content"] = content + "\n".join(error_block)
        return enriched
