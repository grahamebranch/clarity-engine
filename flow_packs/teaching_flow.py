"""
Teaching Flow Logic Pack - v1.0

Defines how the engine selects templates and behaviours
based on learner level, mode, and constraints.
"""

def get_teaching_flow_logic():
    return {
        "version": "FLOW-TEACHING-1",

        # -----------------------------------------------------
        # Level-based behaviour
        # -----------------------------------------------------
        "level_rules": {
            "beginner": {
                "template_bias": {
                    "warmup": 0.9,
                    "presentation": 0.8,
                    "controlled_practice": 0.9,
                    "freer_practice": 0.4,
                    "reflection": 0.5,
                    "assessment": 0.7,
                    "homework": 0.6
                },
                "language_simplicity": "A1-A2 vocabulary, short sentences"
            },

            "intermediate": {
                "template_bias": {
                    "warmup": 0.7,
                    "presentation": 0.7,
                    "controlled_practice": 0.8,
                    "freer_practice": 0.7,
                    "reflection": 0.7,
                    "assessment": 0.8,
                    "homework": 0.7
                },
                "language_simplicity": "B1-B2 vocabulary, moderate complexity"
            },

            "advanced": {
                "template_bias": {
                    "warmup": 0.5,
                    "presentation": 0.6,
                    "controlled_practice": 0.6,
                    "freer_practice": 0.9,
                    "reflection": 0.9,
                    "assessment": 0.9,
                    "homework": 0.8
                },
                "language_simplicity": "C1-C2 vocabulary, full complexity"
            }
        },

        # -----------------------------------------------------
        # Mode-based behaviour
        # -----------------------------------------------------
        "mode_rules": {
            "conversation-led": {
                "priority_sections": ["warmup", "freer_practice", "reflection"],
                "correction_style": "gentle"
            },
            "scaffold": {
                "priority_sections": ["presentation", "controlled_practice"],
                "correction_style": "explicit"
            },
            "correct-gently": {
                "priority_sections": ["controlled_practice", "freer_practice"],
                "correction_style": "soft-recast"
            }
        },

        # -----------------------------------------------------
        # Constraint-based behaviour
        # -----------------------------------------------------
        "constraint_rules": {
            "max_turn_length": {
                "short": 80,
                "medium": 150,
                "long": 250
            },
            "tone": {
                "supportive": "Use warm, encouraging language.",
                "neutral": "Use clear, direct language.",
                "formal": "Use precise, professional language."
            }
        }
    }
