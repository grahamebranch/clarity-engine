from .engine import Engine
from .context import EngineContext
from .pipeline import Pipeline
import re


class SimpleEngine(Engine):
    def __init__(self):
        self.pipeline = Pipeline()

    def load(self, config):
        pass

    # ------------------------------------------------------------
    # 1. Heading Normalisation
    # ------------------------------------------------------------
    def normalize_headings(self, text):
        lines = text.split("\n")
        normalized = []

        for line in lines:
            stripped = line.lstrip()
            if stripped.startswith("#"):
                # Collapse multiple # into a single space after them
                hashes, rest = re.match(r"(#+)(.*)", stripped).groups()
                normalized.append(f"{hashes} {rest.strip()}")
            else:
                normalized.append(line)

        return "\n".join(normalized)

    # ------------------------------------------------------------
    # 2. Bullet Grouping
    # ------------------------------------------------------------
    def group_bullets(self, text):
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
    # 3. Block Detection
    # ------------------------------------------------------------
    def detect_blocks(self, text):
        lines = text.split("\n")
        blocks = []
        current = []

        def flush():
            nonlocal current, blocks
            if current:
                blocks.append("\n".join(current))
                current = []

        for line in lines:
            if line.strip() == "":
                flush()
            else:
                current.append(line)

        flush()
        return blocks

    # ------------------------------------------------------------
    # 4. Chunking
    # ------------------------------------------------------------
    def chunk_blocks(self, blocks):
        chunks = []
        for block in blocks:
            chunks.append({"text": block, "intent": None, "score": None})
        return chunks

    # ------------------------------------------------------------
    # 5. Intent Detection (MVP heuristic)
    # ------------------------------------------------------------
    def detect_intents(self, chunks):
        for c in chunks:
            text = c["text"].lower()
            if text.startswith("#"):
                c["intent"] = "heading"
            elif text.startswith(("-", "*", "•")):
                c["intent"] = "list"
            else:
                c["intent"] = "paragraph"
        return chunks

    # ------------------------------------------------------------
    # 6. Clarity Scoring (MVP heuristic)
    # ------------------------------------------------------------
    def score_clarity(self, chunks):
        for c in chunks:
            text = c["text"]
            sentences = re.split(r"(?<=[.!?]) +", text.strip())
            c["score"] = len(sentences)
        return chunks

    # ------------------------------------------------------------
    # 7. Final Assembly
    # ------------------------------------------------------------
    def assemble_output(self, chunks):
        out = []
        for c in chunks:
            out.append(c["text"])
        return "\n\n".join(out)

    # ------------------------------------------------------------
    # 8. Pipeline Integration
    # ------------------------------------------------------------
    def run(self, input_data):
        # Early normalization
        input_data = self.normalize_headings(input_data)
        input_data = self.group_bullets(input_data)

        # Block detection BEFORE sentence splitting
        blocks = self.detect_blocks(input_data)

        # Chunking
        chunks = self.chunk_blocks(blocks)

        # Intent detection
        chunks = self.detect_intents(chunks)

        # Clarity scoring (sentence splitting happens inside scoring)
        chunks = self.score_clarity(chunks)

        # Final assembly
        final_output = self.assemble_output(chunks)

        return self.pipeline.run(final_output)
