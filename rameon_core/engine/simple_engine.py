from .engine import Engine
from .context import EngineContext
from .pipeline import Pipeline
import re


class SimpleEngine(Engine):
    def __init__(self):
        self.pipeline = Pipeline()

    def load(self, config):
        # MVP: no external config yet
        pass

    # ------------------------------------------------------------
    # 1. Heading normalisation
    # ------------------------------------------------------------
    def normalize_headings(self, text: str) -> str:
        """
        Normalise markdown-style headings so they are consistent and easy to detect.
        """
        lines = text.split("\n")
        normalized = []

        for line in lines:
            stripped = line.lstrip()
            if stripped.startswith("#"):
                match = re.match(r"(#+)(.*)", stripped)
                if match:
                    hashes, rest = match.groups()
                    normalized.append(f"{hashes} {rest.strip()}")
                else:
                    normalized.append(stripped)
            else:
                normalized.append(line)

        return "\n".join(normalized)

    # ------------------------------------------------------------
    # 2. Bullet grouping
    # ------------------------------------------------------------
    def group_bullets(self, text: str) -> str:
        """
        Group consecutive bullet lines into single logical bullet blocks.
        """
        lines = text.split("\n")
        grouped = []
        buffer = []

        def flush():
            nonlocal buffer, grouped
            if buffer:
                grouped.append("\n".join(buffer))
                buffer = []

        for line in lines:
            stripped = line.strip()
            if stripped.startswith(("-", "*", "•")):
                buffer.append(stripped)
            else:
                flush()
                grouped.append(line)

        flush()
        return "\n".join(grouped)

    # ------------------------------------------------------------
    # 3. Block detection
    # ------------------------------------------------------------
    def detect_blocks(self, text: str):
        """
        Turn lines into typed blocks: heading, bullet_group, paragraph.
        """
        lines = text.split("\n")
        blocks = []

        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue

            if stripped.startswith("#"):
                blocks.append({
                    "type": "heading",
                    "content": stripped
                })
            elif stripped.startswith(("-", "*", "•")) or "\n" in line:
                # After grouping, bullets may be multi-line joined with \n
                blocks.append({
                    "type": "bullet_group",
                    "content": stripped
                })
            else:
                blocks.append({
                    "type": "paragraph",
                    "content": stripped
                })

        return blocks

    # ------------------------------------------------------------
    # 4. Chunking
    # ------------------------------------------------------------
    def chunk_blocks(self, blocks):
        """
        Group blocks into chunks, each optionally headed by a heading block.
        """
        chunks = []
        current_chunk = {
            "heading": None,
            "blocks": []
        }

        def flush():
            nonlocal current_chunk, chunks
            if current_chunk["heading"] is not None or current_chunk["blocks"]:
                chunks.append(current_chunk)
            current_chunk = {
                "heading": None,
                "blocks": []
            }

        for block in blocks:
            if block["type"] == "heading":
                # Start a new chunk at each heading
                flush()
                current_chunk["heading"] = block["content"]
            else:
                current_chunk["blocks"].append(block)

        flush()
        return chunks

    # ------------------------------------------------------------
    # 5. Intent detection (MVP heuristic)
    # ------------------------------------------------------------
    def detect_intents(self, chunks):
        """
        Assign a simple intent label to each chunk based on its content.
        """
        for chunk in chunks:
            blocks = chunk["blocks"]
            has_bullets = any(b["type"] == "bullet_group" for b in blocks)

            if has_bullets:
                intent = "list"
            elif chunk["heading"]:
                intent = "section"
            else:
                intent = "paragraph"

            chunk["intent"] = intent

        return chunks

    # ------------------------------------------------------------
    # 6. Clarity scoring (0–100, deterministic)
    # ------------------------------------------------------------
    def score_clarity(self, chunks):
        """
        Deterministic clarity scoring for MVP.
        Produces a 0–100 clarity score per chunk.
        """
        JARGON = {"utilize", "leverage", "synergy", "paradigm", "framework"}

        for chunk in chunks:
            # Concatenate all block contents
            text = "\n".join(b["content"] for b in chunk["blocks"]).strip()
            words = text.split()
            word_count = len(words)

            score = 100

            # Penalty: long text (very rough proxy for long sentences)
            if word_count > 40:
                score -= min(40, (word_count - 40))

            # Penalty: jargon
            jargon_hits = sum(1 for w in words if w.lower().strip(".,!?;:") in JARGON)
            score -= jargon_hits * 5

            # Bonus: bullet lists are clearer
            if any(b["type"] == "bullet_group" for b in chunk["blocks"]):
                score += 10

            # Bonus: heading present
            if chunk["heading"]:
                score += 5

            # Clamp score
            score = max(0, min(100, score))

            chunk["clarity_score"] = score

        return chunks

     # ------------------------------------------------------------
    # 7. Final assembly (DIS document)
    # ------------------------------------------------------------
    def apply_edition_logic(self, dis_document: dict) -> dict:
         ...

        """
        Build a minimal DIS (Document Interpretation Structure) object.
        This is the canonical document model for all downstream systems.
        """

        # Compute document-level clarity score (simple average)
        clarity_scores = [
            c.get("clarity_score", 0)
            for c in chunks
        ]
        document_clarity = int(sum(clarity_scores) / len(clarity_scores)) if clarity_scores else 0

        dis_document = {
            "version": "DIS-1",
            "document_clarity_score": document_clarity,
            "sections": []
        }

        for chunk in chunks:
            section = {
                "heading": chunk.get("heading"),
                "intent": chunk.get("intent"),
                "clarity_score": chunk.get("clarity_score"),
                "blocks": [
                    {
                        "type": b["type"],
                        "content": b["content"]
                    }
                    for b in chunk["blocks"]
                ]
            }
            dis_document["sections"].append(section)

        return dis_document

    # ------------------------------------------------------------
    # 8. Pipeline integration (returns DIS document)
    # ------------------------------------------------------------
    def run(self, input_data: str):
        """
        Full MVP pipeline → returns a DIS document.
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

        dis_document = self.assemble_output(chunks)
        edited_document = self.apply_edition_logic(dis_document)
        return self.pipeline.run(edited_document)

