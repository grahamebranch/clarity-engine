"""
EL2 - Clarity Reorder
Reorders sections based on clarity-related metadata.

Inputs (from DIS5):
- length
- avg_sentence_length
- keywords
- density
- cohesion_score

Outputs:
- reordered sections
- clarity scores for trace
"""

class EL2ClarityReorder:
    def run(self, data: dict) -> dict:
        sections = data.get("sections", [])

        # Score each section
        for sec in sections:
            meta = sec.get("metadata", {})

            length = meta.get("length", 1)
            avg_len = meta.get("avg_sentence_length", 1)
            density = meta.get("density", 1)
            cohesion = meta.get("cohesion_score", 0)

            # Clarity scoring formula (explainable, non-ML)
            # Higher cohesion = clearer
            # Lower density = clearer
            # Shorter sentences = clearer
            # Moderate length = clearer (not too short, not too long)

            clarity_score = (
                (cohesion * 2.0)        # cohesion is the strongest clarity signal
                - (density * 0.8)       # dense sections are harder to read
                - (avg_len * 0.5)       # long sentences reduce clarity
                - (abs(length - 3) * 0.3)  # ideal section length ≈ 3 units
            )

            sec["clarity_score"] = clarity_score

        # Sort sections by clarity score (descending)
        sections = sorted(sections, key=lambda s: s.get("clarity_score", 0), reverse=True)

        # Return updated data
        return {
            "stage": "EL2",
            "sections": sections
        }
