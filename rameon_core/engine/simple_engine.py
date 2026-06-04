from .engine import Engine
from .context import EngineContext
from .pipeline import Pipeline


class SimpleEngine(Engine):
    def __init__(self):
        self.pipeline = Pipeline()

    def load(self, config):
        pass

    def run(self, input_data):
        input_data = self.normalize_headings(input_data)
        input_data = self.group_bullets(input_data)
        input_data = self.split_sentences(input_data)
        input_data = self.normalize_tokens(input_data)

        blocks = self.detect_blocks(input_data)
        chunks = self.chunk_blocks(blocks)
        chunks = self.detect_intents(chunks)
        chunks = self.score_clarity(chunks)

        final_output = self.assemble_output(chunks)

        return self.pipeline.run(final_output)


    def shutdown(self):
        pass

    def normalize_headings(self, text):
        lines = text.split("\n")
        normalized = []

        for line in lines:
            stripped = line.lstrip()
            if stripped.startswith("#"):
                parts = stripped.split()
                hashes = parts[0]
                title = " ".join(parts[1:])
                normalized.append(f"{hashes} {title}")
            else:
                normalized.append(line)

        return "\n".join(normalized)

    def group_bullets(self, text):
        lines = text.split("\n")
        grouped = []
        buffer = []

        for line in lines:
            stripped = line.lstrip()

            if stripped.startswith("- "):
                buffer.append(line)
            else:
                if buffer:
                    grouped.append("\n".join(buffer))
                    buffer = []
                grouped.append(line)

        if buffer:
            grouped.append("\n".join(buffer))

        return "\n".join(grouped)

    def split_sentences(self, text):
        import re
        pattern = r'(?<=[.!?])\s+'
        parts = re.split(pattern, text)
        parts = [p.strip() for p in parts if p.strip()]
        return "\n".join(parts)

    def normalize_tokens(self, text):
        import re

        lines = text.split("\n")
        normalised_lines = []

        for line in lines:
            # work at token level but return a sentence string
            tokens = line.split()

            cleaned_tokens = []
            for t in tokens:
                # lowercase
                t = t.lower()
                # strip leading/trailing non-word chars (simple, deterministic)
                t = re.sub(r"^[^\w]+|[^\w]+$", "", t)
                if t:
                    cleaned_tokens.append(t)

            normalised_lines.append(" ".join(cleaned_tokens))

        return "\n".join(normalised_lines)
    
    def detect_blocks(self, text):
        """
        Deterministic block detection.
        Turns the cleaned text into structural blocks:
        - heading
        - bullet_group
        - paragraph
        """

        lines = text.split("\n")
        blocks = []
        buffer = []
        current_type = None

        def flush_buffer():
            nonlocal buffer, current_type
            if buffer:
                blocks.append({
                    "type": current_type,
                    "content": "\n".join(buffer).strip()
                })
                buffer = []
                current_type = None

        for line in lines:
            stripped = line.strip()

            # Blank line → end current block
            if stripped == "":
                flush_buffer()
                continue

            # Heading block
            if stripped.startswith("#"):
                flush_buffer()
                current_type = "heading"
                buffer.append(stripped)
                flush_buffer()
                continue

            # Bullet group block
            if stripped.startswith("- "):
                if current_type != "bullet_group":
                    flush_buffer()
                    current_type = "bullet_group"
                buffer.append(stripped)
                continue

            # Paragraph block
            if current_type != "paragraph":
                flush_buffer()
                current_type = "paragraph"
            buffer.append(stripped)

        # Flush final block
        flush_buffer()

        return blocks

    def chunk_blocks(self, blocks):
        """
        Deterministic semantic chunking.
        Groups blocks under their nearest heading.
        """

        chunks = []
        current_chunk = {
            "heading": None,
            "blocks": []
        }

        for block in blocks:
            if block["type"] == "heading":
                # Start a new chunk
                if current_chunk["blocks"]:
                    chunks.append(current_chunk)

                current_chunk = {
                    "heading": block["content"],
                    "blocks": []
                }
            else:
                # Add block to current chunk
                current_chunk["blocks"].append(block)

        # Add final chunk
        if current_chunk["blocks"] or current_chunk["heading"]:
            chunks.append(current_chunk)

        return chunks

    def detect_intents(self, chunks):
        """
        Deterministic intent detection for MVP.
        Assigns a simple intent label to each chunk.
        """

        for chunk in chunks:
            heading = chunk["heading"] or ""
            text = "\n".join(b["content"] for b in chunk["blocks"]).strip()

            # Default intent
            intent = "other"

            # If chunk has a heading, use it
            if heading:
                intent = "heading"

            # If chunk contains bullet groups
            if any(b["type"] == "bullet_group" for b in chunk["blocks"]):
                intent = "list"

            # Instruction patterns
            if text.lower().startswith(("how to", "steps", "do this", "follow")):
                intent = "instruction"

            # Definition patterns
            if text.lower().startswith(("is defined as", "refers to", "means")):
                intent = "definition"

            # Explanation patterns
            if text.endswith(".") and len(text.split()) > 8:
                intent = "explanation"

            chunk["intent"] = intent

        return chunks

    def score_clarity(self, chunks):
        """
        Deterministic clarity scoring for MVP.
        Produces a 0–100 clarity score per chunk.
        """

        JARGON = {"utilize", "leverage", "synergy", "paradigm", "framework"}

        for chunk in chunks:
            text = "\n".join(b["content"] for b in chunk["blocks"]).strip()
            words = text.split()
            word_count = len(words)

            # Base score
            score = 100

            # Penalty: long sentences
            if word_count > 20:
                score -= min(30, (word_count - 20))

            # Penalty: jargon
            jargon_hits = sum(1 for w in words if w.lower() in JARGON)
            score -= jargon_hits * 5

            # Bonus: bullet lists are clearer
            if any(b["type"] == "bullet_group" for b in chunk["blocks"]):
                score += 10

            # Bonus: heading present
            if chunk["heading"]:
                score += 5

            # Clamp score
            score = max(0, min(100, score))


    def assemble_output(self, chunks):
        """
        Final output assembly for MVP.
        Produces a clean, stable structure for downstream systems.
        """

        output = {
            "chunks": []
        }

        for chunk in chunks:
            assembled = {
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
            output["chunks"].append(assembled)

        return output

    def assemble_output(self, chunks):
        """
        Final output assembly for MVP.
        Produces a clean, stable structure for downstream systems.
        """

        output = {
            "chunks": []
        }

        for chunk in chunks:
            assembled = {
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
            output["chunks"].append(assembled)

        return output
