"""
Cultural Enricher — injects cultural notes, contrasts, and sensitivities.
Deterministic, production‑safe version with real cultural insights.
"""

from typing import List, Dict
from .cultural_profile import CulturalProfile


class CulturalEnricher:
    def __init__(self) -> None:
        self.profile = CulturalProfile()

    def apply(self, sections: List[Dict[str, str]], level: str, topic: str) -> List[Dict[str, str]]:
        """
        Enrich each section with cultural notes based on level.
        """
        profile = self.profile.get_profile(level)
        enriched = []

        for s in sections:
            enriched.append(self._enrich_section(s, profile, topic))

        return enriched

    def _enrich_section(self, section: Dict[str, str], profile: Dict[str, int], topic: str) -> Dict[str, str]:
        """
        Adds cultural blocks to each section.
        Replaces placeholder text with real cultural insights.
        """

        content = section.get("content", "")
        notes_count = profile["notes"]
        topic_clean = topic.strip() if topic else "the topic"

        # ---------------------------------------------------------------------
        # REAL CULTURAL INSIGHTS (deterministic)
        # ---------------------------------------------------------------------

        cultural_bank = [
            f"In many countries, people plan trips around public holidays, while others prefer spontaneous weekend travel.",
            f"Attitudes toward travel vary: some cultures value detailed itineraries, while others prefer flexible, unstructured trips.",
            f"Food is often a major part of travel culture — many travellers choose destinations based on local cuisine.",
            f"Some cultures prioritise budget travel and hostels, while others prefer comfort and private accommodation.",
            f"Travel etiquette differs globally — for example, tipping customs, queueing behaviour, and expectations around punctuality.",
            f"Environmental awareness affects travel choices: some regions promote sustainable tourism more actively than others.",
            f"Solo travel is common in some cultures but less typical in others, where group or family travel is the norm.",
        ]

        # Select the number of notes requested by the profile
        selected_notes = cultural_bank[:notes_count]

        # ---------------------------------------------------------------------
        # Build block
        # ---------------------------------------------------------------------
        cultural_block = ["\n\n[Cultural Notes]"]
        for note in selected_notes:
            cultural_block.append(f"- {note}")

        enriched = dict(section)
        enriched["content"] = content + "\n".join(cultural_block)
        return enriched
