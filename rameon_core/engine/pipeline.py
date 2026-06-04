class Pipeline:
    """
    The core pipeline that processes input through multiple stages:
    parse → validate → transform → output
    """

    def parse(self, input_data):
        import re

        lines = input_data.split("\n")
        parsed = []

        for line in lines:
            stripped = line.strip()

            # Detect Markdown headings (#, ##, ###)
            md_heading = re.match(r'^(#{1,6})\s+(.*)$', stripped)
            if md_heading:
                level = len(md_heading.group(1))
                text = md_heading.group(2).strip()
                parsed.append({"heading": text, "level": level})
                continue

            # Detect simple headings (e.g., "Heading:" or "HEADING")
            if stripped.endswith(":") and stripped[:-1].isalpha():
                parsed.append({"heading": stripped[:-1], "level": 1})
                continue

            # Detect bullet points: "-", "*", "•"
            if stripped.startswith(("-", "*", "•")):
                bullet_text = stripped.lstrip("-*•").strip()
                parsed.append({"bullet": bullet_text})
                continue

            # Sentence splitting for normal lines
            sentences = re.split(r'(?<=[.!?]) +', stripped)
            for s in sentences:
                if s:
                    parsed.append(s)

        return parsed




    def validate(self, parsed_data):
        return parsed_data

    def transform(self, validated_data):
        cleaned = []

        for item in validated_data:
            # Bullet
            if isinstance(item, dict) and "bullet" in item:
                text = item["bullet"].strip()
                text = " ".join(text.split())
                cleaned.append({"bullet": text})
                continue

            # Heading
            if isinstance(item, dict) and "heading" in item:
                text = item["heading"].strip()
                text = " ".join(text.split())
                cleaned.append({"heading": text, "level": item["level"]})
                continue

            # Normal sentence
            text = item.strip()
            text = " ".join(text.split())
            cleaned.append(text)

        return cleaned



    def output(self, transformed_data):
        lines = []

        for item in transformed_data:
            # Bullet
            if isinstance(item, dict) and "bullet" in item:
                lines.append(f"- {item['bullet']}")
                continue

            # Heading
            if isinstance(item, dict) and "heading" in item:
                prefix = "#" * item["level"]
                lines.append(f"{prefix} {item['heading']}")
                continue

            # Normal sentence
            lines.append(item)

        return "\n".join(lines)




    def run(self, input_data):
        parsed = self.parse(input_data)
        validated = self.validate(parsed)
        transformed = self.transform(validated)
        return self.output(transformed)
