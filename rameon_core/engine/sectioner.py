"""
Sectioner — removes duplicated headings inside content.
"""

import re

HEADING_PATTERN = re.compile(r"^[A-Z][A-Za-z0-9 ,.'’\-]{1,80}$")

def is_heading(line: str) -> bool:
    return bool(HEADING_PATTERN.match(line.strip()))

def split_into_sections(text: str):
    lines = text.split("\n")
    sections = []
    current_title = None
    current_content = []

    for line in lines:
        stripped = line.strip()

        if is_heading(stripped):
            # If we were in a section, save it
            if current_title is not None:
                sections.append({
                    "title": current_title,
                    "content": "\n".join(current_content).strip()
                })

            # Start new section
            current_title = stripped
            current_content = []
        else:
            # Normal content line
            current_content.append(stripped)

    # Final section
    if current_title is not None:
        sections.append({
            "title": current_title,
            "content": "\n".join(current_content).strip()
        })

    return sections
