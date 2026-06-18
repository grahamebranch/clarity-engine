"""
DIS5 - Semantic Section Detector
Rules:
1. Topic shift markers
2. Semantic density shift
3. Semantic similarity boundary
4. Semantic cohesion window (3-sentence rolling window)

Adds metadata:
- length
- avg_sentence_length
- keywords
- density
- cohesion_score
"""

import re

class DIS5SectionDetector:
    def run(self, data: dict) -> dict:
        units = data.get("semantic_units", [])

        # Rule 1: Topic-shift markers
        topic_markers = [
            "however", "but", "on the other hand",
            "in contrast", "meanwhile", "alternatively",
            "next", "moving on", "another point",
            "importantly", "crucially"
        ]

        sections = []
        current = {"id": "sec_1", "units": []}
        counter = 1

        prev_len = None
        prev_keywords = set()
        density_threshold = 1.6  # 60% increase

        cohesion_window = []

        for u in units:
            text = u["text"]
            lower = text.lower()
            length = len(text)

            # Extract simple keywords
            keywords = set(re.findall(r"[a-zA-Z]+", lower))

            start_new = False

            # Rule 1: Topic shift
            if any(lower.startswith(marker) for marker in topic_markers):
                start_new = True

            # Rule 2: Density shift
            if prev_len and length > prev_len * density_threshold:
                start_new = True

            # Rule 3: Semantic similarity boundary
            if prev_keywords:
                overlap = len(keywords & prev_keywords)
                if overlap == 0:
                    start_new = True

            # Rule 4: Semantic cohesion window
            if cohesion_window:
                window_overlap = sum(len(keywords & kw) for kw in cohesion_window)
                if window_overlap == 0:
                    start_new = True

            # Start new section
            if start_new:
                if current["units"]:
                    sections.append(self._add_metadata(current))
                counter += 1
                current = {"id": f"sec_{counter}", "units": []}
                cohesion_window = []

            # Add unit
            current["units"].append(u)

            # Update trackers
            prev_len = length
            prev_keywords = keywords

            cohesion_window.append(keywords)
            if len(cohesion_window) > 3:
                cohesion_window.pop(0)

        # Final section
        if current["units"]:
            sections.append(self._add_metadata(current))

        return {
            "stage": "DIS5",
            "sections": sections
        }

    # ------------------------------------------------------------
    # Metadata builder
    # ------------------------------------------------------------
    def _add_metadata(self, section: dict) -> dict:
        units = section["units"]

        # Length
        length = len(units)

        # Average sentence length
        avg_len = sum(len(u["text"]) for u in units) / length

        # Keywords
        all_keywords = set()
        for u in units:
            all_keywords |= set(re.findall(r"[a-zA-Z]+", u["text"].lower()))

        # Density = avg sentence length
        density = avg_len

        # Cohesion score = average keyword overlap between consecutive units
        overlaps = []
        prev_kw = None
        for u in units:
            kw = set(re.findall(r"[a-zA-Z]+", u["text"].lower()))
            if prev_kw:
                overlaps.append(len(kw & prev_kw))
            prev_kw = kw

        cohesion_score = sum(overlaps) / len(overlaps) if overlaps else 0

        # Attach metadata
        section["metadata"] = {
            "length": length,
            "avg_sentence_length": avg_len,
            "keywords": sorted(list(all_keywords)),
            "density": density,
            "cohesion_score": cohesion_score
        }

        return section
