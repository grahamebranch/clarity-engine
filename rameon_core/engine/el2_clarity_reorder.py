"""
EL2 — Clarity Reorder (FastPath Version)
Reorders sections using clarity score, semantic weight, and structural role.
"""

class EL2ClarityReorder:
    def run(self, data: dict) -> dict:
        sections = data.get("sections", [])
        if not sections or len(sections) <= 2:
            return data

        # ----------------------------------------------------
        # 1. Identify structural roles
        # ----------------------------------------------------
        def role(sec):
            title = (sec.get("title") or "").lower()
            if any(k in title for k in ["intro", "introduction", "overview", "summary"]):
                return "intro"
            if any(k in title for k in ["conclusion", "closing", "wrap"]):
                return "outro"
            return "middle"

        # ----------------------------------------------------
        # 2. Extract clarity score (fallback = 50)
        # ----------------------------------------------------
        def clarity(sec):
            return sec.get("clarity_score", 50)

        # ----------------------------------------------------
        # 3. Extract semantic weight (based on length)
        # ----------------------------------------------------
        def semantic_weight(sec):
            blocks = sec.get("blocks", [])
            text = "\n".join(b.get("text", "") for b in blocks)
            return len(text)

        # ----------------------------------------------------
        # 4. Build sortable tuple
        # ----------------------------------------------------
        def sort_key(sec):
            r = role(sec)
            if r == "intro":
                return (0, -clarity(sec), -semantic_weight(sec))
            if r == "middle":
                return (1, -clarity(sec), -semantic_weight(sec))
            if r == "outro":
                return (2, -clarity(sec), -semantic_weight(sec))
            return (1, -clarity(sec), -semantic_weight(sec))

        # ----------------------------------------------------
        # 5. Sort sections
        # ----------------------------------------------------
        reordered = sorted(sections, key=sort_key)

        data["sections"] = reordered
        return data
