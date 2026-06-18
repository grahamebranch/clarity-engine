"""
EL4 - Semantic Fusion (FastPath Version)
Deterministic merging of related units into coherent paragraphs.
"""

import re

class EL4SemanticFusion:
    def run(self, data: dict) -> dict:
        sections = data.get("sections", [])

        fused_sections = []
        for sec in sections:
            fused_units = self._fuse_units(sec.get("units", []))

            fused_sections.append({
                **sec,
                "units": fused_units
            })

        return {
            "stage": "EL4",
            "sections": fused_sections
        }

    # ------------------------------------------------------------
    # Core fusion logic
    # ------------------------------------------------------------
    def _fuse_units(self, units):
        if not units:
            return units

        fused = []
        buffer = []

        for u in units:
            text = u.get("text", "").strip()
            is_bullet = text.lstrip().startswith(("-", "*", "•"))
            is_transition = u.get("role") == "transition"

            # 1. Bullets never fuse
            if is_bullet:
                if buffer:
                    fused.append(self._flush_buffer(buffer))
                    buffer = []
                fused.append(u)
                continue

            # 2. Transitions never fuse
            if is_transition:
                if buffer:
                    fused.append(self._flush_buffer(buffer))
                    buffer = []
                fused.append(u)
                continue

            # 3. Narrative units → fuse if short
            if len(text) < 80:
                buffer.append(u)
            else:
                if buffer:
                    fused.append(self._flush_buffer(buffer))
                    buffer = []
                fused.append(u)

        # Flush remaining
        if buffer:
            fused.append(self._flush_buffer(buffer))

        return fused

    # ------------------------------------------------------------
    # Merge buffered units into one paragraph
    # ------------------------------------------------------------
    def _flush_buffer(self, buffer):
        merged_text = " ".join(u["text"] for u in buffer)
        base = buffer[0].copy()
        base["text"] = merged_text
        return base
