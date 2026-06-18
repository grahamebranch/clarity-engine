"""
Edition Router — determines which editions should be generated
based on the user's input text.

Supported editions:
- student_core
- student_plus
- trainer_lite
- trainer
"""

from typing import List


class EditionRouter:
    def route(self, text: str) -> List[str]:
        """
        Returns a list of editions to generate.
        """

        t = text.lower()

        # --- TRAINER PRO ---
        # Strong signals for full methodology
        if any(k in t for k in ["trainer", "teacher", "methodology", "pedagogy", "celta", "delta"]):
            return ["trainer"]

        # --- TRAINER LITE ---
        # Signals for teachers without formal training
        if any(k in t for k in ["tutor", "conversation coach", "language helper", "teach english", "help me teach"]):
            return ["trainer_lite"]

        # --- STUDENT PLUS ---
        # Signals for learners who want enrichment but not methodology
        if any(k in t for k in ["student plus", "extra help", "explain more", "give me everything", "self study", "self-learning"]):
            return ["student_plus"]

        # --- STUDENT CORE (default) ---
        return ["student_core"]
