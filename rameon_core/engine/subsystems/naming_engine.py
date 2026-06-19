# naming_engine.py
# FastPath: Standalone naming engine for Clarity

class NamingEngine:

    def __init__(self):
        self.domain_map = {
            "teaching": "lesson",
            "self_reflection": "reflection",
            "coaching": "guidance",
            "training": "module",
            "project_planning": "plan",
            "operations": "manual",
            "strategy": "strategy",
            "process_design": "process",
            "analysis": "analysis",
            "communication": "message",
            "presentation": "deck",
            "speechwriting": "speech",
            "documentation": "guide",
            "policy": "policy",
            "reporting": "report",
            "instructions": "instructions",
            "brainstorming": "sketch",
            "storytelling": "story",
            "concept_dev": "concept",
            "journaling": "journal",
            "life_planning": "map",
            "decision_making": "choice"
        }

        self.format_map = {
            "summary": "summary",
            "outline": "outline",
            "notes": "notes",
            "checklist": "checklist",
            "script": "script",
            "report": "report",
            "brief": "brief",
            "proposal": "proposal",
            "email": "email",
            "message": "message",
            "announcement": "announcement",
            "guide": "guide",
            "instructions": "instructions",
            "walkthrough": "walkthrough",
            "story": "story",
            "concept": "concept",
            "sketch": "sketch"
        }

    def detect_domain(self, analysis):
        return analysis.get("domain")

    def detect_format(self, analysis):
        return analysis.get("format")

    def get_clarity_noun(self, analysis):
        domain = self.detect_domain(analysis)
        if domain and domain in self.domain_map:
            return "clarity " + self.domain_map[domain]

        fmt = self.detect_format(analysis)
        if fmt and fmt in self.format_map:
            return "clarity " + self.format_map[fmt]

        return "clarity work"
