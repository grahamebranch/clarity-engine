# lesson_composer.py — FastPath Whole-File Replacement
# Clarity Companion — Lesson Composer (v1)

from typing import Dict, Any

class LessonComposer:
    """
    Lesson Composer
    Orchestrates domain packs, structure packs, template packs, and flow packs
    to produce a fully rendered lesson before edition transforms are applied.
    """

    def __init__(self, edition_engine):
        self.version = "1.0"
        self.edition_engine = edition_engine

    # ---------------------------------------------------------
    # CORE PIPELINE
    # ---------------------------------------------------------
    def compose(self,
                topic: str,
                domain_pack,
                structure_pack,
                template_pack,
                flow_pack,
                edition: str = None) -> Dict[str, Any]:
        """
        Composes a full lesson from all components.
        Returns both the raw sections and the final edition.
        """

        # 1. Get the conceptual content from the domain pack
        domain_sections = domain_pack.generate(topic)

        # 2. Get the structural layout from the structure pack
        structure = structure_pack.structure()

        # 3. Render each section using the template pack
        rendered_sections = {}
        for section_role in structure:
            payload = domain_sections.get(section_role, {})
            rendered_sections[section_role] = template_pack.render(section_role, payload)

        # 4. Apply flow ordering
        ordered_sections = flow_pack.order(rendered_sections)

        # 5. Combine into a single text block
        combined_text = "\n\n".join(ordered_sections.values())

        # 6. Apply edition (optional)
        if edition:
            final_text = self.edition_engine.apply(edition, combined_text)
        else:
            final_text = combined_text

        return {
            "topic": topic,
            "sections": ordered_sections,
            "final": final_text
        }
