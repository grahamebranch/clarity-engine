"""
el6.py — Hybrid-ready Clarity Engine (placeholder LLM, sections only)

Current scope:
- clean input text
- produce simple sections
- prepare structure for later trace/quality/diagnostics
- use a local LLM placeholder (no external dependency yet)
"""

from dataclasses import dataclass, asdict
from typing import List, Dict, Any


# ---------------------------------------------------------
# Data models
# ---------------------------------------------------------

@dataclass
class Section:
    id: int
    title: str
    content: str


@dataclass
class EngineResult:
    input_text: str
    cleaned_text: str
    sections: List[Section]
    # placeholders for future steps
    trace: str = ""
    quality: Dict[str, Any] = None
    diagnostics: Dict[str, Any] = None


# ---------------------------------------------------------
# LLM placeholder (to be replaced later)
# ---------------------------------------------------------

def call_llm(prompt: str) -> str:
    """
    Placeholder LLM call.

    Later this will call a real model (OpenAI, local, etc.).
    For now, it just echoes a short, safe response so the
    pipeline and UI can be tested without any external service.
    """
    # Keep it short and deterministic
    snippet = prompt.strip().replace("\n", " ")
    if len(snippet) > 200:
        snippet = snippet[:200] + "..."
    return f"[LLM placeholder response based on prompt snippet: '{snippet}']"


# ---------------------------------------------------------
# Text cleaning
# ---------------------------------------------------------

def clean_text(text: str) -> str:
    """
    Basic cleaning:
    - strip leading/trailing whitespace
    - normalise line endings
    - collapse excessive blank lines
    """
    if not text:
        return ""

    # Normalise line endings
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # Split into lines and trim
    lines = [line.rstrip() for line in text.split("\n")]

    # Collapse multiple blank lines
    cleaned_lines: List[str] = []
    blank_streak = 0
    for line in lines:
        if line.strip() == "":
            blank_streak += 1
            if blank_streak <= 1:
                cleaned_lines.append("")
        else:
            blank_streak = 0
            cleaned_lines.append(line)

    cleaned = "\n".join(cleaned_lines).strip()
    return cleaned


# ---------------------------------------------------------
# Simple sectioning logic
# ---------------------------------------------------------

def _split_into_blocks(text: str) -> List[str]:
    """
    Split text into blocks using blank lines as separators.
    """
    if not text:
        return []

    blocks: List[str] = []
    current: List[str] = []

    for line in text.split("\n"):
        if line.strip() == "":
            if current:
                blocks.append("\n".join(current).strip())
                current = []
        else:
            current.append(line)

    if current:
        blocks.append("\n".join(current).strip())

    return blocks


def _make_title_from_block(block: str, index: int) -> str:
    """
    Create a simple title from the first sentence or first line.
    """
    if not block:
        return f"Section {index}"

    first_line = block.split("\n", 1)[0].strip()
    # Try to cut at a sentence boundary
    for sep in [".", "!", "?"]:
        if sep in first_line:
            first_line = first_line.split(sep, 1)[0].strip()
            break

    if len(first_line) > 80:
        first_line = first_line[:77] + "..."

    if not first_line:
        return f"Section {index}"

    return first_line


def make_sections(cleaned_text: str) -> List[Section]:
    """
    Turn cleaned text into a list of sections.

    For now:
    - split on blank lines
    - derive a simple title from each block
    - assign incremental IDs
    """
    blocks = _split_into_blocks(cleaned_text)
    sections: List[Section] = []

    if not blocks:
        return sections

    for i, block in enumerate(blocks, start=1):
        title = _make_title_from_block(block, i)
        sections.append(Section(id=i, title=title, content=block))

    return sections


# ---------------------------------------------------------
# Public engine entrypoint
# ---------------------------------------------------------

def run_engine(input_text: str) -> Dict[str, Any]:
    """
    Main entrypoint for the engine.

    Current behaviour:
    - clean the input text
    - create simple sections
    - return a structured dict ready for the backend/UI

    Later we will:
    - add LLM-powered trace
    - add quality scoring
    - add diagnostics
    """
    cleaned = clean_text(input_text)
    sections = make_sections(cleaned)

    result = EngineResult(
        input_text=input_text,
        cleaned_text=cleaned,
        sections=sections,
        trace="",          # to be filled in a later step
        quality=None,      # to be filled in a later step
        diagnostics=None,  # to be filled in a later step
    )

    # Convert dataclasses to plain dicts for JSON friendliness
    result_dict = asdict(result)
    # sections are already converted by asdict()
    return result_dict


# ---------------------------------------------------------
# Simple manual test (optional)
# ---------------------------------------------------------

if __name__ == "__main__":
    sample = """
This is a quick test of the Clarity Engine.

It should split this text into sections,
using blank lines as separators.

Here is another section, with a bit more content.
We want to see how the titles are generated.
"""
    out = run_engine(sample)
    from pprint import pprint
    pprint(out)
