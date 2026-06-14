# rameon_core/engine/sectioner.py

import re
from typing import List, Dict

HEADING_RE = re.compile(r'^\s{0,3}(#{1,6}\s+.+|[A-Z][A-Z0-9 ]{5,}$)')
BULLET_RE = re.compile(r'^\s*([-*+]|[0-9]+[.)])\s+')

def section_text(text: str) -> List[Dict]:
    """
    Strict sectioning:
    - Headings become their own sections
    - Blank lines break sections
    - Bullet/numbered lists become list sections
    """
    lines = text.splitlines()
    sections: List[Dict] = []
    buffer: list[str] = []
    current_type: str | None = None

    def flush():
        nonlocal buffer, current_type, sections
        if not buffer:
            return
        content = "\n".join(buffer).strip()
        if not content:
            buffer = []
            current_type = None
            return
        sections.append(
            {
                "id": len(sections) + 1,
                "type": current_type or "paragraph",
                "text": content,
            }
        )
        buffer = []
        current_type = None

    for line in lines:
        # Blank line → end of current section
        if not line.strip():
            flush()
            continue

        # Headings → their own section
        if HEADING_RE.match(line):
            flush()
            current_type = "heading"
            buffer.append(line.strip())
            flush()
            continue

        # Bullet / numbered list items
        if BULLET_RE.match(line):
            if current_type not in ("list", None):
                flush()
            current_type = "list"
            buffer.append(line.rstrip())
            continue

        # Continuation of a list (indented or wrapped lines)
        if current_type == "list":
            buffer.append(line.rstrip())
            continue

        # Normal paragraph text
        if current_type not in ("paragraph", None):
            flush()
        current_type = "paragraph"
        buffer.append(line.rstrip())

    flush()
    return sections
