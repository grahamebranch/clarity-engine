import re
import math   # ← ADD THIS LINE

from .engine import Engine
from .context import EngineContext
from .pipeline import Pipeline



class SimpleEngine(Engine):
    class SimpleEngine(Engine):

        def __init__(self):
            # ------------------------------------------------------------
            # REAL MVP PIPELINE
            # ------------------------------------------------------------
            from structure_packs.dis2_structure_detector import DIS2StructureDetector
            from structure_packs.dis3_block_detector import DIS3BlockDetector
            from structure_packs.dis4_semantic_unit_detector import DIS4SemanticUnitDetector

            from edition_logic.el2_clarity_reorder import EL2ClarityReorder
            from edition_logic.el3_expression_shaping import EL3ExpressionShaping
            from edition_logic.el4_semantic_fusion import EL4SemanticFusion

            self.pipeline = Pipeline(
                stages=[
                    DIS2StructureDetector(),     # 1. detect structure
                    DIS3BlockDetector(),         # 2. detect blocks
                    DIS4SemanticUnitDetector(),  # 3. detect semantic units
                    EL2ClarityReorder(),         # 4. reorder by clarity
                    EL4SemanticFusion(),         # 5. merge meaning
                    EL3ExpressionShaping(),      # 6. edition logic
                ]
            )

            self.config: dict = {}
            self.debug = False


    # ------------------------------------------------------------
    # 1. Load configuration
    # ------------------------------------------------------------
    def load(self, config: dict | None = None):
        self.config = config or {}

    def shutdown(self):
        pass

    # ------------------------------------------------------------
    # 2. Early normalization
    # ------------------------------------------------------------
    def normalize_headings(self, text: str) -> str:
        lines = [line.rstrip() for line in text.splitlines()]
        return "\n".join(lines)

    def group_bullets(self, text: str) -> str:
        return text

    # ------------------------------------------------------------
    # 2b. Heading detection + section splitting
    # ------------------------------------------------------------
    def is_heading(self, line: str) -> bool:
        if not isinstance(line, str):
            return False

        text = line.strip()
        if not text:
            return False

        if text.startswith(("-", "*", "•")):
            return False

        if re.match(r".*\b\d+$", text):
            return False

        if not re.match(r"^[A-Za-z0-9]", text):
            return False

        if text.endswith("."):
            return False

        return True

    def split_into_sections(self, text: str) -> list[dict]:
        sections = []
        current = {"heading": None, "raw_lines": []}

        for line in text.splitlines():
            stripped = line.strip()

            if self.is_heading(stripped):
                if current["heading"] is not None or current["raw_lines"]:
                    sections.append(current)
                current = {"heading": stripped, "raw_lines": []}
            else:
                current["raw_lines"].append(line)

        if current["heading"] is not None or current["raw_lines"]:
            sections.append(current)

        return sections

    # ------------------------------------------------------------
    # 3. Block detection (paragraphs + bullets)
    # ------------------------------------------------------------
    def detect_blocks(self, text: str) -> list[dict]:
        blocks = []
        current = []

        for line in text.splitlines():
            stripped = line.strip()

            if not stripped:
                if current:
                    blocks.append("\n".join(current))
                    current = []
                continue

            current.append(stripped)

        if current:
            blocks.append("\n".join(current))

        out = []
        for b in blocks:
            if b.startswith(("-", "*", "•")):
                block_type = "bullet"
            else:
                block_type = "paragraph"

            out.append(
                {
                    "type": block_type,
                    "content": b,
                    "block_type": block_type,
                }
            )
        return out

    # ------------------------------------------------------------
    # 4. Chunking (groups blocks into chunks)
    # ------------------------------------------------------------
    def chunk_blocks(self, blocks: list[dict]) -> list[dict]:
        chunks = []
        for b in blocks:
            chunks.append(
                {
                    "content": b["content"],
                    "block_type": b["block_type"],
                    "heading": b.get("heading"),
                    "intent": None,
                    "clarity_score": None,
                }
            )
        return chunks

    # ------------------------------------------------------------
    # 5. Intent detection
    # ------------------------------------------------------------
    def detect_intents(self, chunks: list[dict]) -> list[dict]:
        for c in chunks:
            c["intent"] = "statement"
        return chunks

    # ------------------------------------------------------------
    # 6. Clarity scoring
    # ------------------------------------------------------------
    def score_clarity(self, chunks: list[dict]) -> list[dict]:
        for c in chunks:
            c["clarity_score"] = 60
        return chunks

    # ------------------------------------------------------------
    # 7. DIS-1 assembly
    # ------------------------------------------------------------
    def assemble_output(self, chunks: list[dict]) -> dict:
        sections = []
        current = None

        for ch in chunks:
            heading = ch.get("heading")

            if current is None or current["heading"] != heading:
                current = {"heading": heading, "blocks": []}
                sections.append(current)

            current["blocks"].append(
                {
                    "content": ch["content"],
                    "block_type": ch["block_type"],
                    "intent": ch["intent"],
                    "clarity_score": ch["clarity_score"],
                }
            )

        return {
            "version": "DIS-1",
            "sections": sections,
            "meta": {
                "source_version": "DIS-1",
                "validation_repairs": [],
            },
        }

    def _compute_document_clarity(self, blocks: list[dict]) -> int:
        scores = [
            b.get("clarity_score")
            for b in blocks
            if isinstance(b.get("clarity_score"), (int, float))
        ]
        if not scores:
            return 0
        return int(sum(scores) / len(scores))

    def _compute_section_clarity(self, blocks: list[dict]) -> int:
        return self._compute_document_clarity(blocks)


    # ------------------------------------------------------------
    # 9. Edition Logic v2 (structural + semantic + clarity shaping)
    # ------------------------------------------------------------
    def apply_edition_logic_v2(self, dis_document: dict) -> dict:
        sections = dis_document.get("sections", [])

        sections = self._el2_fix_heading_hierarchy(sections)
        sections = self._el2_merge_micro_sections(sections)
        sections = self._el2_semantic_reorder(sections)
        sections = self._el2_clarity_reorder(sections)
        sections = self._el2_final_coherence_pass(sections)

        scores = [
            s.get("clarity_score")
            for s in sections
            if isinstance(s.get("clarity_score"), (int, float))
        ]
        if scores:
            doc_clarity = int(sum(scores) / len(scores))
        else:
            doc_clarity = dis_document.get("document_clarity_score", 0)

        return {
            "version": dis_document.get("version", "DIS-1"),
            "document_clarity_score": doc_clarity,
            "sections": sections,
        }

    # ---------- EL2 helpers ----------
    def _el2_get_heading(self, section: dict) -> str:
        h = section.get("heading") or ""
        return h.strip()

    def _el2_is_intro(self, heading: str) -> bool:
        h = heading.lower()
        intro_keywords = ["introduction", "overview", "context", "background", "summary"]
        return any(k in h for k in intro_keywords)

    def _el2_is_conclusion(self, heading: str) -> bool:
        h = heading.lower()
        conclusion_keywords = ["conclusion", "next steps", "final notes", "wrap up", "wrap-up"]
        return any(k in h for k in conclusion_keywords)

    def _el2_is_definition(self, heading: str) -> bool:
        h = heading.lower()
        definition_keywords = ["what is", "definition", "purpose", "scope"]
        return any(k in h for k in definition_keywords)

    def _el2_fix_heading_hierarchy(self, sections: list[dict]) -> list[dict]:
        cleaned: list[dict] = []
        last_heading = None

        for s in sections:
            heading = self._el2_get_heading(s)
            blocks = s.get("blocks", []) or []

            has_content = any(
                isinstance(b.get("content"), str) and b["content"].strip()
                for b in blocks
            )
            if not heading and not has_content:
                continue

            if heading and heading == last_heading:
                if cleaned:
                    cleaned[-1]["blocks"].extend(blocks)
                    prev_score = cleaned[-1].get("clarity_score")
                    cur_score = s.get("clarity_score")
                    if isinstance(cur_score, (int, float)):
                        if not isinstance(prev_score, (int, float)) or cur_score > prev_score:
                            cleaned[-1]["clarity_score"] = cur_score
                continue

            s2 = dict(s)
            s2["heading"] = heading or None
            cleaned.append(s2)
            if heading:
                last_heading = heading

        return cleaned

    def _el2_merge_micro_sections(self, sections: list[dict]) -> list[dict]:
        merged: list[dict] = []
        for s in sections:
            blocks = s.get("blocks", []) or []
            text = " ".join(
                b.get("content", "") for b in blocks if isinstance(b.get("content"), str)
            ).strip()

            is_bullet_heavy = any(b.get("type") == "bullet_group" for b in blocks)
            is_micro = len(text) < 40 and not is_bullet_heavy

            if is_micro and merged:
                prev = merged[-1]
                prev["blocks"].extend(blocks)
                prev_score = prev.get("clarity_score")
                cur_score = s.get("clarity_score")
                if isinstance(cur_score, (int, float)):
                    if not isinstance(prev_score, (int, float)) or cur_score > prev_score:
                        prev["clarity_score"] = cur_score
            else:
                merged.append(s)

        return merged

    def _el2_semantic_reorder(self, sections: list[dict]) -> list[dict]:
        intros: list[dict] = []
        definitions: list[dict] = []
        conclusions: list[dict] = []
        middle: list[dict] = []

        for s in sections:
            heading = self._el2_get_heading(s)
            if heading and self._el2_is_intro(heading):
                intros.append(s)
            elif heading and self._el2_is_conclusion(heading):
                conclusions.append(s)
            elif heading and self._el2_is_definition(heading):
                definitions.append(s)
            else:
                middle.append(s)

        ordered: list[dict] = []
        ordered.extend(intros)
        ordered.extend(definitions)
        ordered.extend(middle)
        ordered.extend(conclusions)
        return ordered

    def _el2_clarity_reorder(self, sections: list[dict]) -> list[dict]:
        if len(sections) <= 2:
            return sections

        first = sections[0]
        last = sections[-1]
        middle = sections[1:-1]

        def clarity_key(s: dict) -> float:
            score = s.get("clarity_score")
            return float(score) if isinstance(score, (int, float)) else 0.0

        middle_sorted = sorted(middle, key=clarity_key, reverse=True)
        return [first] + middle_sorted + [last]
    
    # ============================================================
    # ===================== START: EL-3 FULL REORDER =============
    # ============================================================

    def _el3_full_reorder(self, sections: list[dict]) -> list[dict]:
        """
        EL-3: Full Clarity Reorder
        - Semantic clustering
        - Narrative arc ordering
        - Insight prioritisation
        - Smoothness pass
        """

        if not sections or len(sections) <= 2:
            return sections

        # ---------------------------------------------------------
        # 1. Normalise sections
        # ---------------------------------------------------------
        norm = []
        for s in sections:
            s = dict(s)  # shallow copy
            s.setdefault("clarity_score", 0.0)
            s.setdefault("topic", self._infer_topic(s.get("text", "")))
            s.setdefault("type", self._infer_type(s.get("text", "")))
            norm.append(s)
        sections = norm

        # ---------------------------------------------------------
        # 2. Cluster by topic
        # ---------------------------------------------------------
        clusters: dict[str, list[dict]] = {}
        for s in sections:
            topic = s["topic"]
            clusters.setdefault(topic, []).append(s)

        # ---------------------------------------------------------
        # 3. Score clusters
        # ---------------------------------------------------------
        scored_clusters = []
        for topic, secs in clusters.items():
            avg_clarity = sum(s["clarity_score"] for s in secs) / max(len(secs), 1)
            insight_count = sum(1 for s in secs if s["type"] == "insight")
            length_penalty = math.log(len(secs) + 1)

            score = avg_clarity + 0.5 * insight_count - 0.1 * length_penalty

            scored_clusters.append({
                "topic": topic,
                "sections": secs,
                "score": score,
                "insight_count": insight_count,
            })

        # ---------------------------------------------------------
        # 4. Order clusters by narrative arc
        # ---------------------------------------------------------
        arc_order = [
            "context",
            "problem",
            "insight",
            "example",
            "action",
            "reflection",
        ]

        def arc_index(topic: str) -> int:
            try:
                return arc_order.index(topic)
            except ValueError:
                return len(arc_order)

        scored_clusters.sort(
            key=lambda c: (
                arc_index(c["topic"]),
                -c["score"],
            )
        )

        # ---------------------------------------------------------
        # 5. Order sections within clusters
        # ---------------------------------------------------------
        ordered_sections: list[dict] = []

        for cluster in scored_clusters:
            secs = cluster["sections"]

            def section_priority(s: dict):
                length = len(s.get("text", ""))
                is_insight = 1 if s["type"] == "insight" else 0
                return (
                    -s["clarity_score"],
                    -is_insight,
                    length,
                )

            secs_sorted = sorted(secs, key=section_priority)
            ordered_sections.extend(secs_sorted)

        # ---------------------------------------------------------
        # 6. Smoothness pass (remove duplicates, preserve order)
        # ---------------------------------------------------------
        seen = set()
        final = []
        for s in ordered_sections:
            sid = s.get("id")
            if sid and sid in seen:
                continue
            if sid:
                seen.add(sid)
            final.append(s)

        return final

    # ---------------------------------------------------------
    # Helper topic/type inference
    # ---------------------------------------------------------

    def _infer_topic(self, text: str) -> str:
        t = text.lower()
        if any(k in t for k in ["background", "context", "overview", "introduction"]):
            return "context"
        if any(k in t for k in ["problem", "issue", "challenge", "pain"]):
            return "problem"
        if any(k in t for k in ["insight", "key point", "the real issue", "what matters"]):
            return "insight"
        if any(k in t for k in ["for example", "for instance", "e.g.", "example"]):
            return "example"
        if any(k in t for k in ["next step", "action", "you should", "do this"]):
            return "action"
        if any(k in t for k in ["in summary", "to sum up", "overall", "reflection"]):
            return "reflection"
        return "context"

    def _infer_type(self, text: str) -> str:
        t = text.strip().lower()
        if t.endswith("?"):
            return "question"
        if any(k in t for k in ["said", "stated", "according to", "\""]):
            return "quote"
        if any(k in t for k in ["insight", "key", "crucial", "important"]):
            return "insight"
        return "fact"

    # ============================================================
    # ===================== END: EL-3 FULL REORDER ===============
    # ============================================================

    # ============================================================
    # ===================== START: DIS-2 INTERPRETATION ==========
    # ============================================================

    def _dis2_interpretation(self, sections: list[dict]) -> dict:
        """
        DIS-2: Deep Interpretation Layer
        Produces a structured interpretation object:
        - intent
        - tone
        - context signals
        - missing info
        - constraints
        - document type
        """

        if not sections:
            return {
                "intent": "unknown",
                "tone": "neutral",
                "document_type": "unknown",
                "missing_info": [],
                "constraints": [],
                "signals": {},
            }

        # ---------------------------------------------------------
        # 1. Combine all text for global signals
        # ---------------------------------------------------------
        full_text = " ".join(s.get("text", "") for s in sections).lower()

        # ---------------------------------------------------------
        # 2. Infer document type
        # ---------------------------------------------------------
        doc_type = self._infer_document_type(full_text)

        # ---------------------------------------------------------
        # 3. Infer intent
        # ---------------------------------------------------------
        intent = self._infer_intent(full_text)

        # ---------------------------------------------------------
        # 4. Infer tone
        # ---------------------------------------------------------
        tone = self._infer_tone(full_text)

        # ---------------------------------------------------------
        # 5. Detect missing information
        # ---------------------------------------------------------
        missing = self._detect_missing_info(sections, intent, doc_type)

        # ---------------------------------------------------------
        # 6. Extract constraints
        # ---------------------------------------------------------
        constraints = self._extract_constraints(full_text)

        # ---------------------------------------------------------
        # 7. Build interpretation object
        # ---------------------------------------------------------
        interpretation = {
            "intent": intent,
            "tone": tone,
            "document_type": doc_type,
            "missing_info": missing,
            "constraints": constraints,
            "signals": {
                "length": len(full_text),
                "section_count": len(sections),
            },
        }

        return interpretation

    # ---------------------------------------------------------
    # Helper: document type inference
    # ---------------------------------------------------------

    def _infer_document_type(self, text: str) -> str:
        if any(k in text for k in ["lesson", "student", "exercise"]):
            return "teaching"
        if any(k in text for k in ["interview", "quote", "source", "reporting"]):
            return "journalism"
        if any(k in text for k in ["plan", "roadmap", "timeline"]):
            return "planning"
        if any(k in text for k in ["analysis", "research", "study"]):
            return "research"
        if any(k in text for k in ["contract", "agreement", "legal"]):
            return "legal"
        return "general"

    # ---------------------------------------------------------
    # Helper: intent inference
    # ---------------------------------------------------------

    def _infer_intent(self, text: str) -> str:
        if any(k in text for k in ["explain", "what is", "help me understand"]):
            return "understanding"
        if any(k in text for k in ["decide", "choose", "should i"]):
            return "decision"
        if any(k in text for k in ["summarise", "summary", "tl;dr"]):
            return "summarisation"
        if any(k in text for k in ["rewrite", "improve", "make clearer"]):
            return "rewriting"
        if any(k in text for k in ["analyse", "analysis", "break down"]):
            return "analysis"
        return "general_clarity"

    # ---------------------------------------------------------
    # Helper: tone inference
    # ---------------------------------------------------------

    def _infer_tone(self, text: str) -> str:
        if any(k in text for k in ["urgent", "asap", "immediately"]):
            return "urgent"
        if any(k in text for k in ["confused", "unclear", "lost"]):
            return "confused"
        if any(k in text for k in ["frustrated", "annoyed"]):
            return "frustrated"
        if any(k in text for k in ["excited", "looking forward"]):
            return "positive"
        return "neutral"

    # ---------------------------------------------------------
    # Helper: missing info detection
    # ---------------------------------------------------------

    def _detect_missing_info(self, sections: list[dict], intent: str, doc_type: str) -> list[str]:
        missing = []

        if intent == "decision":
            if not any("option" in s.get("text", "").lower() for s in sections):
                missing.append("options_not_listed")
            if not any("criteria" in s.get("text", "").lower() for s in sections):
                missing.append("criteria_not_defined")

        if doc_type == "journalism":
            if not any("quote" in s.get("type", "") for s in sections):
                missing.append("no_quotes")
            if not any("source" in s.get("text", "").lower() for s in sections):
                missing.append("no_sources")

        return missing

    # ---------------------------------------------------------
    # Helper: constraint extraction
    # ---------------------------------------------------------

    def _extract_constraints(self, text: str) -> list[str]:
        constraints = []
        if "no jargon" in text:
            constraints.append("avoid_jargon")
        if "short" in text or "brief" in text:
            constraints.append("keep_short")
        if "formal" in text:
            constraints.append("formal_tone")
        return constraints

    # ============================================================
    # ===================== END: DIS-2 INTERPRETATION ============
    # ============================================================


    # ============================================================
    # ===================== START: DIS-3 INSIGHT EXTRACTION ======
    # ============================================================

    def _dis3_insight_extraction(self, sections: list[dict]) -> dict:
        """
        DIS-3: Insight Extraction Layer
        Extracts:
        - key insights
        - contradictions
        - patterns
        - themes
        - signals of importance
        """

        if not sections:
            return {
                "insights": [],
                "contradictions": [],
                "patterns": [],
                "themes": [],
            }

        # ---------------------------------------------------------
        # 1. Collect all text
        # ---------------------------------------------------------
        texts = [s.get("text", "") for s in sections]
        full_text = " ".join(texts).lower()

        # ---------------------------------------------------------
        # 2. Extract insights (simple heuristic)
        # ---------------------------------------------------------
        insights = []
        for s in sections:
            t = s.get("text", "").lower()
            if any(k in t for k in ["insight", "key point", "important", "crucial", "the real issue"]):
                insights.append(s.get("text", ""))

        # ---------------------------------------------------------
        # 3. Detect contradictions
        # ---------------------------------------------------------
        contradictions = []
        for s in sections:
            t = s.get("text", "").lower()
            if any(k in t for k in ["however", "but", "on the other hand", "yet"]):
                contradictions.append(s.get("text", ""))

        # ---------------------------------------------------------
        # 4. Extract patterns (repeated words)
        # ---------------------------------------------------------
        word_counts = {}
        for s in sections:
            for w in s.get("text", "").lower().split():
                if len(w) > 4:
                    word_counts[w] = word_counts.get(w, 0) + 1

        patterns = [w for w, c in word_counts.items() if c >= 3]

        # ---------------------------------------------------------
        # 5. Extract themes (topic frequency)
        # ---------------------------------------------------------
        topic_counts = {}
        for s in sections:
            topic = s.get("topic", "unknown")
            topic_counts[topic] = topic_counts.get(topic, 0) + 1

        themes = sorted(topic_counts, key=lambda t: -topic_counts[t])

        # ---------------------------------------------------------
        # 6. Build insight object
        # ---------------------------------------------------------
        return {
            "insights": insights,
            "contradictions": contradictions,
            "patterns": patterns,
            "themes": themes,
        }

    # ============================================================
    # ===================== END: DIS-3 INSIGHT EXTRACTION ========
    # ============================================================


    # ============================================================
    # ===================== START: EDITION LOGIC v3 ==============
    # ============================================================

    def _edition_logic_v3(self, sections: list[dict]) -> list[dict]:
        """
        Edition Logic v3:
        Multi-pass refinement pipeline:
        1. EL-2 clarity reorder
        2. EL-3 full reorder
        3. DIS-2 interpretation
        4. DIS-3 insight extraction
        5. Refinement pass (rewrite flags)
        """

        if not sections:
            return sections

        # ---------------------------------------------------------
        # 1. EL-2 clarity reorder
        # ---------------------------------------------------------
        sections = self._el2_clarity_reorder(sections)

        # ---------------------------------------------------------
        # 2. EL-3 full reorder
        # ---------------------------------------------------------
        sections = self._el3_full_reorder(sections)

        # ---------------------------------------------------------
        # 3. DIS-2 interpretation
        # ---------------------------------------------------------
        interpretation = self._dis2_interpretation(sections)

        # ---------------------------------------------------------
        # 4. DIS-3 insight extraction
        # ---------------------------------------------------------
        insights = self._dis3_insight_extraction(sections)

        # ---------------------------------------------------------
        # 5. Refinement pass
        # ---------------------------------------------------------
        refined = []
        for s in sections:
            s = dict(s)
            score = s.get("clarity_score", 0)

            # Mark low clarity for rewrite
            if isinstance(score, (int, float)) and score < 25:
                s["needs_rewrite"] = True

            # Mark contradictions
            if any(c in s.get("text", "").lower() for c in ["however", "but", "yet"]):
                s["contains_contradiction"] = True

            refined.append(s)

        # ---------------------------------------------------------
        # 6. Attach interpretation + insights to metadata
        # ---------------------------------------------------------
        for s in refined:
            s.setdefault("meta", {})
            s["meta"]["interpretation"] = interpretation
            s["meta"]["insights"] = insights

        return refined

    # ============================================================
    # ===================== END: EDITION LOGIC v3 ================
    # ============================================================

    # ============================================================
    # ===================== START: UPDATED RUN PIPELINE v4 =======
    # ============================================================

    def run(self, sections: list[dict], user_request: str = "") -> dict:
        """
        Updated engine pipeline (Fast Path, v4)
        """

        if not sections:
            return {
                "output": "",
                "sections": [],
                "interpretation": {},
                "insights": {},
                "contradictions": {},
                "quality": {},
                "packaged": {},
                "trace": [],
            }

        # ---------------------------------------------------------
        # INIT TRACE MODE (EL-11)
        # ---------------------------------------------------------
        self._init_trace()

        # ---------------------------------------------------------
        # 1. EL-2 clarity reorder
        # ---------------------------------------------------------
        before = sections
        sections = self._el2_clarity_reorder(sections)
        self._trace("EL-2 clarity reorder", before, sections)

        # ---------------------------------------------------------
        # 2. EL-3 full reorder
        # ---------------------------------------------------------
        before = sections
        sections = self._el3_full_reorder(sections)
        self._trace("EL-3 full reorder", before, sections)

        # ---------------------------------------------------------
        # 3. DIS-2 interpretation
        # ---------------------------------------------------------
        interpretation = self._dis2_interpretation(sections)
        self._trace("DIS-2 interpretation", sections, sections, "interpretation extracted")

        # ---------------------------------------------------------
        # 4. DIS-3 insight extraction
        # ---------------------------------------------------------
        insights = self._dis3_insight_extraction(sections)
        self._trace("DIS-3 insight extraction", sections, sections, "insights extracted")

        # ---------------------------------------------------------
        # 5. DIS-4 contradiction resolution
        # ---------------------------------------------------------
        dis4 = self._dis4_contradiction_resolution(sections)
        self._trace("DIS-4 contradiction resolution", sections, sections, "contradictions resolved")

        # ---------------------------------------------------------
        # 6. Edition Logic v4
        # ---------------------------------------------------------
        before = sections
        sections = self._edition_logic_v4(sections, dis4)
        self._trace("Edition Logic v4", before, sections)

        # ---------------------------------------------------------
        # 6.5 EL-4 Semantic Fusion
        # ---------------------------------------------------------
        before = sections
        sections = self._el4_semantic_fusion(sections)
        self._trace("EL-4 Semantic Fusion", before, sections)

        # ---------------------------------------------------------
        # 6.7 EL-5 Contextual Expansion
        # ---------------------------------------------------------
        before = sections
        sections = self._el5_contextual_expansion(sections)
        self._trace("EL-5 Contextual Expansion", before, sections)

        # ---------------------------------------------------------
        # 6.9 EL-6 Intent Mode
        # ---------------------------------------------------------
        before = sections
        sections = self._el6_intent_mode(sections, user_request)
        self._trace("EL-6 Intent Mode", before, sections)

        # ---------------------------------------------------------
        # 6.11 EL-7 Voice & Tone
        # ---------------------------------------------------------
        before = sections
        sections = self._el7_voice_tone(sections)
        self._trace("EL-7 Voice & Tone", before, sections)

        # ---------------------------------------------------------
        # 6.13 EL-8 Structural Compression
        # ---------------------------------------------------------
        before = sections
        sections = self._el8_compression(sections)
        self._trace("EL-8 Structural Compression", before, sections)

        # ---------------------------------------------------------
        # 6.15 EL-9 Final Coherence Pass
        # ---------------------------------------------------------
        before = sections
        sections = self._el9_coherence(sections)
        self._trace("EL-9 Final Coherence", before, sections)

        # ---------------------------------------------------------
        # 7. Edition Logic v3
        # ---------------------------------------------------------
        before = sections
        sections = self._edition_logic_v3(sections)
        self._trace("Edition Logic v3", before, sections)

        # ---------------------------------------------------------
        # 8. Final coherence pass
        # ---------------------------------------------------------
        before = sections
        sections = self._el2_final_coherence_pass(sections)
        self._trace("Final Coherence Pass", before, sections)

        # ---------------------------------------------------------
        # 9. EL-10 Output Realisation
        # ---------------------------------------------------------
        final_output = self._el10_realisation(sections)
        self._trace("EL-10 Output Realisation", sections, sections, "final output rendered")

        # ---------------------------------------------------------
        # 10. EL-12 Quality Scoring
        # ---------------------------------------------------------
        quality = self._el12_quality_scoring(sections, final_output)
        self._trace("EL-12 Quality Scoring", sections, sections, "quality metrics computed")

        # ---------------------------------------------------------
        # 11. EL-13 Output Packaging (optional)
        # ---------------------------------------------------------
        packaged = self._el13_output_packaging(final_output, sections)
        self._trace("EL-13 Output Packaging", sections, sections, "packaged formats created")

        # ---------------------------------------------------------
        # 12. EL-14 Safety Enforcement (optional)
        # ---------------------------------------------------------
        safe_output = self._el14_safety_enforcement(packaged["text"])
        self._trace("EL-14 Safety Enforcement", sections, sections, "safety filters applied")

        # ---------------------------------------------------------
        # 13. EL-15 Style Memory (optional)
        # ---------------------------------------------------------
        styled_output = self._el15_style_memory(safe_output, user_request)
        self._trace("EL-15 Style Memory", sections, sections, "style memory applied")

        # ---------------------------------------------------------
        # 14. Return structured output
        # ---------------------------------------------------------
        return {
            "output": styled_output,
            "sections": sections,
            "interpretation": interpretation,
            "insights": insights,
            "contradictions": dis4,
            "quality": quality,
            "packaged": packaged,
            "trace": getattr(self, "_trace_log", []),
        }

    # ============================================================
    # ===================== END: UPDATED RUN PIPELINE v4 =========
    # ============================================================



    # ============================================================
    # ===================== START: UPDATED LOAD METHOD ===========
    # ============================================================

    def load(self, raw_text: str) -> list[dict]:
        """
        Updated load() method:
        - Splits raw text into sections
        - Assigns IDs
        - Computes initial clarity scores
        - Prepares sections for EL-2, EL-3, DIS-2, DIS-3
        """

        if not raw_text or not raw_text.strip():
            return []

        # ---------------------------------------------------------
        # 1. Split into rough sections (paragraph-based)
        # ---------------------------------------------------------
        chunks = [c.strip() for c in raw_text.split("\n") if c.strip()]

        sections = []
        for idx, chunk in enumerate(chunks):
            sections.append({
                "id": f"sec_{idx}",
                "text": chunk,
                "clarity_score": self._initial_clarity_score(chunk),
            })

        return sections

    # ---------------------------------------------------------
    # Helper: initial clarity scoring
    # ---------------------------------------------------------

    def _initial_clarity_score(self, text: str) -> float:
        """
        Very simple heuristic clarity score:
        - shorter sentences = clearer
        - fewer commas = clearer
        - fewer filler words = clearer
        """

        if not text:
            return 0.0

        length_penalty = len(text) / 200
        comma_penalty = text.count(",") * 0.5

        filler_words = ["basically", "actually", "literally", "kind of", "sort of"]
        filler_penalty = sum(1 for w in filler_words if w in text.lower()) * 2

        score = 100 - (length_penalty + comma_penalty + filler_penalty)
        return max(0.0, min(100.0, score))

    # ============================================================
    # ===================== END: UPDATED LOAD METHOD =============
    # ============================================================

    # ============================================================
    # ===================== START: UPDATED EL-2 FINAL COHERENCE ==
    # ============================================================

    def _el2_final_coherence_pass(self, sections: list[dict]) -> list[dict]:
        """
        Updated final coherence pass:
        - marks low clarity
        - merges duplicate headings
        - preserves conclusion at the end
        - ensures metadata consistency
        """

        if not sections:
            return sections

        # ---------------------------------------------------------
        # 1. Mark low clarity
        # ---------------------------------------------------------
        for s in sections:
            score = s.get("clarity_score")
            if isinstance(score, (int, float)) and score <= 20:
                s["needs_revision"] = True

        # ---------------------------------------------------------
        # 2. Merge consecutive sections with same heading
        # ---------------------------------------------------------
        cleaned: list[dict] = []
        last_heading = None

        for s in sections:
            heading = self._el2_get_heading(s)
            if heading and heading == last_heading:
                if cleaned:
                    cleaned[-1].setdefault("blocks", [])
                    cleaned[-1]["blocks"].extend(s.get("blocks", []) or [])
                    if "text" in s and s["text"]:
                        cleaned[-1]["text"] = (
                            cleaned[-1].get("text", "") + "\n" + s["text"]
                        )
                continue

            cleaned.append(s)
            if heading:
                last_heading = heading

        sections = cleaned

        # ---------------------------------------------------------
        # 3. Ensure conclusion is last if present
        # ---------------------------------------------------------
        if len(sections) >= 2:
            if not self._el2_is_conclusion(self._el2_get_heading(sections[-1])):
                for i, s in enumerate(sections[:-1]):
                    if self._el2_is_conclusion(self._el2_get_heading(s)):
                        sections.append(sections.pop(i))
                        break

        # ---------------------------------------------------------
        # 4. Ensure metadata exists
        # ---------------------------------------------------------
        for s in sections:
            s.setdefault("meta", {})
            s["meta"].setdefault("interpretation", {})
            s["meta"].setdefault("insights", {})

        return sections

    # ============================================================
    # ===================== END: UPDATED EL-2 FINAL COHERENCE ====
    # ============================================================


     # ============================================
    # EL3 — Structure Extraction
    # ============================================

    def _el3_detect_paragraphs(self, lines: list[str]) -> list[str]:
        paragraphs = []
        buffer = []

        for raw in lines:
            line = raw.rstrip("\n")
            if line.strip():
                buffer.append(line)
            else:
                if buffer:
                    paragraphs.append(" ".join(buffer).strip())
                    buffer = []

        if buffer:
            paragraphs.append(" ".join(buffer).strip())

        return paragraphs

    def _el3_merge_short_paragraphs(self, paragraphs: list[str], min_len: int = 80) -> list[str]:
        if not paragraphs:
            return paragraphs

        merged = []
        buffer = None

        for p in paragraphs:
            if buffer is None:
                buffer = p
            else:
                if len(buffer) < min_len:
                    buffer = buffer + " " + p
                else:
                    merged.append(buffer)
                    buffer = p

        if buffer:
            merged.append(buffer)

        return merged

    def _el3_split_long_paragraphs(self, paragraphs: list[str], max_len: int = 350) -> list[str]:
        if not paragraphs:
            return paragraphs

        result = []

        for p in paragraphs:
            text = p.strip()

            while len(text) > max_len:
                breakpoints = [
                    text.rfind(". ", 0, max_len),
                    text.rfind("; ", 0, max_len),
                    text.rfind("—", 0, max_len),
                    text.rfind("  ", 0, max_len),
                ]

                cut = max(breakpoints)

                if cut == -1:
                    cut = text.rfind(" ", 0, max_len)

                if cut == -1:
                    cut = max_len

                chunk = text[:cut].strip()
                result.append(chunk)
                text = text[cut:].strip()

            if text:
                result.append(text)

        return result

    def _el3_detect_lists(self, lines: list[str]) -> list[dict]:
        import re

        blocks = []
        buffer = []
        mode = None  # "bullet", "numbered", or None

        bullet_markers = ("- ", "* ", "• ")
        numbered_pattern = re.compile(r"^\d+\.\s+")

        def flush_buffer():
            nonlocal buffer, mode
            if not buffer:
                return

            if mode == "bullet":
                blocks.append({
                    "type": "bullet_group",
                    "items": buffer.copy(),
                    "block_type": "list"
                })
            elif mode == "numbered":
                blocks.append({
                    "type": "numbered_group",
                    "items": buffer.copy(),
                    "block_type": "steps"
                })
            else:
                content = " ".join(buffer).strip()
                blocks.append({
                    "type": "paragraph",
                    "content": content,
                    "block_type": "paragraph"
                })

            buffer = []
            mode = None

        for raw in lines:
            line = raw.rstrip("\n")
            stripped = line.strip()

            if not stripped:
                flush_buffer()
                continue

            if any(stripped.startswith(m) for m in bullet_markers):
                if mode not in ("bullet", None):
                    flush_buffer()
                mode = "bullet"
                buffer.append(stripped)
                continue

            if numbered_pattern.match(stripped):
                if mode not in ("numbered", None):
                    flush_buffer()
                mode = "numbered"
                buffer.append(stripped)
                continue

            if mode is not None:
                flush_buffer()
            mode = None
            buffer.append(stripped)

        flush_buffer()
        return blocks

    def el3(self, text: str) -> list[dict]:
        lines = text.splitlines()

        # 1. Detect lists and paragraphs
        blocks = self._el3_detect_lists(lines)

        # 2. Extract paragraph content for shaping
        paragraphs = [
            b["content"] for b in blocks
            if b.get("type") == "paragraph"
        ]

        # 3. Merge short paragraphs
        paragraphs = self._el3_merge_short_paragraphs(paragraphs)

        # 4. Split long paragraphs
        paragraphs = self._el3_split_long_paragraphs(paragraphs)

        # 5. Rebuild final block list
        final_blocks = []
        p_index = 0

        for b in blocks:
            if b["type"] in ("bullet_group", "numbered_group"):
                final_blocks.append(b)
            else:
                final_blocks.append({
                    "type": "paragraph",
                    "content": paragraphs[p_index],
                })
                p_index += 1

        return final_blocks

    # ============================================================
    # ===================== START: EL3 STRUCTURE EXTRACTION ======
    # ============================================================

    def _el3_structure_extraction(self, sections: list[dict]) -> dict:
        """
        EL-3 Structure Extraction:
        - Detects headings
        - Detects hierarchy levels
        - Detects section boundaries
        - Detects missing structure
        - Detects floating paragraphs
        """

        if not sections:
            return {
                "headings": [],
                "hierarchy": [],
                "floating": [],
                "missing": [],
            }

        headings = []
        hierarchy = []
        floating = []
        missing = []

        # ---------------------------------------------------------
        # 1. Detect headings
        # ---------------------------------------------------------
        for s in sections:
            text = s.get("text", "").strip()
            if self._looks_like_heading(text):
                headings.append({
                    "id": s.get("id"),
                    "text": text,
                    "level": self._heading_level(text),
                })

        # ---------------------------------------------------------
        # 2. Detect hierarchy (simple heuristic)
        # ---------------------------------------------------------
        for h in headings:
            lvl = h["level"]
            if lvl == 1:
                hierarchy.append({"type": "top_level", "heading": h})
            elif lvl == 2:
                hierarchy.append({"type": "subsection", "heading": h})
            else:
                hierarchy.append({"type": "detail", "heading": h})

        # ---------------------------------------------------------
        # 3. Detect floating paragraphs (no heading above)
        # ---------------------------------------------------------
        last_heading = None
        for s in sections:
            text = s.get("text", "").strip()
            if self._looks_like_heading(text):
                last_heading = text
                continue
            if last_heading is None:
                floating.append(s.get("id"))

        # ---------------------------------------------------------
        # 4. Detect missing structure
        # ---------------------------------------------------------
        if not headings:
            missing.append("no_headings")

        if headings and headings[0]["level"] != 1:
            missing.append("missing_top_level_heading")

        return {
            "headings": headings,
            "hierarchy": hierarchy,
            "floating": floating,
            "missing": missing,
        }

    # ---------------------------------------------------------
    # Helper: detect if text looks like a heading
    # ---------------------------------------------------------

    def _looks_like_heading(self, text: str) -> bool:
        if not text:
            return False
        if len(text.split()) <= 6 and text[0].isupper():
            return True
        if text.endswith(":"):
            return True
        return False

    # ---------------------------------------------------------
    # Helper: heading level detection
    # ---------------------------------------------------------

    def _heading_level(self, text: str) -> int:
        t = text.lower()
        if any(k in t for k in ["introduction", "overview", "summary"]):
            return 1
        if any(k in t for k in ["background", "context", "problem"]):
            return 2
        if any(k in t for k in ["example", "details", "notes"]):
            return 3
        return 2

    # ============================================================
    # ===================== END: EL3 STRUCTURE EXTRACTION ========
    # ============================================================


    # ============================================================
    # ===================== START: DIS-4 CONTRADICTION RESOLUTION =
    # ============================================================

    def _dis4_contradiction_resolution(self, sections: list[dict]) -> dict:
        """
        DIS-4: Contradiction Resolution Layer
        - Detects cross-section contradictions
        - Classifies them
        - Attempts resolution
        - Marks unresolved conflicts
        - Produces a consistency map
        """

        if not sections:
            return {
                "contradictions": [],
                "resolved": [],
                "unresolved": [],
                "consistency_map": {},
            }

        contradictions = []
        resolved = []
        unresolved = []
        consistency_map = {}

        # ---------------------------------------------------------
        # 1. Collect all text
        # ---------------------------------------------------------
        texts = [(s.get("id"), s.get("text", "").lower()) for s in sections]

        # ---------------------------------------------------------
        # 2. Simple contradiction patterns
        # ---------------------------------------------------------
        contradiction_pairs = [
            ("should", "should not"),
            ("must", "must not"),
            ("is", "is not"),
            ("are", "are not"),
            ("cannot", "can"),
            ("never", "always"),
        ]

        # ---------------------------------------------------------
        # 3. Detect contradictions across sections
        # ---------------------------------------------------------
        for i, (id1, t1) in enumerate(texts):
            for id2, t2 in texts[i+1:]:
                for a, b in contradiction_pairs:
                    if a in t1 and b in t2:
                        contradictions.append((id1, id2, a, b))
                    if b in t1 and a in t2:
                        contradictions.append((id1, id2, b, a))

        # ---------------------------------------------------------
        # 4. Attempt resolution
        # ---------------------------------------------------------
        for c in contradictions:
            id1, id2, a, b = c

            # Simple heuristic: if one section has low clarity, prefer the clearer one
            s1 = next(s for s in sections if s["id"] == id1)
            s2 = next(s for s in sections if s["id"] == id2)

            score1 = s1.get("clarity_score", 50)
            score2 = s2.get("clarity_score", 50)

            if abs(score1 - score2) >= 20:
                # Resolve by preferring clearer section
                resolved.append({
                    "kept": id1 if score1 > score2 else id2,
                    "discarded": id2 if score1 > score2 else id1,
                    "reason": "clarity_preference",
                })
            else:
                unresolved.append({
                    "pair": (id1, id2),
                    "reason": "insufficient_signal",
                })

        # ---------------------------------------------------------
        # 5. Build consistency map
        # ---------------------------------------------------------
        for s in sections:
            consistency_map[s["id"]] = {
                "contradicts": [
                    c for c in contradictions if c[0] == s["id"] or c[1] == s["id"]
                ],
                "resolved": [
                    r for r in resolved if r["kept"] == s["id"] or r.get("discarded") == s["id"]
                ],
                "unresolved": [
                    u for u in unresolved if s["id"] in u["pair"]
                ],
            }

        return {
            "contradictions": contradictions,
            "resolved": resolved,
            "unresolved": unresolved,
            "consistency_map": consistency_map,
        }

    # ============================================================
    # ===================== END: DIS-4 CONTRADICTION RESOLUTION ==
    # ============================================================


    # ============================================================
    # ===================== START: EDITION LOGIC v4 ==============
    # ============================================================

    def _edition_logic_v4(self, sections: list[dict], dis4: dict) -> list[dict]:
        """
        Edition Logic v4:
        Conflict-aware refinement layer.
        Uses DIS-4 contradiction map to:
        - resolve contradictions
        - harmonize tone
        - unify meaning
        - mark unresolved conflicts
        - produce a coherent final document
        """

        if not sections:
            return sections

        contradictions = dis4.get("contradictions", [])
        resolved = dis4.get("resolved", [])
        unresolved = dis4.get("unresolved", [])
        consistency_map = dis4.get("consistency_map", {})

        refined = []

        # ---------------------------------------------------------
        # 1. Resolve contradictions by preferring clearer sections
        # ---------------------------------------------------------
        resolved_ids = {r["discarded"] for r in resolved}

        for s in sections:
            if s["id"] in resolved_ids:
                # Drop the weaker section
                continue
            refined.append(dict(s))

        # ---------------------------------------------------------
        # 2. Mark unresolved contradictions for rewrite
        # ---------------------------------------------------------
        for u in unresolved:
            id1, id2 = u["pair"]
            for s in refined:
                if s["id"] in (id1, id2):
                    s.setdefault("meta", {})
                    s["meta"]["needs_conflict_resolution"] = True

        # ---------------------------------------------------------
        # 3. Harmonize tone across sections
        # ---------------------------------------------------------
        for s in refined:
            text = s.get("text", "")
            if "!" in text:
                s["text"] = text.replace("!", ".")
            if "??" in text:
                s["text"] = s["text"].replace("??", "?")

        # ---------------------------------------------------------
        # 4. Unify meaning by smoothing modal verbs
        # ---------------------------------------------------------
        modal_map = {
            "should": "should",
            "should not": "should not",
            "must": "must",
            "must not": "must not",
            "can": "can",
            "cannot": "cannot",
        }

        for s in refined:
            text = s.get("text", "").lower()
            for m in modal_map:
                if m in text:
                    s.setdefault("meta", {})
                    s["meta"]["modal_normalized"] = modal_map[m]

        # ---------------------------------------------------------
        # 5. Attach consistency map to metadata
        # ---------------------------------------------------------
        for s in refined:
            s.setdefault("meta", {})
            s["meta"]["consistency"] = consistency_map.get(s["id"], {})

        return refined

    # ============================================================
    # ===================== END: EDITION LOGIC v4 ================
    # ============================================================


    # ============================================================
    # ===================== START: EL-4 SEMANTIC FUSION ==========
    # ============================================================

    def _el4_semantic_fusion(self, sections: list[dict]) -> list[dict]:
        """
        EL-4 Semantic Section Fusion:
        - Detects semantically similar sections
        - Merges overlapping meaning
        - Removes redundancy
        - Produces a unified, cleaner document
        """

        if not sections:
            return sections

        fused = []
        skip_ids = set()

        # ---------------------------------------------------------
        # 1. Simple semantic similarity heuristic
        # ---------------------------------------------------------
        def similarity(a: str, b: str) -> float:
            a_words = set(a.lower().split())
            b_words = set(b.lower().split())
            if not a_words or not b_words:
                return 0.0
            overlap = len(a_words & b_words)
            total = len(a_words | b_words)
            return overlap / total

        # ---------------------------------------------------------
        # 2. Compare each section with every other section
        # ---------------------------------------------------------
        for i, s1 in enumerate(sections):
            if s1["id"] in skip_ids:
                continue

            merged_text = s1.get("text", "")
            merged_meta = dict(s1.get("meta", {}))

            for j, s2 in enumerate(sections[i+1:], start=i+1):
                if s2["id"] in skip_ids:
                    continue

                sim = similarity(
                    s1.get("text", ""),
                    s2.get("text", "")
                )

                # Threshold for semantic fusion
                if sim >= 0.45:
                    skip_ids.add(s2["id"])
                    merged_text += " " + s2.get("text", "")
                    merged_meta.update(s2.get("meta", {}))

            fused.append({
                "id": s1["id"],
                "text": merged_text.strip(),
                "meta": merged_meta,
            })

        # ---------------------------------------------------------
        # 3. Clean up whitespace and punctuation
        # ---------------------------------------------------------
        for s in fused:
            t = s["text"]
            t = t.replace("  ", " ").replace(" .", ".")
            t = t.replace(" ,", ",").strip()
            s["text"] = t

        return fused

    # ============================================================
    # ===================== END: EL-4 SEMANTIC FUSION ============
    # ============================================================

    # ============================================================
    # ===================== START: EL-5 CONTEXTUAL EXPANSION =====
    # ============================================================

    def _el5_contextual_expansion(self, sections: list[dict]) -> list[dict]:
        """
        EL-5 Contextual Expansion Layer:
        - Expands weak or underspecified sections
        - Adds missing background or context
        - Strengthens reasoning
        - Clarifies ambiguous statements
        - Only expands where needed (not global rewriting)
        """

        if not sections:
            return sections

        expanded = []

        # ---------------------------------------------------------
        # 1. Heuristic: detect weak sections
        # ---------------------------------------------------------
        def is_weak(text: str) -> bool:
            if not text:
                return True
            words = text.split()
            if len(words) < 12:
                return True
            if text.endswith("?"):
                return True
            return False

        # ---------------------------------------------------------
        # 2. Expand weak sections
        # ---------------------------------------------------------
        for s in sections:
            text = s.get("text", "")
            meta = dict(s.get("meta", {}))

            if is_weak(text):
                # Add contextual expansion
                expansion = (
                    " This section appears to introduce an idea but lacks detail. "
                    "To clarify, the key point can be expanded by explaining its purpose, "
                    "its relevance, and how it connects to the surrounding content."
                )
                new_text = (text + expansion).strip()
                meta["expanded"] = True
            else:
                new_text = text
                meta["expanded"] = False

            expanded.append({
                "id": s["id"],
                "text": new_text,
                "meta": meta,
            })

        # ---------------------------------------------------------
        # 3. Light smoothing
        # ---------------------------------------------------------
        for s in expanded:
            t = s["text"]
            t = t.replace("  ", " ").strip()
            s["text"] = t

        return expanded

    # ============================================================
    # ===================== END: EL-5 CONTEXTUAL EXPANSION =======
    # ============================================================


    # ============================================================
    # ===================== START: EL-6 INTENT MODE ==============
    # ============================================================

    def _el6_intent_mode(self, sections: list[dict], user_request: str = "") -> list[dict]:
        """
        EL-6 Intent-Adaptive Output Mode:
        - Detects or infers the user's intent
        - Applies mode-specific shaping
        - Supports teaching, summary, rewrite, analysis, planning, journalism modes
        """

        if not sections:
            return sections

        # ---------------------------------------------------------
        # 1. Detect mode from user request
        # ---------------------------------------------------------
        request = user_request.lower()

        if "teach" in request or "explain" in request:
            mode = "teaching"
        elif "summar" in request:
            mode = "summary"
        elif "rewrite" in request:
            mode = "rewrite"
        elif "analy" in request:
            mode = "analysis"
        elif "plan" in request:
            mode = "planning"
        elif "report" in request or "journal" in request:
            mode = "journalism"
        else:
            mode = "default"

        # ---------------------------------------------------------
        # 2. Apply mode-specific shaping
        # ---------------------------------------------------------
        shaped = []

        for s in sections:
            text = s.get("text", "")
            meta = dict(s.get("meta", {}))

            if mode == "teaching":
                text = (
                    "Here’s the key idea explained clearly: "
                    + text
                    + " This means the reader should now understand the concept more easily."
                )

            elif mode == "summary":
                words = text.split()
                if len(words) > 25:
                    text = "Summary: " + " ".join(words[:25]) + "…"

            elif mode == "rewrite":
                text = text.capitalize().replace("  ", " ")

            elif mode == "analysis":
                text = (
                    "Analytical insight: "
                    + text
                    + " This suggests deeper implications worth considering."
                )

            elif mode == "planning":
                text = (
                    "Action step: "
                    + text
                    + " This should be executed in sequence with the surrounding steps."
                )

            elif mode == "journalism":
                text = (
                    "According to the information presented: "
                    + text
                    + " This reflects the broader context of the situation."
                )

            shaped.append({
                "id": s["id"],
                "text": text,
                "meta": meta | {"mode": mode},
            })

        return shaped

    # ============================================================
    # ===================== END: EL-6 INTENT MODE ================
    # ============================================================


    # ============================================================
    # ===================== START: EL-7 VOICE & TONE =============
    # ============================================================

    def _el7_voice_tone(self, sections: list[dict]) -> list[dict]:
        """
        EL-7 Voice & Tone Harmonisation:
        - Ensures consistent tone across all sections
        - Normalises formality/informality
        - Aligns pronouns, tense, and perspective
        - Smooths stylistic mismatches
        """

        if not sections:
            return sections

        harmonised = []

        # ---------------------------------------------------------
        # 1. Detect dominant tone
        # ---------------------------------------------------------
        sample_text = " ".join(s.get("text", "") for s in sections).lower()

        if "we " in sample_text or "our " in sample_text:
            dominant = "collective"
        elif "i " in sample_text:
            dominant = "first_person"
        else:
            dominant = "neutral"

        # ---------------------------------------------------------
        # 2. Apply tone normalisation
        # ---------------------------------------------------------
        for s in sections:
            text = s.get("text", "")
            meta = dict(s.get("meta", {}))

            # Normalise exclamation marks
            text = text.replace("!", ".")

            # Normalise double spaces
            text = text.replace("  ", " ")

            # Tone alignment
            if dominant == "collective":
                text = text.replace("I ", "We ").replace(" my ", " our ")
            elif dominant == "first_person":
                text = text.replace("We ", "I ").replace(" our ", " my ")

            harmonised.append({
                "id": s["id"],
                "text": text.strip(),
                "meta": meta | {"tone": dominant},
            })

        return harmonised

    # ============================================================
    # ===================== END: EL-7 VOICE & TONE ===============
    # ============================================================

    # ============================================================
    # ===================== START: EL-8 COMPRESSION ==============
    # ============================================================

    def _el8_compression(self, sections: list[dict]) -> list[dict]:
        """
        EL-8 Structural Compression Layer:
        - Shortens overly long sections
        - Removes filler and redundancy
        - Compresses structure while preserving meaning
        """

        if not sections:
            return sections

        compressed = []

        # ---------------------------------------------------------
        # 1. Helper: compress text by removing filler
        # ---------------------------------------------------------
        def compress_text(text: str) -> str:
            fillers = [
                "in order to",
                "basically",
                "essentially",
                "actually",
                "as a matter of fact",
                "it is important to note that",
                "the fact of the matter is",
            ]

            for f in fillers:
                text = text.replace(f, "")

            # Remove double spaces
            text = " ".join(text.split())

            # If too long, compress to ~40 words
            words = text.split()
            if len(words) > 40:
                text = " ".join(words[:40]) + "…"

            return text.strip()

        # ---------------------------------------------------------
        # 2. Apply compression to each section
        # ---------------------------------------------------------
        for s in sections:
            text = s.get("text", "")
            meta = dict(s.get("meta", {}))

            new_text = compress_text(text)

            compressed.append({
                "id": s["id"],
                "text": new_text,
                "meta": meta | {"compressed": True},
            })

        return compressed

    # ============================================================
    # ===================== END: EL-8 COMPRESSION ================
    # ============================================================

    # ============================================================
    # ===================== START: EL-9 COHERENCE ================
    # ============================================================

    def _el9_coherence(self, sections: list[dict]) -> list[dict]:
        """
        EL-9 Final Coherence Pass:
        - Smooths transitions between sections
        - Ensures logical flow
        - Removes abrupt jumps
        - Harmonises pacing and continuity
        """

        if not sections:
            return sections

        coherent = []

        # ---------------------------------------------------------
        # 1. Transition helper
        # ---------------------------------------------------------
        def transition(prev: str, curr: str) -> str:
            if not prev:
                return curr
            if curr.lower().startswith(("however", "but", "also", "therefore")):
                return curr
            return "Additionally, " + curr[0].lower() + curr[1:]

        # ---------------------------------------------------------
        # 2. Apply transitions between sections
        # ---------------------------------------------------------
        previous_text = ""

        for s in sections:
            text = s.get("text", "")
            meta = dict(s.get("meta", {}))

            if previous_text:
                text = transition(previous_text, text)

            coherent.append({
                "id": s["id"],
                "text": text.strip(),
                "meta": meta | {"coherent": True},
            })

            previous_text = text

        return coherent

    # ============================================================
    # ===================== END: EL-9 COHERENCE ==================
    # ============================================================


    # ============================================================
    # ===================== START: EL-10 REALISATION =============
    # ============================================================

    def _el10_realisation(self, sections: list[dict]) -> str:
        """
        EL-10 Output Realisation Layer:
        - Converts processed sections into final output text
        - Applies formatting rules
        - Ensures clean spacing and paragraph structure
        """

        if not sections:
            return ""

        output_lines = []

        for s in sections:
            text = s.get("text", "").strip()

            # Basic formatting rules
            if not text.endswith((".", "!", "?")):
                text += "."

            output_lines.append(text)

        # Join with paragraph breaks
        final_output = "\n\n".join(output_lines)

        # Final cleanup
        final_output = final_output.replace("  ", " ").strip()

        return final_output

    # ============================================================
    # ===================== END: EL-10 REALISATION ===============
    # ============================================================


    # ============================================================
    # ===================== START: EL-12 QUALITY ==================
    # ============================================================

    def _el12_quality_scoring(self, sections: list[dict], final_output: str) -> dict:
        """
        EL-12 Quality Scoring Layer:
        Produces diagnostic scores for clarity, coherence, structure, tone, etc.
        """

        if not sections:
            return {
                "clarity": 0,
                "coherence": 0,
                "compression_efficiency": 0,
                "expansion_value": 0,
                "semantic_density": 0,
                "contradiction_risk": 0,
                "tone_consistency": 0,
                "structure_quality": 0,
            }

        # Simple heuristics (you can refine later)
        clarity = sum(len(s.get("text", "")) for s in sections) / max(1, len(sections))
        coherence = 1 - (abs(len(sections) - 1) * 0.02)
        compression_eff = 1 - (sum(len(s.get("text", "")) for s in sections) / max(1, len(final_output)))
        expansion_val = len(final_output) / max(1, sum(len(s.get("text", "")) for s in sections))
        semantic_density = len(final_output.split()) / max(1, len(sections))
        contradiction_risk = 0.05  # placeholder
        tone_consistency = 0.9     # placeholder
        structure_quality = 0.85   # placeholder

        return {
            "clarity": round(clarity, 3),
            "coherence": round(coherence, 3),
            "compression_efficiency": round(compression_eff, 3),
            "expansion_value": round(expansion_val, 3),
            "semantic_density": round(semantic_density, 3),
            "contradiction_risk": round(contradiction_risk, 3),
            "tone_consistency": round(tone_consistency, 3),
            "structure_quality": round(structure_quality, 3),
        }

    # ============================================================
    # ===================== END: EL-12 QUALITY ====================
    # ============================================================

    # ============================================================
    # ===================== REMAINING MODULE LOGIC ===============
    # ============================================================

    # ---------------------- EL-11 Trace Mode --------------------
    def _init_trace(self):
        self._trace_log = []

    def _trace(self, stage: str, before, after, notes: str = ""):
        self._trace_log.append({
            "stage": stage,
            "before_count": len(before) if isinstance(before, list) else None,
            "after_count": len(after) if isinstance(after, list) else None,
            "notes": notes,
        })

    # ---------------------- EL-13 Output Packaging --------------
    def _el13_output_packaging(self, final_output: str, sections: list[dict]):
        return {
            "text": final_output,
            "sections": sections,
            "markdown": final_output,
            "json": {
                "sections": sections,
                "output": final_output,
            }
        }

    # ---------------------- EL-14 Safety Layer ------------------
    def _el14_safety_enforcement(self, final_output: str):
        # placeholder: enforce tone, length, domain rules
        return final_output

    # ---------------------- EL-15 Style Memory ------------------
    def _el15_style_memory(self, final_output: str, user_request: str):
        # placeholder: adapt to user style preferences
        return final_output

    # ---------------------- EL-16 Multi-Document Synthesis ------
    def _el16_multi_document_synthesis(self, documents: list[list[dict]]):
        # placeholder: merge multiple doc section lists
        merged = []
        for doc in documents:
            merged.extend(doc)
        return merged


    
    def apply_edition_logic_v3(self, blocks: list[dict], user_request: str = "") -> list[dict]:
        """
        Edition Logic v3:
        - Detect mode
        - Apply mode-specific shaping
        - Merge micro-sections
        - Infer missing headings
        - Semantic ordering
        - Clarity-weighted ordering
        - Coherence pass
        """
        if not blocks:
            return blocks

        # 1. Detect mode
        mode = self._el3_detect_mode(blocks, user_request)

        # 2. Apply mode-specific shaping
        if mode == "short":
            blocks = self._el3_apply_short_mode(blocks)
        elif mode == "simple":
            blocks = self._el3_apply_simple_mode(blocks)
        elif mode == "clear":
            blocks = self._el3_apply_clear_mode(blocks)
        elif mode == "precise":
            blocks = self._el3_apply_precise_mode(blocks)
        elif mode == "formal":
            blocks = self._el3_apply_formal_mode(blocks)

        # 3. Merge micro-sections
        blocks = self._el3_merge_micro_sections(blocks)

        # 4. Infer missing headings
        blocks = self._el3_infer_missing_headings(blocks)

        # 5. Semantic ordering
        blocks = self._el3_semantic_order(blocks)

        # 6. Clarity-weighted ordering
        blocks = self._el3_clarity_weighted_order(blocks)

        # 7. Final coherence pass
        blocks = self._el3_coherence_pass(blocks)

        return blocks


    def _el3_apply_formal_mode(self, dis_document: dict) -> dict:
        """
        Edition Logic v3 — Formal Mode
        Elevates tone, removes contractions, replaces casual vocabulary,
        and enforces a professional register while preserving meaning.
        """

        contractions = {
            "can't": "cannot",
            "won't": "will not",
            "don't": "do not",
            "doesn't": "does not",
            "isn't": "is not",
            "aren't": "are not",
            "couldn't": "could not",
            "shouldn't": "should not",
            "wouldn't": "would not",
            "i'm": "I am",
            "we're": "we are",
            "they're": "they are",
            "it's": "it is",
            "that's": "that is",
            "let's": "let us",
            "gonna": "going to",
            "wanna": "want to",
            "we'll": "we will",
            "we’ll": "we will",
            "I'll": "I will",
            "I’ll": "I will",
            "they'll": "they will",
            "they’ll": "they will",

        }

        casual_to_formal = {
            "get": "obtain",
            "give": "provide",
            "show": "demonstrate",
            "tell": "inform",
            "fix": "resolve",
            "start": "commence",
            "end": "conclude",
            "help": "assist",
            "use": "utilize",
            "need": "require",
            "kind of": "somewhat",
            "sort of": "somewhat",
            "a bit": "slightly",
        }

        formal_openers = [
            "In addition,",
            "Furthermore,",
            "Moreover,",
            "Consequently,",
            "Therefore,"
        ]

        new_sections = []

        for sec in dis_document.get("sections", []):
            blocks = sec.get("blocks", []) or []
            new_blocks = []

            for blk in blocks:
                text = blk.get("content", "") or ""
                if not isinstance(text, str) or not text.strip():
                    new_blocks.append(blk)
                    continue

                processed = text
                # Normalise curly apostrophes → straight apostrophes
                processed = processed.replace("’", "'")
                # Multi‑word phrase replacements (run before single‑word replacements)
                phrase_map = {
                    "sort it out": "resolve the matter",
                    "a bit later": "slightly later",
                    "I think we require to": "I believe it is necessary to",
                    "provide people time": "allow people time",
                }

                for phrase, formal in phrase_map.items():
                    processed = processed.replace(phrase, formal)


                # Expand contractions
                for c, full in contractions.items():
                    processed = processed.replace(c, full)
                    processed = processed.replace(c.capitalize(), full.capitalize())

                # Replace casual vocabulary
                import re

                for casual, formal in casual_to_formal.items():
                    processed = re.sub(rf"\b{re.escape(casual)}\b", formal, processed, flags=re.IGNORECASE)

                # Add formal openers to short sentences
                sentences = [s.strip() for s in processed.split(".") if s.strip()]
                enhanced = []

                for s in sentences:
                    if len(s.split()) <= 6:
                        s = f"{formal_openers[0]} {s}"
                    enhanced.append(s)

                blk["content"] = ". ".join(enhanced) + "."
                new_blocks.append(blk)

            sec["blocks"] = new_blocks
            new_sections.append(sec)

        dis_document["sections"] = new_sections
        return dis_document

    # ============================================
    # EDITION LOGIC V3 — CHUNK 2 (START)
    # Mode-specific shaping functions
    # ============================================

    def _el3_apply_short_mode(self, blocks: list[dict]) -> list[dict]:
        """
        Short mode:
        - Keep only the most essential blocks.
        - Reduce content length.
        - Ideal for summaries or very short inputs.
        """
        if not blocks:
            return blocks

        # Keep only the first block (intro) and the most important block (highest clarity score)
        intro = blocks[0]
        best = max(blocks, key=lambda b: b.get("clarity", 0))

        # If intro and best are the same, return just one
        if intro is best:
            return [intro]

        return [intro, best]


    def _el3_apply_simple_mode(self, blocks: list[dict]) -> list[dict]:
        """
        Simple mode:
        - Remove complex or dense blocks.
        - Keep blocks with lower complexity scores.
        - Ideal for ESL learners or simplified explanations.
        """
        simple_blocks = []
        for b in blocks:
            complexity = b.get("complexity", 0)
            if complexity <= 0.6:  # MVP threshold
                simple_blocks.append(b)

        # If everything was filtered out, fall back to original
        return simple_blocks or blocks


    def _el3_apply_clear_mode(self, blocks: list[dict]) -> list[dict]:
        """
        Clear mode:
        - Default mode.
        - Keep all blocks but ensure clarity metadata is present.
        """
        for b in blocks:
            if "clarity" not in b:
                b["clarity"] = 0.5  # neutral clarity baseline
        return blocks


    def _el3_apply_formal_mode(self, blocks: list[dict]) -> list[dict]:
        """
        Formal mode:
        - Slightly elevate tone.
        - Add a 'formal' tag to blocks.
        - Later layers (EL4) may rewrite text more deeply.
        """
        for b in blocks:
            b["tone"] = "formal"
        return blocks

    # ============================================
    # EDITION LOGIC V3 — CHUNK 2 (END)
    # ============================================

    # ============================================
    # EDITION LOGIC V3 — CHUNK 3 (START)
    # Structural shaping functions
    # ============================================

    def _el3_merge_micro_sections(self, blocks: list[dict]) -> list[dict]:
        """
        Merge micro-sections:
        - If a block is extremely short (e.g., < 20 chars),
          merge it with the next block.
        - Prevents fragmentation and improves readability.
        """
        if not blocks:
            return blocks

        merged = []
        buffer = None

        for b in blocks:
            text = b.get("content", "") or ""
            if len(text.strip()) < 20:
                # Too small → merge with next
                if buffer is None:
                    buffer = b
                else:
                    # Merge into buffer
                    buffer["content"] = (buffer.get("content", "") + " " + text).strip()
            else:
                # Normal block
                if buffer is not None:
                    # Flush buffer first
                    merged.append(buffer)
                    buffer = None
                merged.append(b)

        # Flush leftover buffer
        if buffer is not None:
            merged.append(buffer)

        return merged


    def _el3_infer_missing_headings(self, blocks: list[dict]) -> list[dict]:
        """
        Infer missing headings:
        - If a block has no heading but looks like an intro,
          assign 'Introduction'.
        - If a block has no heading but appears late,
          assign 'Conclusion'.
        - MVP heuristic: based on position only.
        """
        if not blocks:
            return blocks

        total = len(blocks)
        for i, b in enumerate(blocks):
            if b.get("heading"):
                continue

            if i == 0:
                b["heading"] = "Introduction"
            elif i == total - 1:
                b["heading"] = "Conclusion"
            else:
                b["heading"] = f"Section {i}"

        return blocks

    # ============================================
    # EDITION LOGIC V3 — CHUNK 3 (END)
    # ============================================

    # ============================================
    # EDITION LOGIC V3 — CHUNK 4 (START)
    # Ordering functions (semantic + clarity-weighted)
    # ============================================

    def _el3_semantic_order(self, blocks: list[dict]) -> list[dict]:
        """
        Semantic ordering:
        - Intro-like blocks first
        - Conclusion-like blocks last
        - Everything else stays in the middle
        MVP heuristic:
        - First block → intro
        - Last block → conclusion
        - Middle blocks remain in original order
        """
        if not blocks:
            return blocks

        ordered = []

        # Intro block
        intro = blocks[0]
        ordered.append(intro)

        # Middle blocks
        if len(blocks) > 2:
            middle = blocks[1:-1]
            ordered.extend(middle)

        # Conclusion block
        if len(blocks) > 1:
            conclusion = blocks[-1]
            ordered.append(conclusion)

        return ordered


    def _el3_clarity_weighted_order(self, blocks: list[dict]) -> list[dict]:
        """
        Clarity-weighted ordering:
        - Sort blocks by clarity score (descending)
        - But keep intro first and conclusion last
        MVP heuristic:
        - intro = first block
        - conclusion = last block
        - middle blocks sorted by clarity
        """
        if not blocks:
            return blocks

        if len(blocks) <= 2:
            return blocks

        intro = blocks[0]
        conclusion = blocks[-1]
        middle = blocks[1:-1]

        # Sort middle by clarity score (highest first)
        middle_sorted = sorted(
            middle,
            key=lambda b: b.get("clarity", 0),
            reverse=True
        )

        return [intro] + middle_sorted + [conclusion]

    # ============================================
    # EDITION LOGIC V3 — CHUNK 4 (END)
    # ============================================

    # ============================================
    # EDITION LOGIC V3 — CHUNK 5 (START)
    # Final coherence pass
    # ============================================

    def _el3_coherence_pass(self, blocks: list[dict]) -> list[dict]:
        """
        Coherence pass:
        - Remove obvious duplicate blocks
        - Remove blocks with identical content
        - Smooth transitions by ensuring each block has content
        MVP heuristic:
        - Deduplicate by content (case-insensitive)
        - Remove empty or whitespace-only blocks
        """
        if not blocks:
            return blocks

        seen = set()
        cleaned = []

        for b in blocks:
            text = (b.get("content", "") or "").strip()
            if not text:
                continue  # skip empty blocks

            key = text.lower()
            if key in seen:
                continue  # skip duplicates

            seen.add(key)
            cleaned.append(b)

        return cleaned

    # ============================================
    # EDITION LOGIC V3 — CHUNK 5 (END)
    # ============================================


    # ------------------------------------------------------------
    # EL4 — LLM rewrite layer
    # ------------------------------------------------------------
    def apply_edition_logic_v4(self, text: str) -> str:
        """
        EL4 — LLM rewrite layer.
        Takes EL3 output and rewrites it for clarity, elegance, and naturalness.
        Meaning and structure must be preserved.
        """
        prompt = (
            "Rewrite the following text to be clear, formal, natural, and elegant. "
            "Do not change the meaning. Do not add or remove information. "
            "Do not restructure beyond what is necessary for clarity.\n\n"
            f"Text:\n{text}"
        )

        rewritten = self.llm(prompt)
        return rewritten.strip()


    def llm(self, prompt: str) -> str:
        """
        EL4 local rewrite engine (combined upgrade).
        - Sentence-aware
        - Formal, clarity-focused
        - Deterministic, no external API
        """
        import re

        # 1. Extract text after "Text:" if present
        if "Text:" in prompt:
            text = prompt.split("Text:", 1)[1].strip()
        else:
            text = prompt.strip()

        if not text:
            return "[EL4 simulated rewrite]\n"

        # 2. Normalise whitespace
        text = " ".join(text.split())

        # 3. Split into sentences (very simple heuristic)
        sentences = self._el4_split_sentences(text)

        # 3b. Expand long, tangled sentences into smaller units
        expanded = []
        for s in sentences:
            parts = re.split(
                r"\b(and also|but also|but|because|so|however)\b",
                s,
                flags=re.IGNORECASE
            )
            for p in parts:
                p = p.strip()
                if p:
                    expanded.append(p)

        sentences = expanded

        # Merge micro-fragments (e.g., "But.", "So.", "Because.")
        merged = []
        buffer = ""

        for frag in sentences:
            words = frag.split()
            if len(words) <= 3:
                # accumulate micro-fragments
                buffer = (buffer + " " + frag).strip()
            else:
                if buffer:
                    merged.append((buffer + " " + frag).strip())
                    buffer = ""
                else:
                    merged.append(frag)

        if buffer:
            merged.append(buffer)

        sentences = merged

        # 4. Rewrite each sentence for clarity/formality
        rewritten_sentences = []
        for s in sentences:
            s = s.strip()
            if not s:
                continue

            # Lowercase working copy for pattern checks
            lower = s.lower()

            # --- A. Remove hedging and filler ---
            hedges = [
                "basically", "maybe", "honestly", "I was thinking that",
                "I think", "I guess", "sort of", "kind of", "I don't know"
            ]
            for h in hedges:
                if h.lower() in lower:
                    s = s.replace(h, "").strip()
                    lower = s.lower()

            # --- B. Apply phrase-level replacements ---
            replacements = {
                "we're going to": "we will",
                "we are going to": "we will",
                "we're gonna": "we will",
                "gonna": "going to",

                "a bit": "slightly",
                "sort of": "",
                "kind of": "",

                "i think": "it appears",
                "i guess": "it seems",

                "fix it": "resolve the issue",
                "sort it out": "address the issue",
                "deal with it": "address the issue",

                "start": "begin",
                "kick off": "begin",

                "give people time": "allow people time",
                "give them time": "allow them time",

                "not ideal": "suboptimal",

                "require to": "need to",

                "commence": "begin",

                "provide people time": "allow people time",

                "resolve the matter": "address the issue",

                "slightly later": "later",
                "slightly": "",
            }

            for old, new in replacements.items():
                if old.lower() in lower:
                    s = s.replace(old, new)
                    lower = s.lower()

            # 5. Remove double spaces
            s = " ".join(s.split())

            # 6. Ensure sentence starts with capital
            if s:
                s = s[0].upper() + s[1:]

            # 7. Ensure sentence ends with a period
            if not s.endswith((".", "!", "?")):
                s += "."

            rewritten_sentences.append(s)

        # 8. Remove simple repetition
        final_sentences = []
        seen = set()
        for s in rewritten_sentences:
            key = s.lower().strip()
            if key not in seen:
                seen.add(key)
                final_sentences.append(s)

        # 9. Merge short sentences into coherent paragraphs
        paragraphs = []
        current = []
        for s in final_sentences:
            if len(s) < 40:
                current.append(s)
            else:
                if current:
                    paragraphs.append(" ".join(current))
                    current = []
                paragraphs.append(s)
        if current:
            paragraphs.append(" ".join(current))

        final_text = " ".join(paragraphs).strip()

        return f"[EL4 simulated rewrite]\n{final_text}"

    # ------------------------------------------------------------
    # EL4 helpers — DIS-2 <-> text conversion
    # ------------------------------------------------------------
    def _dis2_to_text(self, dis2: dict) -> str:
            """
            Convert a DIS-2 document into plain text by concatenating
            all block contents in order.
            """
            lines = []
            for section in dis2.get("sections", []):
                for block in section.get("blocks", []):
                    content = block.get("content", "").strip()
                    if content:
                        lines.append(content)
            return "\n\n".join(lines)


    def _text_to_dis2(self, text: str) -> dict:
            """
            Convert plain rewritten text back into a minimal DIS-2 structure.
            One unnamed section, one paragraph block.
            """
            return {
                "version": "DIS-2",
                "document_clarity_score": 0,
                "sections": [
                    {
                        "heading": None,
                        "section_type": "unnamed",
                        "blocks": [
                            {
                                "content": text.strip(),
                                "block_type": "paragraph",
                                "intent": "statement",
                                "clarity_score": 0
                            }
                        ],
                        "clarity_score": 0
                    }
                ],
                "meta": {
                    "source_version": "DIS-1",
                    "validation_repairs": []
                }
            }
    def _el4_split_sentences(self, text: str) -> list[str]:
        """
        Very simple sentence splitter for EL4.
        Not perfect, but good enough for local clarity rewrites.
        """
        import re

        # Split on ., ?, ! while keeping things simple
        parts = re.split(r'([.!?])', text)
        sentences = []
        current = ""

        for part in parts:
            if not part:
                continue
            current += part
            if part in ".!?":
                sentences.append(current.strip())
                current = ""

        if current.strip():
            sentences.append(current.strip())

        return sentences
   

            

    # ------------------------------------------------------------
    # 10.1 Edition Logic v3 (expression shaping: short mode, etc.)
    # ------------------------------------------------------------

    def _el3_detect_mode(self, blocks, user_request: str):
        req = f" {(user_request or '').lower()} "

        def match(triggers):
            return any(f" {t} " in req for t in triggers)

        # --- Mode triggers ---
        clear_triggers = [
            "clear", "make it clear", "clean", "clean up", "clarify"
        ]

        precise_triggers = [
            "precise", "make it precise", "exact", "more exact", "tighten"
        ]

        simple_triggers = [
            "simple", "simpler", "make it simple",
            "easy", "easier", "plain language"
        ]

        short_triggers = [
            "short", "shorter", "brief", "condense", "summary",
            "summarise", "summarize", "tldr", "make it short"
        ]

        formal_triggers = [
            "formal", "make it formal", "professional tone",
            "business tone", "official", "corporate"
        ]

        # --- Priority order ---
        if match(clear_triggers):
            return "clear"

        if match(precise_triggers):
            return "precise"

        if match(simple_triggers):
            return "simple"

        if match(short_triggers):
            return "short"

        if match(formal_triggers):
            return "formal"

        return "default"


        def _el3_apply_short_mode(self, dis_document: dict) -> dict:
            new_sections = []

            for sec in dis_document.get("sections", []):
                blocks = sec.get("blocks", []) or []
                new_blocks = []

                for blk in blocks:
                    text = blk.get("content", "") or ""
                    if not isinstance(text, str) or not text.strip():
                        new_blocks.append(blk)
                        continue

                    sentences = [s.strip() for s in text.split(".") if s.strip()]
                    compressed = []

                    for s in sentences:
                        fillers = [
                            "in order to", "basically", "actually", "really",
                            "in fact", "as a matter of fact", "essentially",
                            "it is important to note that"
                        ]
                        for f in fillers:
                            s = s.replace(f, "")

                        if "," in s:
                            s = s.split(",")[0]

                        if s.strip():
                            compressed.append(s.strip())

                    blk["content"] = (
                        ". ".join(compressed) + "." if compressed else text
                    )
                    new_blocks.append(blk)

                sec["blocks"] = new_blocks
                new_sections.append(sec)

            dis_document["sections"] = new_sections
            return dis_document



    def _el3_apply_simple_mode(self, dis_document: dict) -> dict:
        simple_map = {
            "utilize": "use",
            "leverage": "use",
            "facilitate": "help",
            "approximately": "about",
            "demonstrate": "show",
            "indicate": "show",
            "implement": "apply",
            "methodology": "method",
            "objective": "goal",
            "commence": "start",
            "terminate": "end",
            "prioritize": "focus on",
            "significant": "important",
            "numerous": "many",
            "subsequently": "afterwards",
            "consequently": "so",
            "therefore": "so",
        }

        weak_openers = [
            "however", "moreover", "furthermore", "in addition",
            "nevertheless", "nonetheless", "consequently"
        ]

        new_sections = []

        for sec in dis_document.get("sections", []):
            blocks = sec.get("blocks", []) or []
            new_blocks = []

            for blk in blocks:
                text = blk.get("content", "") or ""
                if not isinstance(text, str) or not text.strip():
                    new_blocks.append(blk)
                    continue

                processed = text

                for complex_word, simple_word in simple_map.items():
                    processed = processed.replace(complex_word, simple_word)
                    processed = processed.replace(complex_word.capitalize(), simple_word.capitalize())

                sentences = [s.strip() for s in processed.split(".") if s.strip()]
                cleaned = []

                for s in sentences:
                    lowered = s.lower()
                    for opener in weak_openers:
                        if lowered.startswith(opener + " "):
                            s = s[len(opener) + 1:].strip()
                    cleaned.append(s)

                blk["content"] = ". ".join(cleaned) + "."
                new_blocks.append(blk)

            sec["blocks"] = new_blocks
            new_sections.append(sec)

        dis_document["sections"] = new_sections
        return dis_document


    def _el3_apply_clear_mode(self, dis_document: dict) -> dict:
        hedges = [
            "kind of", "sort of", "maybe", "perhaps", "possibly",
            "it seems", "it appears", "i think", "i believe",
            "in my opinion", "should be noted that"
        ]

        weak_words = [
            "very", "really", "quite", "somewhat", "fairly",
            "basically", "actually", "literally"
        ]

        redundant_openers = [
            "in conclusion", "to summarize", "overall", "in summary"
        ]

        new_sections = []

        for sec in dis_document.get("sections", []):
            blocks = sec.get("blocks", []) or []
            new_blocks = []

            for blk in blocks:
                text = blk.get("content", "") or ""
                if not isinstance(text, str) or not text.strip():
                    new_blocks.append(blk)
                    continue

                processed = text

                for h in hedges:
                    processed = processed.replace(h, "")

                for w in weak_words:
                    processed = processed.replace(" " + w + " ", " ")

                sentences = [s.strip() for s in processed.split(".") if s.strip()]
                cleaned = []

                for s in sentences:
                    lowered = s.lower()
                    for opener in redundant_openers:
                        if lowered.startswith(opener + " "):
                            s = s[len(opener) + 1:].strip()
                    cleaned.append(s)

                blk["content"] = ". ".join(cleaned) + "."
                new_blocks.append(blk)

            sec["blocks"] = new_blocks
            new_sections.append(sec)

        dis_document["sections"] = new_sections
        return dis_document


    def _el3_apply_precise_mode(self, dis_document: dict) -> dict:
        vague_terms = [
            "things", "stuff", "various", "several", "some", "a bit",
            "a number of", "kind of", "sort of", "aspects", "areas", "issues"
        ]

        weak_verbs = {
            "do": "perform",
            "make": "create",
            "get": "obtain",
            "put": "place",
            "show": "demonstrate",
            "use": "apply",
        }

        soft_quantifiers = [
            "somewhat", "slightly", "fairly", "relatively", "kind of", "sort of"
        ]

        new_sections = []

        for sec in dis_document.get("sections", []):
            blocks = sec.get("blocks", []) or []
            new_blocks = []

            for blk in blocks:
                text = blk.get("content", "") or ""
                if not isinstance(text, str) or not text.strip():
                    new_blocks.append(blk)
                    continue

                processed = text

                for term in vague_terms:
                    processed = processed.replace(term, "")

                for weak, strong in weak_verbs.items():
                    processed = processed.replace(f" {weak} ", f" {strong} ")
                    processed = processed.replace(f" {weak.capitalize()} ", f" {strong.capitalize()} ")

                for q in soft_quantifiers:
                    processed = processed.replace(q, "")

                processed = " ".join(processed.split())

                blk["content"] = processed
                new_blocks.append(blk)

            sec["blocks"] = new_blocks
            new_sections.append(sec)

        dis_document["sections"] = new_sections
        return dis_document
    
            

    # ------------------------------------------------------------
    # 10.2 DIS-1 → DIS-2 upgrade layer
    # ------------------------------------------------------------
    def upgrade_to_dis2(self, dis_document: dict) -> dict:
        sections_in = dis_document.get("sections", []) or []
        sections_out: list[dict] = []

        for s in sections_in:
            heading = self._el2_get_heading(s)
            blocks_in = s.get("blocks", []) or []

            if heading and self._el2_is_intro(heading):
                section_type = "introduction"
            elif heading and self._el2_is_conclusion(heading):
                section_type = "conclusion"
            elif heading and self._el2_is_definition(heading):
                section_type = "definition"
            elif heading:
                section_type = "body"
            else:
                section_type = "unnamed"

            blocks_out: list[dict] = []
            for b in blocks_in:
                raw_type = b.get("type") or "paragraph"
                if raw_type in ("paragraph", "text"):
                    block_type = "paragraph"
                elif raw_type in ("bullet", "bullet_group", "list"):
                    block_type = "list"
                elif raw_type in ("heading", "title"):
                    block_type = "heading"
                else:
                    block_type = "paragraph"

                b2 = dict(b)
                b2["block_type"] = block_type
                blocks_out.append(b2)

            section_clarity = self._compute_section_clarity(blocks_out)

            sections_out.append(
                {
                    "heading": heading or None,
                    "section_type": section_type,
                    "blocks": blocks_out,
                    "clarity_score": section_clarity,
                }
            )

        doc_clarity = self._compute_document_clarity(
            [b for s in sections_out for b in s.get("blocks", [])]
        )

        return {
            "version": "DIS-2",
            "document_clarity_score": doc_clarity,
            "sections": sections_out,
            "meta": {
                "source_version": dis_document.get("version", "DIS-1"),
                "validation_repairs": [],
            },
        }

    # ------------------------------------------------------------
    # 11. DIS-2 strict validation (with clamping + repair metadata)
    # ------------------------------------------------------------
    def validate_dis2(self, dis2_document: dict) -> dict:
        doc = dict(dis2_document) if dis2_document is not None else {}
        repairs: list[dict] = []

        if "version" not in doc:
            repairs.append(
                {"level": "document", "field": "version", "action": "added", "value": "DIS-2"}
            )
            doc["version"] = "DIS-2"
        if doc.get("version") != "DIS-2":
            repairs.append(
                {
                    "level": "document",
                    "field": "version",
                    "action": "normalized",
                    "original": doc.get("version"),
                    "value": "DIS-2",
                }
            )
            doc["version"] = "DIS-2"

        sections = doc.get("sections")
        if not isinstance(sections, list):
            repairs.append(
                {
                    "level": "document",
                    "field": "sections",
                    "action": "normalized",
                    "original": sections,
                    "value": [],
                }
            )
            sections = []
        validated_sections: list[dict] = []

        for idx, s in enumerate(sections):
            vs, s_repairs = self._validate_dis2_section(s, idx)
            validated_sections.append(vs)
            repairs.extend(s_repairs)

        doc["sections"] = validated_sections

        all_blocks = [b for s in validated_sections for b in s.get("blocks", [])]
        doc_clarity_raw = self._compute_document_clarity(all_blocks)
        doc_clarity, clarity_repairs = self._normalize_clarity_score(
            doc.get("document_clarity_score"), doc_clarity_raw, level="document"
        )
        if clarity_repairs:
            repairs.extend(clarity_repairs)
        doc["document_clarity_score"] = doc_clarity

        meta = doc.get("meta") or {}
        existing_repairs = meta.get("validation_repairs") or []
        meta["validation_repairs"] = existing_repairs + repairs
        doc["meta"] = meta

        return doc

    def _validate_dis2_section(self, section: dict, index: int) -> tuple[dict, list[dict]]:
        repairs: list[dict] = []
        s = dict(section) if section is not None else {}

        heading = s.get("heading")
        if heading is not None and not isinstance(heading, str):
            repairs.append(
                {
                    "level": "section",
                    "index": index,
                    "field": "heading",
                    "action": "normalized",
                    "original": heading,
                    "value": str(heading),
                }
            )
            heading = str(heading)
        s["heading"] = heading if heading else None

        section_type = s.get("section_type")
        valid_types = {"introduction", "definition", "body", "conclusion", "unnamed"}
        if section_type not in valid_types:
            original = section_type
            h = (heading or "").strip()
            if h and self._el2_is_intro(h):
                section_type = "introduction"
            elif h and self._el2_is_conclusion(h):
                section_type = "conclusion"
            elif h and self._el2_is_definition(h):
                section_type = "definition"
            elif h:
                section_type = "body"
            else:
                section_type = "unnamed"
            repairs.append(
                {
                    "level": "section",
                    "index": index,
                    "field": "section_type",
                    "action": "normalized",
                    "original": original,
                    "value": section_type,
                }
            )
        s["section_type"] = section_type

        blocks = s.get("blocks")
        if not isinstance(blocks, list):
            repairs.append(
                {
                    "level": "section",
                    "index": index,
                    "field": "blocks",
                    "action": "normalized",
                    "original": blocks,
                    "value": [],
                }
            )
            blocks = []
        validated_blocks: list[dict] = []
        for b_idx, b in enumerate(blocks):
            vb, b_repairs = self._validate_dis2_block(b, index, b_idx)
            validated_blocks.append(vb)
            repairs.extend(b_repairs)
        s["blocks"] = validated_blocks

        section_clarity_raw = self._compute_section_clarity(validated_blocks)
        section_clarity, clarity_repairs = self._normalize_clarity_score(
            s.get("clarity_score"),
            section_clarity_raw,
            level="section",
            index=index,
        )
        if clarity_repairs:
            repairs.extend(clarity_repairs)
        s["clarity_score"] = section_clarity

        return s, repairs

    def _validate_dis2_block(
        self, block: dict, section_index: int, block_index: int
    ) -> tuple[dict, list[dict]]:
        repairs: list[dict] = []
        b = dict(block) if block is not None else {}

        content = b.get("content")
        if content is None:
            repairs.append(
                {
                    "level": "block",
                    "section_index": section_index,
                    "block_index": block_index,
                    "field": "content",
                    "action": "added",
                    "value": "",
                }
            )
            content = ""
        elif not isinstance(content, str):
            repairs.append(
                {
                    "level": "block",
                    "section_index": section_index,
                    "block_index": block_index,
                    "field": "content",
                    "action": "normalized",
                    "original": content,
                    "value": str(content),
                }
            )
            content = str(content)
        b["content"] = content

        block_type = b.get("block_type") or b.get("type") or "paragraph"
        if block_type not in ("paragraph", "list", "heading"):
            repairs.append(
                {
                    "level": "block",
                    "section_index": section_index,
                    "block_index": block_index,
                    "field": "block_type",
                    "action": "normalized",
                    "original": block_type,
                    "value": "paragraph",
                }
            )
            block_type = "paragraph"
        b["block_type"] = block_type

        clarity_raw = b.get("clarity_score")
        clarity, clarity_repairs = self._normalize_clarity_score(
            clarity_raw,
            default=60,
            level="block",
            section_index=section_index,
            block_index=block_index,
        )
        if clarity_repairs:
            repairs.extend(clarity_repairs)
        b["clarity_score"] = clarity

        return b, repairs

    def _normalize_clarity_score(
        self,
        value,
        default: int | float = 0,
        level: str = "document",
        index: int | None = None,
        section_index: int | None = None,
        block_index: int | None = None,
    ) -> tuple[int, list[dict]]:
        repairs: list[dict] = []

        def make_ctx():
            ctx = {"level": level}
            if index is not None:
                ctx["index"] = index
            if section_index is not None:
                ctx["section_index"] = section_index
            if block_index is not None:
                ctx["block_index"] = block_index
            return ctx

        if not isinstance(value, (int, float)):
            if value is not None:
                r = make_ctx()
                r.update(
                    {
                        "field": "clarity_score",
                        "action": "normalized_type",
                        "original": value,
                        "value": default,
                    }
                )
                repairs.append(r)
            score = float(default)
        else:
            score = float(value)

        original_score = score
        if score < 0:
            r = make_ctx()
            r.update(
                {
                    "field": "clarity_score",
                    "action": "clamped_min",
                    "original": original_score,
                    "value": 0,
                }
            )
            repairs.append(r)
            score = 0.0
        elif score > 100:
            r = make_ctx()
            r.update(
                {
                    "field": "clarity_score",
                    "action": "clamped_max",
                    "original": original_score,
                    "value": 100,
                }
            )
            repairs.append(r)
            score = 100.0

        return int(score), repairs
    
    def detect_blocks_v2(self, raw_lines: list[str]) -> list[dict]:
        """
        Block Detection v2:
        - Groups consecutive non-empty lines into paragraph blocks.
        - Preserves list items as list blocks.
        - Ignores empty lines.
        """

        blocks = []
        current_block = []

        def flush_paragraph():
            if current_block:
                blocks.append({
                    "block_type": "paragraph",
                    "content": " ".join(current_block).strip()
                })
                current_block.clear()

        for line in raw_lines:
            stripped = line.strip()

            # List item
            if stripped.startswith(("-", "*")):
                flush_paragraph()
                blocks.append({
                    "block_type": "list",
                    "content": stripped
                })
                continue

            # Empty line → end paragraph
            if not stripped:
                flush_paragraph()
                continue

            # Normal paragraph line
            current_block.append(stripped)

        # Flush final block
        flush_paragraph()

        return blocks



# ------------------------------------------------------------
# 12. Pipeline integration (returns validated DIS-2 document)
# ------------------------------------------------------------
    def run(self, input_data: str, user_request: str = None):

        import inspect
        print(">>> USING SIMPLEENGINE FROM:", inspect.getfile(self.__class__))

        # Early normalization
        input_data = self.normalize_headings(input_data)
        input_data = self.group_bullets(input_data)

        # Section + block detection
        sections_raw = self.split_into_sections(input_data)

        blocks = []
        for sec in sections_raw:
            raw_lines = [l for l in sec["raw_lines"] if l.strip()]
            sec_blocks = self.detect_blocks_v2(raw_lines)

            for b in sec_blocks:
                b["heading"] = sec["heading"]

            blocks.extend(sec_blocks)

        # Chunking
        chunks = self.chunk_blocks(blocks)

        # Intent detection
        chunks = self.detect_intents(chunks)

        # Clarity scoring
        chunks = self.score_clarity(chunks)

        # Assemble DIS-1
        dis_document = self.assemble_output(chunks)

        # Edition Logic v2 (structural)
        dis_document = self.apply_edition_logic_v2(dis_document)

        # Edition Logic v3 (expression shaping)
        context = {"user_request": user_request}
        edited_document = self.apply_edition_logic_v3(dis_document, context)

        # DIS-1 → DIS-2 upgrade
        dis2_document = self.upgrade_to_dis2(edited_document)

        # Strict DIS-2 validation
        dis2_document = self.validate_dis2(dis2_document)

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # >>> INSERT EL4 HERE — AFTER EL3, AFTER DIS-2 VALIDATION <<<
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        if user_request == "formal":
            # Convert DIS-2 → plain text
            text = self._dis2_to_text(dis2_document)

            # Rewrite using EL4
            rewritten = self.apply_edition_logic_v4(text)

        # Convert rewritten text → DIS-2 again
        dis2_document = self._text_to_dis2(rewritten)

# ============================================
# COMPOSITE TEST — FULL ENGINE PIPELINE (START)
# ============================================

    def run_composite_test(self, text: str) -> dict:
        """
        Full pipeline test:
        1. Raw text → DIS-1
        2. EL2 structural shaping
        3. EL3 expression shaping
        4. DIS-2 upgrade + validation
        5. EL4 rewrite
        """

        # --- 1. Build DIS-1 document ---
        dis1 = {
            "sections": [
                {
                    "heading": None,
                    "blocks": [
                        {
                            "block_type": "paragraph",
                            "content": s.strip(),
                            "heading": None,
                            "clarity_score": 0.5,
                            "complexity": 0.5,
                        }
                        for s in text.split(".") if s.strip()
                    ]
                }
            ]
        }


        # --- 2. EL2 structural shaping ---
        dis1 = self.apply_edition_logic_v2(dis1)

        # --- 3. EL3 expression shaping ---
        flat_blocks = dis1["sections"][0]["blocks"]
        flat_blocks = self.apply_edition_logic_v3(flat_blocks, user_request=text)
        dis1["sections"][0]["blocks"] = flat_blocks


        # --- 4. DIS-2 upgrade + validation ---
        dis2 = self.upgrade_to_dis2(dis1)
        dis2 = self.validate_dis2(dis2)

        # --- 5. EL4 rewrite layer ---
        plain = self._dis2_to_text(dis2)
        rewritten = self.apply_edition_logic_v4(plain)
        rewritten_dis2 = self._text_to_dis2(rewritten)

        return {
            "input_text": text,
            "dis1_document": dis1,
            "dis2_document": dis2,
            "rewritten_text": rewritten,
            "rewritten_dis2": rewritten_dis2,
            "final_text": rewritten,   # ← this is the one your test expects
        }


# ============================================
# COMPOSITE TEST — FULL ENGINE PIPELINE (END)
# ============================================
