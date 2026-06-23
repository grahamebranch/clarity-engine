from typing import List, Dict


def extract_sections(text: str) -> List[Dict[str, str]]:
    """
    Simple deterministic section extractor.
    Heuristic:
    - Split on double newlines.
    - First non-empty line in a block is the 'title'.
    - Remaining lines are the 'content'.
    - If no content exists, treat the whole block as content.
    """

    sections: List[Dict[str, str]] = []

    if not text or not text.strip():
        return sections

    # Split into blocks separated by blank lines
    blocks = text.split("\n\n")

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        lines = block.splitlines()
        title = lines[0].strip()
        content = "\n".join(lines[1:]).strip()

        # If there's no content, treat the block as content
        if not content:
            content = title
            title = "Section"

        sections.append({
            "title": title,
            "content": content
        })

    return sections
