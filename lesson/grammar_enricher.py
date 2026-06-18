"""
Grammar Enricher — injects grammar focus, examples, errors, and practice.
Deterministic, production‑safe version with real grammar content.
"""

from typing import List, Dict
from .grammar_profile import GrammarProfile


class GrammarEnricher:
    def __init__(self) -> None:
        self.profile = GrammarProfile()

    def apply(self, sections: List[Dict[str, str]], level: str, topic: str) -> List[Dict[str, str]]:
        """
        Enrich each section with grammar content based on level.
        """
        grammar = self.profile.get_profile(level)
        enriched = []

        for s in sections:
            enriched.append(self._enrich_section(s, grammar, topic))

        return enriched

    def _enrich_section(self, section: Dict[str, str], grammar: Dict[str, str], topic: str) -> Dict[str, str]:
        """
        Adds grammar blocks to each section.
        Replaces placeholder text with real, level‑appropriate grammar content.
        """

        content = section.get("content", "")
        focus = grammar["focus"]
        topic_clean = topic.strip() if topic else "the topic"

        # ---------------------------------------------------------------------
        # REAL GRAMMAR CONTENT (deterministic)
        # ---------------------------------------------------------------------

        # Example sentences by grammar focus
        example_bank = {
            "modals_of_advice": f"You should check the weather before you travel.",
            "comparatives": f"Travelling by train is usually cheaper than flying.",
            "past_simple_vs_continuous": f"I was packing my bag when my friend called.",
            "future_plans": f"I'm going to visit Italy next month.",
            "present_perfect_experience": f"I've visited many countries, but Japan was my favourite.",
        }

        # Common learner errors
        error_bank = {
            "modals_of_advice": "Learners often say 'You should to go' instead of 'You should go'.",
            "comparatives": "Learners sometimes forget 'than' in comparative sentences.",
            "past_simple_vs_continuous": "Learners confuse the long action (continuous) with the short action (simple).",
            "future_plans": "Learners mix up 'going to' and 'will' when talking about plans.",
            "present_perfect_experience": "Learners incorrectly use past simple for life experiences.",
        }

        # Controlled practice tasks
        practice_bank = {
            "modals_of_advice": "Rewrite: 'You should to book early.' → 'You should book early.'",
            "comparatives": "Rewrite: 'The train is fast the bus.' → 'The train is faster than the bus.'",
            "past_simple_vs_continuous": "Rewrite: 'I cooked when the phone rang.' → 'I was cooking when the phone rang.'",
            "future_plans": "Rewrite: 'I will visit Spain next summer (plan).' → 'I'm going to visit Spain next summer.'",
            "present_perfect_experience": "Rewrite: 'I went to Paris many times.' → 'I have been to Paris many times.'",
        }

        # Resolve grammar focus key
        focus_key = grammar.get("key", "modals_of_advice")

        example = example_bank.get(focus_key, f"Here is an example related to {topic_clean}.")
        error = error_bank.get(focus_key, "Learners often make small mistakes with this structure.")
        practice = practice_bank.get(focus_key, "Rewrite the sentence using the target structure.")

        # ---------------------------------------------------------------------
        # Build grammar block
        # ---------------------------------------------------------------------
        grammar_block = (
            "\n\n[Grammar Focus]\n"
            f"- Target structure: {focus}\n"
            f"- Example (topic: {topic_clean}): {example}\n"
            f"- Common learner error: {error}\n"
            f"- Controlled practice: {practice}\n"
        )

        enriched = dict(section)
        enriched["content"] = content + grammar_block
        return enriched
