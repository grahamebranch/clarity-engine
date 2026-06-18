"""
EL8 - Validation & Sanity Checks (FastPath Version)
Ensures structural integrity of the final output.
"""

import re

class EL8Validation:
    def run(self, data: dict) -> dict:
        text = data.get("text", "")
        sections = data.get("sections", [])

        validated_sections = []
        seen_section_ids = set()

        for sec in sections:
            sid = sec.get("id")

            # 1. Section ID must exist
            if not sid:
                continue

            # 2. Section ID must be unique
            if sid in seen_section_ids:
                continue
            seen_section_ids.add(sid)

            units = sec.get("units", [])
            validated_units = []
            seen_unit_ids = set()

            for u in units:
                uid = u.get("id")

                # 3. Unit ID must exist
                if not uid:
                    continue

                # 4. Unit ID must be unique within section
                if uid in seen_unit_ids:
                    continue
                seen_unit_ids.add(uid)

                text_u = u.get("text", "").strip()

                # 5. Unit text must not be empty
                if not text_u:
                    continue

                # 6. Role must be valid
                role = u.get("role", "content")
                if role not in ("content", "transition"):
                    role = "content"

                # 7. Bullet formatting sanity
                if text_u.startswith(("-", "*", "•")):
                    # Ensure space after bullet marker
                    text_u = re.sub(r"^([-*•])(?=\S)", r"\1 ", text_u)

                validated_units.append({
                    **u,
                    "text": text_u,
                    "role": role
                })

            # 8. Section must have at least one valid unit
            if not validated_units:
                continue

            validated_sections.append({
                **sec,
                "units": validated_units
            })

        # 9. Final text must not be empty
        final_text = text.strip()

        return {
            "stage": "EL8",
            "text": final_text,
            "sections": validated_sections
        }
