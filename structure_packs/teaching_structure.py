"""
Teaching OSF Structure Pack - v1.0

Defines the structural skeleton for teaching outputs.
This is the domain-specific shape that OSF applies.
"""

def get_teaching_structure():
    return {
        "version": "OSF-TEACHING-1",

        # -----------------------------------------------------
        # High-level lesson flow
        # -----------------------------------------------------
        "sections": [
            "warmup",
            "presentation",
            "controlled_practice",
            "freer_practice",
            "reflection",
            "assessment",
            "homework"
        ],

        # -----------------------------------------------------
        # Section metadata (optional but useful later)
        # -----------------------------------------------------
        "metadata": {
            "warmup": {
                "goal": "Activate schema and get the learner speaking.",
                "typical_time": 5
            },
            "presentation": {
                "goal": "Introduce target language or topic context.",
                "typical_time": 8
            },
            "controlled_practice": {
                "goal": "Guide the learner through structured tasks.",
                "typical_time": 10
            },
            "freer_practice": {
                "goal": "Encourage natural, open-ended communication.",
                "typical_time": 10
            },
            "reflection": {
                "goal": "Help the learner notice progress and gaps.",
                "typical_time": 3
            },
            "assessment": {
                "goal": "Check understanding and performance.",
                "typical_time": 4
            },
            "homework": {
                "goal": "Extend learning beyond the session.",
                "typical_time": 2
            }
        }
    }
