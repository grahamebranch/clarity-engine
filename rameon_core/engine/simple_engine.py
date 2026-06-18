"""
SimpleEngine — FastPath Version with Routing + Lessons + Formatting + Tracing
"""

from .tracing import TraceCollector

# Domain Routing Layer
from .routing.domain_router import DomainRouter

# Lesson Generator Core
from .lesson.lesson_generator import LessonGenerator

# DIS pipeline
from .dis1_detect_structure import DIS1DetectStructure
from .dis2_structure_detector import DIS2StructureDetector
from .dis3_block_detector import DIS3BlockDetector
from .dis4_semantic_unit_detector import DIS4SemanticUnitDetector
from .dis5_section_detector import DIS5SectionDetector

# EL pipeline
from .el2_clarity_reorder import EL2ClarityReorder
from .el3_expression_shaping import EL3ExpressionShaping
from .el4_semantic_fusion import EL4SemanticFusion
from .el5_output_composer import EL5OutputComposer
from .el6_final_polish import EL6FinalPolish
from .el7_packaging import EL7Packaging
from .el8_validation import EL8Validation
from .el9_export import EL9Export
from .el10_diagnostics import EL10Diagnostics

# Scoring
from .clarity_scorer import score_sections

# Output Formatting Layer
from .output_formatting import output_formatting


class SimpleEngine:
    def run(self, text: str) -> dict:
        trace = TraceCollector()

        # ============================================================
        # Domain Routing Layer
        # ============================================================
        router = DomainRouter()
        mode = router.route(text)
        data = {"text": text, "mode": mode}
        trace.add("ROUTER", data)

        # ============================================================
        # Lesson Generator Core (only activates if mode == "lesson")
        # ============================================================
        lesson_gen = LessonGenerator()
        data = lesson_gen.run(data)
        trace.add("LESSON", {
            "mode": data.get("mode"),
            "lesson_type": data.get("lesson_type", None)
        })

        # ============================================================
        # DIS Pipeline
        # ============================================================
        data = DIS1DetectStructure().run(data); trace.add("DIS1", data)
        data = DIS2StructureDetector().run(data); trace.add("DIS2", data)
        data = DIS3BlockDetector().run(data); trace.add("DIS3", data)
        data = DIS4SemanticUnitDetector().run(data); trace.add("DIS4", data)
        data = DIS5SectionDetector().run(data); trace.add("DIS5", data)

        # ============================================================
        # EL Pipeline
        # ============================================================
        data = EL2ClarityReorder().run(data); trace.add("EL2", data)
        data = EL3ExpressionShaping().run(data); trace.add("EL3", data)
        data = EL4SemanticFusion().run(data); trace.add("EL4", data)
        data = EL5OutputComposer().run(data); trace.add("EL5", data)
        data = EL6FinalPolish().run(data); trace.add("EL6", data)
        data = EL7Packaging().run(data); trace.add("EL7", data)
        data = EL8Validation().run(data); trace.add("EL8", data)
        data = EL9Export().run(data); trace.add("EL9", data)
        data = EL10Diagnostics().run(data); trace.add("EL10", data)

        # ============================================================
        # Scoring
        # ============================================================
        data["quality"] = score_sections(data.get("sections", []))

        # ============================================================
        # Output Formatting Layer
        # ============================================================
        data["text"] = output_formatting(data.get("text", ""))

        # ============================================================
        # Return Final Output
        # ============================================================
        return {
            "text": data.get("text", ""),
            "sections": data.get("sections", []),
            "trace": trace.export(),
            "quality": data.get("quality", {}),
            "diagnostics": data.get("diagnostics", {})
        }
