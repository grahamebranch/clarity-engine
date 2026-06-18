class GuidanceRouter:
    from typing import List

    def should_apply(self, editions: List[str], domain: str) -> bool:
        """
        Determines if guidance should be applied for a given domain.
        """

        # Editions that receive guidance
        edition_ok = any(e in editions for e in [
            "student_plus", "trainer_lite", "trainer"
        ])

        # Domains that support guidance
        domain_ok = domain in [
            "lesson",
            "onboarding",
            "self_learning",
            "writing",
            "assessment",
            "conversation",
            "ops"
        ]

        return edition_ok and domain_ok
