"""
Teaching Domain Pack - v1.0

Defines the rules, flows, templates, constraints, and annex logic
for conversation-led ESL teaching outputs.
"""

def get_domain():
    return {
        "name": "teaching",

        # -----------------------------------------------------
        # FLOWS: How the engine should behave in this domain
        # -----------------------------------------------------
        "flows": {
            "conversation-led": "Guide the learner through natural dialogue.",
            "scaffold": "Break tasks into simple, progressive steps.",
            "correct-gently": "Correct errors without interrupting flow.",
        },

        # -----------------------------------------------------
        # TEMPLATES: Reusable content patterns
        # -----------------------------------------------------
        "templates": {
            "lesson_intro": "Today we're exploring: {topic}",
            "prompt": "Try answering this: {question}",
            "feedback": "Good attempt! Here's a clearer version: {correction}",
        },

        # -----------------------------------------------------
        # CONSTRAINTS: Hard rules the engine must obey
        # -----------------------------------------------------
        "constraints": {
            "max_turn_length": 120,
            "avoid_jargon": True,
            "tone": "supportive",
        },

        # -----------------------------------------------------
        # ANNEX RULES: Extra logic for special cases
        # -----------------------------------------------------
        "annex_rules": {
            "beginner_mode": "Use simpler vocabulary and shorter sentences.",
            "advanced_mode": "Encourage nuance, detail, and self-correction.",
        },
    }
