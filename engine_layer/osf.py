""""
OSF (Output Structure Framework) - v1.1

This module defines the structural skeleton for all outputs.
It ensures that every output follows a predictable, domain-specific structure.
"""

class OSF:
    def __init__(self):
        # Structure registry (populated later)
        self.structures = {}

    def register_structure(self, domain_name: str, edition: str, structure: dict):
        """Register an OSF structure for a given domain + edition."""
        key = f"{domain_name}:{edition}"
        self.structures[key] = structure

    def load_structure(self, domain_name: str, edition: str) -> dict:
        """Return the OSF structure for a given domain + edition."""
        key = f"{domain_name}:{edition}"
        if key not in self.structures:
            raise ValueError(f"Unknown structure for domain/edition: {key}")
        return self.structures[key]

    def apply_structure(self, instruction_set: dict, structure: dict) -> dict:
        """
        Shape the output according to the OSF skeleton.
        This is the first functional version (OSF-1).
        """

        shaped_output = {
            "version": "OSF-1",
            "domain": instruction_set.get("domain"),
            "request": instruction_set.get("request"),
            "structure": structure,
            "flows": instruction_set.get("flows", {}),
            "templates": instruction_set.get("templates", {}),
            "constraints": instruction_set.get("constraints", {}),
            "annex_rules": instruction_set.get("annex_rules", {}),
        }

        return shaped_output
