import re

from .engine import Engine
from .context import EngineContext
from .pipeline import Pipeline


class SimpleEngine(Engine):
    def __init__(self):
        self.pipeline = Pipeline()
        self.config: dict = {}

    # ------------------------------------------------------------
    # 1. Load configuration
    # ------------------------------------------------------------
    def load(self, config: dict | None = None):
        """
        Load engine configuration (MVP: just store it).
        """
        self.config = config or {}

    def shutdown(self):
        pass

    # ------------------------------------------------------------
    # 2. Early normalization
    # ------------------------------------------------------------
    def normalize_headings(self, text: str) -> str:
        """
        MVP: simple normalization placeholder.
        In your real version, keep your existing implementation.
        """
        lines = [line.rstrip() for line in text.splitlines()]
        return "\n".join(lines)

    def group_bullets(self, text: str) -> str:
        # TODO: keep your real implementation here
        return text


    # ------------------------------------------------------------
    # 2b. Heading detection + section splitting
    # ------------------------------------------------------------
    def is_heading(self, line: str) -> bool:
        ... (paste full method here)

    def split_into_sections(self, text: str) -> list[dict]:
        ... (paste full method here)

    # ------------------------------------------------------------
    # 3. Block detection
    # ------------------------------------------------------------
    def detect_blocks(self, text: str) -> list[dict]:

        """
        MVP block detection: split on blank lines into paragraph blocks.
        Replace with your real block detection if you already have it.
        """
        blocks: list[dict] = []
        current: list[str] = []

        def flush():
            if current:
                content = "\n".join(current).strip()
                if content:
                    blocks.append(
                        {
                            "type": "paragraph",
                            "content": content,
                        }
                    )
                current.clear()

        for line in text.splitlines():
            if line.strip():
                current.append(line)
            else:
                flush()
        flush()
        return blocks

    # ------------------------------------------------------------
    # 4. Chunking
    # ------------------------------------------------------------
    def chunk_blocks(self, blocks: list[dict]) -> list[dict]:
        """
        MVP chunking: one chunk per block.
        """
        chunks: list[dict] = []
        for i, b in enumerate(blocks):
            chunks.append(
                {
                    "id": f"chunk-{i+1}",
                    "text": b.get("content", ""),
                    "block_type": b.get("type", "paragraph"),
                }
            )
        return chunks

    # ------------------------------------------------------------
    # 5. Intent detection
    # ------------------------------------------------------------
    def detect_intents(self, chunks: list[dict]) -> list[dict]:
        """
        MVP intent detection: assign a generic intent.
        Replace with your real intent model when ready.
        """
        for c in chunks:
            c["intent"] = "statement"
        return chunks

    # ------------------------------------------------------------
    # 6. Clarity scoring
    # ------------------------------------------------------------
    def score_clarity(self, chunks: list[dict]) -> list[dict]:
        """
        MVP clarity scoring: assign a neutral clarity score.
        Replace with your real scoring logic.
        """
        for c in chunks:
            c["clarity_score"] = 60
        return chunks

    # ------------------------------------------------------------
    # 7. DIS-1 assembly
    # ------------------------------------------------------------
    def assemble_output(self, chunks: list[dict]) -> dict:
        """
        Assemble a minimal DIS-1 document from chunks.
        MVP: single section containing all chunks as blocks.
        """
        blocks = []
        for c in chunks:
            blocks.append(
                {
                    "type": c.get("block_type", "paragraph"),
                    "content": c.get("text", ""),
                    "intent": c.get("intent"),
                    "clarity_score": c.get("clarity_score"),
                }
            )

        dis_document = {
            "version": "DIS-1",
            "document_clarity_score": self._compute_document_clarity(blocks),
            "sections": [
                {
                    "heading": None,
                    "blocks": blocks,
                    "clarity_score": self._compute_section_clarity(blocks),
                }
            ],
        }
        return dis_document

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
    # 8. Edition Logic v1 (cleanup)
    # ------------------------------------------------------------
    def apply_edition_logic(self, dis_document: dict) -> dict:
        """
        EL-1: light cleanup on DIS.
        MVP: remove empty blocks and empty sections.
        """
        sections = []
        for s in dis_document.get("sections", []):
            blocks = s.get("blocks", []) or []
            cleaned_blocks = []
            for b in blocks:
                content = b.get("content")
                if isinstance(content, str) and content.strip():
                    cleaned_blocks.append(b)
            if cleaned_blocks:
                s2 = dict(s)
                s2["blocks"] = cleaned_blocks
                s2["clarity_score"] = self._compute_section_clarity(cleaned_blocks)
                sections.append(s2)

        if not sections:
            sections = [
                {
                    "heading": None,
                    "blocks": [],
                    "clarity_score": 0,
                }
            ]

        doc_clarity = self._compute_document_clarity(
            [b for s in sections for b in s.get("blocks", [])]
        )

        return {
            "version": dis_document.get("version", "DIS-1"),
            "document_clarity_score": doc_clarity,
            "sections": sections,
        }

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
                b.get("content", "") for b in blocks
                if isinstance(b.get("content"), str)
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

    def _el2_final_coherence_pass(self, sections: list[dict]) -> list[dict]:
        if not sections:
            return sections

        for s in sections:
            score = s.get("clarity_score")
            if isinstance(score, (int, float)) and score <= 20:
                s["needs_revision"] = True

        cleaned: list[dict] = []
        last_heading = None
        for s in sections:
            heading = self._el2_get_heading(s)
            if heading and heading == last_heading:
                if cleaned:
                    cleaned[-1]["blocks"].extend(s.get("blocks", []) or [])
                continue
            cleaned.append(s)
            if heading:
                last_heading = heading

        sections = cleaned

        if len(sections) >= 2:
            if not self._el2_is_conclusion(self._el2_get_heading(sections[-1])):
                for i, s in enumerate(sections[:-1]):
                    if self._el2_is_conclusion(self._el2_get_heading(s)):
                        sections.append(sections.pop(i))
                        break

        return sections

    # ------------------------------------------------------------
    # 10. DIS-1 → DIS-2 upgrade layer
    # ------------------------------------------------------------
    def upgrade_to_dis2(self, dis_document: dict) -> dict:
        """
        Upgrade DIS-1 to DIS-2: add stable section/block types and metadata.
        """
        sections_in = dis_document.get("sections", []) or []
        sections_out: list[dict] = []

        for s in sections_in:
            heading = self._el2_get_heading(s)
            blocks_in = s.get("blocks", []) or []

            # classify section type
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
        """
        Strict DIS-2 validation:
        - ensures required keys
        - enforces shapes
        - clamps clarity scores to 0–100
        - records all repairs in meta['validation_repairs'].
        """
        doc = dict(dis2_document) if dis2_document is not None else {}
        repairs: list[dict] = []

        # Ensure top-level keys
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

        # Recompute and clamp document clarity
        all_blocks = [b for s in validated_sections for b in s.get("blocks", [])]
        doc_clarity_raw = self._compute_document_clarity(all_blocks)
        doc_clarity, clarity_repairs = self._normalize_clarity_score(
            doc.get("document_clarity_score"), doc_clarity_raw, level="document"
        )
        if clarity_repairs:
            repairs.extend(clarity_repairs)
        doc["document_clarity_score"] = doc_clarity

        # Attach/extend meta.validation_repairs
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
            # Reclassify based on heading if needed
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

        # Recompute and clamp section clarity
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
        """
        Clamp clarity scores to 0–100 and record any repairs.
        """
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

    # ------------------------------------------------------------
    # 12. Pipeline integration (returns validated DIS-2 document)
    # ------------------------------------------------------------
    def run(self, input_data: str):
        """
        Full MVP pipeline → returns a validated DIS-2 document.
        """

        # Early normalization
        input_data = self.normalize_headings(input_data)
        input_data = self.group_bullets(input_data)

        # Section + block detection
        sections_raw = self.split_into_sections(input_data)

        blocks = []
        for sec in sections_raw:
            sec_blocks = self.detect_blocks("\n".join(sec["raw_lines"]))
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

        # Edition Logic v1 (cleanup)
        edited_document = self.apply_edition_logic(dis_document)

        # Edition Logic v2 (structure + semantics + clarity shaping)
        edited_document = self.apply_edition_logic_v2(edited_document)

        # DIS-1 → DIS-2 upgrade
        dis2_document = self.upgrade_to_dis2(edited_document)

        # Strict DIS-2 validation (with clamping + repair metadata)
        dis2_document = self.validate_dis2(dis2_document)

        # Pass through pipeline
        return self.pipeline.run(dis2_document)
