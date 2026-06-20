from .trace import TraceCollector
from .sectioner import split_into_sections
from .quality import QualityScorer
from .diagnostics import DiagnosticsEngine
from .rewrite import RewriteEngine

class ClarityEngine:
    def __init__(self):
        self.trace = TraceCollector()
        self.quality = QualityScorer()
        self.diagnostics = DiagnosticsEngine()
        self.rewrite = RewriteEngine()

    def run(self, text):
        # Input
        self.trace.add("input_received", {
            "text": text,
            "sections": []
        })

        # Normalization
        normalized = text.strip()
        self.trace.add("normalization_complete", {
            "text": normalized,
            "sections": []
        })

        # Sectioning
        sections = split_into_sections(normalized)
        self.trace.add("sections_created", {
            "text": normalized,
            "sections": sections
        })

        # Quality scoring
        quality_result = self.quality.score(normalized, sections)
        self.trace.add("quality_scored", {
            "text": normalized,
            "sections": sections
        })

        # Diagnostics
        diagnostics_result = self.diagnostics.run(normalized, sections)
        self.trace.add("diagnostics_complete", {
            "text": normalized,
            "sections": sections
        })

        # Rewrite
        rewritten = self.rewrite.run(normalized, sections)
        self.trace.add("rewrite_complete", {
            "text": rewritten,
            "sections": sections
        })

        # Output = rewritten text
        output = rewritten
        self.trace.add("output_ready", {
            "text": output,
            "sections": sections
        })

        return {
            "output": output,
            "sections": sections,
            "trace": self.trace.export(),
            "quality": quality_result,
            "diagnostics": diagnostics_result
        }
