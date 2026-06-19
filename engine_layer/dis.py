"""
DIS (Domain Instruction Set) - v1.1

This module defines the DIS interpreter layer.
It loads domain rules, flows, templates, and constraints,
and produces a deterministic instruction set for the Rameon engine.
"""

class DIS:
    def __init__(self):
        # Domain registry (populated later)
        self.domains = {}

    def register_domain(self, name: str, rules: dict):
        """Register a domain pack (rules, flows, templates, constraints)."""
        self.domains[name] = rules

    def load_domain(self, domain_name: str) -> dict:
        """Return the domain rule set."""
        if domain_name not in self.domains:
            raise ValueError(f"Unknown domain: {domain_name}")
        return self.domains[domain_name]

    def interpret(self, user_request: str, domain_rules: dict) -> dict:
        """
        Convert domain rules + user request into a DIS instruction set.
        This is the first functional version (DIS-1).
        """
        flows = domain_rules.get("flows", {})
        templates = domain_rules.get("templates", {})
        constraints = domain_rules.get("constraints", {})
        annex_rules = domain_rules.get("annex_rules", {})

        instruction_set = {
            "version": "DIS-1",
            "request": user_request,
            "domain": domain_rules.get("name"),
            "flows": flows,
            "templates": templates,
            "constraints": constraints,
            "annex_rules": annex_rules,
        }

        return instruction_set

    # ------------------------------------------------------------
    # Temporary shim for pipeline compatibility
    # ------------------------------------------------------------
    def apply(self, text: str) -> str:
        """Temporary no-op pass-through for MVP pipeline."""
        return text
