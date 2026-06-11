"""
Rameon Engine - v1.1

This module defines the Rameon execution layer.
It takes the DIS instruction set + OSF structure + domain rules
and produces an executed output object ready for governance.
"""

def _select_templates_for_sections(structure: dict, templates: dict, flow_logic: dict, instruction_set: dict) -> dict:
    """
    Deterministic template selector influenced by flow logic.
    Applies:
    - level-based template bias
    - mode-based section priority
    - fallback to first template
    """
    if not templates:
        return {}

    # Extract sections from structure
    sections = (
        structure.get("structure", {}).get("sections")
        or structure.get("sections")
        or []
    )

    # Extract flow parameters
    level = instruction_set.get("level", "intermediate")
    mode = instruction_set.get("mode", "conversation-led")

    level_rules = flow_logic.get("level_rules", {}).get(level, {})
    mode_rules = flow_logic.get("mode_rules", {}).get(mode, {})

    template_bias = level_rules.get("template_bias", {})
    priority_sections = mode_rules.get("priority_sections", [])

    selected = {}

    for section in sections:
        section_templates = templates.get(section)

        if not section_templates:
            selected[section] = None
            continue

        # If section is a priority, pick the first template
        if section in priority_sections:
            selected[section] = section_templates[0]
            continue

        # Apply level-based bias: pick the template with highest bias weight
        bias = template_bias.get(section, 0.5)

        # Deterministic weighted choice:
        # If bias >= 0.7 → pick first template
        # If bias < 0.7 → pick last template
        if bias >= 0.7:
            selected[section] = section_templates[0]
        else:
            selected[section] = section_templates[-1]

    return selected


def _realise_templates(selected: dict, instruction_set: dict) -> dict:
    """
    Turns template strings into real text by filling placeholders
    with simple deterministic values.
    """
    realised = {}

    # Simple deterministic fillers
    fillers = {
        "question": "What did you do last weekend?",
        "prompt": "Tell me about your Saturday.",
        "context": "We're talking about weekend activities.",
        "drill": "Repeat: 'On Saturday, I…'",
        "scenario": "Imagine you're telling a friend about your weekend.",
        "reflection_q": "What part of the weekend was most enjoyable?",
        "check_q": "Can you describe one activity you did?",
        "writing_task": "Write 3–4 sentences about your weekend.",
    }

    for section, template in selected.items():
        if not template:
            realised[section] = None
            continue

        text = template
        for key, value in fillers.items():
            text = text.replace(f"{{{key}}}", value)

        realised[section] = text

    return realised

def _format_lesson(realised: dict) -> str:
    lines = ["# Lesson: Talking About Your Weekend", ""]
    for section, text in realised.items():
        if text:
            title = section.replace("_", " ").title()
            lines.append(f"## {title}")
            lines.append(text)
            lines.append("")
    return "\n".join(lines)


class RameonEngine:
    def __init__(self):
        # Execution configuration or caches (populated later)
        self.config = {}

def execute(
    self,
    instruction_set: dict,
    structure: dict,
    domain_rules: dict,
    templates: dict = None,
    flow_logic: dict = None
) -> dict:
    """
    Execute the deterministic generation pipeline.
    RAMEON-1 + template selection + flow logic passthrough + realisation.
    """

    # Select templates per section (flow‑aware)
    selected_templates = _select_templates_for_sections(
        structure,
        templates or {},
        flow_logic or {},
        instruction_set
    )

    # NEW: Realise templates into actual text
    realised_sections = _realise_templates(selected_templates, instruction_set)

    # NEW: Format the full lesson
    formatted_lesson = _format_lesson(realised_sections)

    executed_output = {
        "version": "RAMEON-1",
        "domain": instruction_set.get("domain"),
        "request": instruction_set.get("request"),

        "structure": structure,
        "flows": instruction_set.get("flows", {}),
        "constraints": instruction_set.get("constraints", {}),
        "annex_rules": instruction_set.get("annex_rules", {}),
        "domain_rules": domain_rules,

        "templates_selected": selected_templates,
        "realised_sections": realised_sections,
        "formatted_lesson": formatted_lesson,
        "flow_logic": flow_logic,
    }

    return executed_output

