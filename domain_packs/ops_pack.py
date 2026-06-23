# ops_pack.py — FastPath Whole-File Replacement
# Clarity Companion — Domain Pack: Ops (v1)

from typing import List, Dict

class OpsPack:
    """
    Domain Pack: Ops
    Provides operational clarity: workflows, processes, execution steps,
    and systems thinking for practical, real-world application.
    """

    def __init__(self):
        self.domain_name = "ops"
        self.version = "1.0"

    # ---------------------------------------------------------
    # SECTION TEMPLATES
    # ---------------------------------------------------------
    def get_sections(self, topic: str) -> List[Dict]:
        """
        Defines the structure of an operations-style lesson.
        Focused on clarity, repeatability, and execution.
        """
        return [
            {
                "title": f"Operational Overview: {topic}",
                "content": (
                    f"This section explains '{topic}' from an operational perspective. "
                    f"We outline what it is, where it fits, and why it matters for execution."
                )
            },
            {
                "title": "Inputs & Preconditions",
                "content": (
                    f"Here we identify what must be true before '{topic}' can be executed. "
                    f"These include resources, constraints, dependencies, and required context."
                )
            },
            {
                "title": "Process Flow",
                "content": (
                    f"This section breaks '{topic}' into a clear, repeatable workflow. "
                    f"Each step is designed to be actionable and unambiguous."
                )
            },
            {
                "title": "Failure Modes & Risks",
                "content": (
                    f"We highlight the most common failure points when executing '{topic}'. "
                    f"This helps anticipate issues and build resilience into the process."
                )
            },
            {
                "title": "Operational Checklist",
                "content": (
                    f"A concise checklist summarizing the essential steps and safeguards "
                    f"for executing '{topic}' reliably."
                )
            }
        ]

    # ---------------------------------------------------------
    # TONE RULES
    # ---------------------------------------------------------
    def get_tone(self) -> str:
        """
        Ops pack uses a structured, procedural tone.
        """
        return "procedural"

    # ---------------------------------------------------------
    # METADATA
    # ---------------------------------------------------------
    def get_metadata(self) -> Dict:
        return {
            "domain": self.domain_name,
            "version": self.version
        }

    # ---------------------------------------------------------
    # MAIN ENTRY POINT
    # ---------------------------------------------------------
    def generate(self, topic: str) -> Dict:
        """
        Main method called by the engine.
        Returns a structured lesson dictionary.
        """
        return {
            "engine_version": "1.0",
            "domain": self.domain_name,
            "tone": self.get_tone(),
            "sections": self.get_sections(topic)
        }
