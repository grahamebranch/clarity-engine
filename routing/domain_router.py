"""
DomainRouter — determines topic, level, and domain from a user request.
Deterministic, no AI calls.
"""

from typing import Dict


class DomainRouter:
    """
    Very simple deterministic router.
    """

    def route(self, user_request: str) -> Dict[str, str]:
        """
        Returns a routing object:
        {
            "topic": str,
            "level": str,
            "domain": str
        }
        """

        cleaned = user_request.strip() if user_request else ""

        # Default deterministic routing
        return {
            "topic": cleaned if cleaned else "General English",
            "level": "B1",
            "domain": "general",
        }
