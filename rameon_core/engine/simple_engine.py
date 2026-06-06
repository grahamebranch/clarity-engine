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

    # ------------------------------------------------------------
    # 2. Early normalization
    # ------------------------------------------------------------
    def normalize_headings(self, text: str) -> str:
        """
        MVP: simple normalization placeholder.
        In your real version, keep your existing implementation.
        """
        # Example: normalise line endings and strip trailing spaces
        lines = [line.rstrip() for line in text.splitlines()]
        return "\n".join(lines)

    def group_bullets(self, text: str) -> str:
        """
        MVP: placeholder that returns text unchanged.
        Keep/replace with your real bullet-grouping logic.
        """
        return text

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
            # Neutral placeholder score
            c["clarity_score"] = 60
        return chunks

    # ------------------------------------------------------------
    # 7. DIS assembly
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

        # Recompute document-level clarity
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
            # Ensure last is conclusion-like if possible
            if not self._el2_is_conclusion(self._el2_get_heading(sections[-1])):
                for i, s in enumerate(sections[:-1]):
                    if self._el2_is_conclusion(self._el2_get_heading(s)):
                        sections.append(sections.pop(i))
                        break

        return sections

    # ------------------------------------------------------------
    # 10. Pipeline integration (returns DIS document)
    # ------------------------------------------------------------
    def run(self, input_data: str):
        """
        Full MVP pipeline → returns a DIS document (after pipeline).
        """

        # Early normalization
        input_data = self.normalize_headings(input_data)
        input_data = self.group_bullets(input_data)

        # Block detection
        blocks = self.detect_blocks(input_data)

        # Chunking
        chunks = self.chunk_blocks(blocks)

        # Intent detection
        chunks = self.detect_intents(chunks)

        # Clarity scoring
        chunks = self.score_clarity(chunks)

        # Assemble DIS
        dis_document = self.assemble_output(chunks)

        # Edition Logic v1 (cleanup)
        edited_document = self.apply_edition_logic(dis_document)

        # Edition Logic v2 (structure + semantics + clarity shaping)
        edited_document = self.apply_edition_logic_v2(edited_document)

        # Pass through pipeline
        return self.pipeline.run(edited_document)
