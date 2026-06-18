"""
Vocabulary Enricher — injects lexical richness into lesson sections.
Deterministic, production‑safe version with real lexical items.
"""

from typing import List, Dict
from .vocab_profile import VocabularyProfile


class VocabularyEnricher:
    def __init__(self) -> None:
        self.profile = VocabularyProfile()

    def apply(self, sections: List[Dict[str, str]], level: str, topic: str) -> List[Dict[str, str]]:
        """
        Enrich each section with lexical items based on level profile.
        """
        profile = self.profile.get_profile(level)
        enriched = []

        for s in sections:
            enriched.append(self._enrich_section(s, profile, topic))

        return enriched

    def _enrich_section(self, section: Dict[str, str], profile: Dict[str, int], topic: str) -> Dict[str, str]:
        """
        Deterministic enrichment: adds lexical blocks at the end of each section.
        Replaces placeholders with real lexical content.
        """

        content = section.get("content", "")
        topic_clean = topic.strip() if topic else "the topic"

        lex = []

        # -----------------------------
        # REAL LEXICAL CONTENT
        # -----------------------------

        # Synonyms
        synonyms_bank = [
            "talk about",
            "discuss",
            "explore",
            "focus on",
            "look at",
        ]
        if profile["synonyms"] > 0:
            selected = synonyms_bank[: profile["synonyms"]]
            lex.append(f"- Synonyms ({profile['synonyms']}): {', '.join(selected)}.")

        # Collocations
        collocations_bank = [
            "make travel plans",
            "book accommodation",
            "plan a trip",
            "check the schedule",
            "pack your bags",
            "catch a flight",
        ]
        if profile["collocations"] > 0:
            selected = collocations_bank[: profile["collocations"]]
            lex.append(f"- Collocations ({profile['collocations']}): {', '.join(selected)}.")

        # Idioms
        idioms_bank = [
            "hit the road",
            "off the beaten track",
            "travel light",
            "the world is your oyster",
        ]
        if profile["idioms"] > 0:
            selected = idioms_bank[: profile["idioms"]]
            lex.append(f"- Idioms ({profile['idioms']}): {', '.join(selected)}.")

        # Contrastive pairs
        contrast_pairs_bank = [
            ("plan ahead", "go with the flow"),
            ("budget trip", "luxury holiday"),
            ("crowded", "quiet"),
            ("flexible schedule", "fixed schedule"),
        ]
        if profile["contrast_pairs"] > 0:
            selected = contrast_pairs_bank[: profile["contrast_pairs"]]
            formatted = "; ".join([f"{a} ↔ {b}" for a, b in selected])
            lex.append(f"- Contrastive pairs ({profile['contrast_pairs']}): {formatted}.")

        # Stretch vocabulary
        stretch_bank = [
            "logistics",
            "itinerary",
            "accommodation options",
            "sustainable tourism",
            "cultural immersion",
        ]
        if profile["stretch_vocab"] > 0:
            selected = stretch_bank[: profile["stretch_vocab"]]
            lex.append(f"- Stretch vocabulary ({profile['stretch_vocab']}): {', '.join(selected)}.")

        # -----------------------------
        # Append to section
        # -----------------------------
        if lex:
            content += "\n\n[Lexical Enrichment]\n" + "\n".join(lex)

        enriched = dict(section)
        enriched["content"] = content
        return enriched
