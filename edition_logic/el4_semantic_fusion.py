"""
EL4 - Semantic Fusion
Merges adjacent sections when it improves clarity and flow.

Uses metadata from DIS5/EL2:
- cohesion_score
- keywords
- length
- avg_sentence_length
- density

Goals:
- Merge sections that are clearly about the same thing
- Keep distinct topics separate
- Add light, human-like transitions where needed
"""

import re

class EL4SemanticFusion:
    def run(self, data: dict) -> dict:
        sections = data.get("sections", [])

        if not sections:
            return {
                "stage": "EL4",
                "sections": []
            }

        fused = []
        current = sections[0]

        for nxt in sections[1:]:
            if self._should_merge(current, nxt):
                current = self._merge_sections(current, nxt)
            else:
                fused.append(current)
                current = nxt

        fused.append(current)

        return {
            "stage": "EL4",
            "sections": fused
        }

    # ------------------------------------------------------------
    # Decide whether to merge two sections
    # ------------------------------------------------------------
    def _should_merge(self, a: dict, b: dict) -> bool:
        meta_a = a.get("metadata", {})
        meta_b = b.get("metadata", {})

        kw_a = set(meta_a.get("keywords", []))
        kw_b = set(meta_b.get("keywords", []))
        keyword_overlap = len(kw_a & kw_b)

        coh_a = meta_a.get("cohesion_score", 0)
        coh_b = meta_b.get("cohesion_score", 0)

        dens_a = meta_a.get("density", 1)
        dens_b = meta_b.get("density", 1)

        # Rule 1: must share some keywords
        if keyword_overlap == 0:
            return False

        # Rule 2: cohesion shouldn't collapse
        if coh_a < -1 and coh_b < -1:
            return False

        # Rule 3: avoid merging if density mismatch is extreme
        if abs(dens_a - dens_b) > 80:
            return False

        return True

    # ------------------------------------------------------------
    # Merge two sections into one
    # ------------------------------------------------------------
    def _merge_sections(self, a: dict, b: dict) -> dict:
        merged = {
            "id": f"{a.get('id', 'sec')}+{b.get('id', 'sec')}",
            "units": [],
        }

        merged["units"] = (
            a.get("units", [])
            + self._maybe_add_transition(a, b)
            + b.get("units", [])
        )

        merged["metadata"] = self._rebuild_metadata(merged)

        return merged

    # ------------------------------------------------------------
    # Add a light transition between sections if needed
    # ------------------------------------------------------------
    def _maybe_add_transition(self, a: dict, b: dict) -> list:
        if not b.get("units"):
            return []

        first_text = b["units"][0]["text"].strip().lower()

        if first_text.startswith((
            "however", "but", "in contrast", "meanwhile", "next"
        )):
            return []

        transition_text = "Next, we can look at this from another angle:"
        return [{
            "text": transition_text,
            "role": "transition",
        }]

    # ------------------------------------------------------------
    # Rebuild metadata after fusion
    # ------------------------------------------------------------
    def _rebuild_metadata(self, section: dict) -> dict:
        units = section.get("units", [])

        if not units:
            return {
                "length": 0,
                "avg_sentence_length": 0,
                "keywords": [],
                "density": 0,
                "cohesion_score": 0,
            }

        length = len(units)
        avg_len = sum(len(u.get("text", "")) for u in units) / length

        all_keywords = set()
        for u in units:
            all_keywords |= set(re.findall(r"[a-zA-Z]+", u.get("text", "").lower()))

        density = avg_len

        overlaps = []
        prev_kw = None
        for u in units:
            kw = set(re.findall(r"[a-zA-Z]+", u.get("text", "").lower()))
            if prev_kw is not None:
                overlaps.append(len(kw & prev_kw))
            prev_kw = kw

        cohesion_score = sum(overlaps) / len(overlaps) if overlaps else 0

        return {
            "length": length,
            "avg_sentence_length": avg_len,
            "keywords": sorted(list(all_keywords)),
            "density": density,
            "cohesion_score": cohesion_score,
        }
