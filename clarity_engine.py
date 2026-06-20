"""
clarity_engine.py — Hybrid-ready Clarity Engine (placeholder LLM, sections + improved text)

Current scope:
- clean input text
- produce simple sections
- generate improved text via placeholder LLM
- prepare structure for later trace/quality/diagnostics
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
    text: str
    sections: List[Section]
    trace: Dict[str, Any]
    quality: Dict[str, Any]
    diagnostics: Dict[str, Any]


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

    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.split("\n")]

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
# ClarityEngine class
# ---------------------------------------------------------

class ClarityEngine:
    """
    Top-level engine used by server.py
    """

    def process(self, text: str) -> Dict[str, Any]:
        """
        Main entrypoint.

        - clean the input text
        - create simple sections
        - generate improved text via placeholder LLM
        - (placeholder) trace/quality/diagnostics
        """
        cleaned = clean_text(text)
        sections = make_sections(cleaned)

        # NEW: generate improved text using placeholder LLM
        improved_text = call_llm(cleaned)

        result = EngineResult(
            text=improved_text,
            sections=sections,
            trace={},          # to be filled later
            quality={},        # to be filled later
            diagnostics={},    # to be filled later
        )

        return asdict(result)
