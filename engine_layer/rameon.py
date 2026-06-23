"""
RameonEngine - v3.0

Purpose:
- Full deterministic pipeline with rewrite, finishing, scoring, trace, and diagnostics
- Returns (final_text, clarity_metadata, trace_metadata, diagnostics_metadata)
"""

from engine_layer.osf import OSFShaping
from engine_layer.el3 import EL3Deterministic
from engine_layer.el4 import EL4Deterministic
from engine_layer.el5 import EL5Rewrite
from engine_layer.el6 import EL6Rewrite
from engine_layer.el7 import EL7Deterministic
from engine_layer.el8 import EL8Deterministic
from engine_layer.el9 import EL9Deterministic
from engine_layer.el10 import EL10Deterministic
from engine_layer.el11 import EL11Clarity
from engine_layer.el12 import EL12Trace
from engine_layer.el13 import EL13Diagnostics
from engine_layer.governance import GovernanceLayer
from engine_layer.final_output import FinalOutputLayer


class RameonEngine:
    def __init__(self):
        # Core layers
        self.osf = OSFShaping()
        self.el3 = EL3Deterministic()
        self.el4 = EL4Deterministic()
        self.el5 = EL5Rewrite()

        # Finishing stack
        self.el6 = EL6Rewrite()
        self.el7 = EL7Deterministic()
        self.el8 = EL8Deterministic()
        self.el9 = EL9Deterministic()
        self.el10 = EL10Deterministic()

        # Scoring + introspection
        self.el11 = EL11Clarity()
        self.trace = EL12Trace()
        self.el13 = EL13Diagnostics()

        # Final layers
        self.gov = GovernanceLayer()
        self.final = FinalOutputLayer()

    def process(self, text: str):
        """
        Returns:
            final_text, clarity_metadata, trace_metadata, diagnostics_metadata
        """

        def run(layer_name, func, current_text):
            before = current_text
            after = func(current_text)
            self.trace.record(layer_name, before, after)
            return after

        # Pipeline with trace
        text = run("OSF", self.osf.osf, text)
        text = run("EL3", self.el3.el3, text)
        text = run("EL4", self.el4.el4, text)
        text = run("EL5", self.el5.el5, text)
        text = run("EL6", self.el6.el6, text)
        text = run("EL7", self.el7.el7, text)
        text = run("EL8", self.el8.el8, text)
        text = run("EL9", self.el9.el9, text)
        text = run("EL10", self.el10.el10, text)

        # Scoring
        clarity = self.el11.el11(text)

        # Governance + final output
        text = run("Governance", self.gov.governance, text)
        text = run("FinalOutput", self.final.final_output, text)

        # Diagnostics (not traced)
        diagnostics = self.el13.el13(text, clarity)

        return text, clarity, self.trace.get_trace(), diagnostics
