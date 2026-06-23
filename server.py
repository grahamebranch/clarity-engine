from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rameon_engine import RameonEngine
from rameon_core.engine.clarity_scorer import score_text
from rameon_core.engine.section_extractor import extract_sections

app = FastAPI(title="Clarity Engine API", version="1.2")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = RameonEngine()


class GenerateRequest(BaseModel):
    text: str


class Section(BaseModel):
    title: str
    content: str


class GenerateResponse(BaseModel):
    output: str
    clarity_score: int
    sections: list[Section]


@app.post("/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest):
    output = engine.run(req.text)
    clarity = score_text(output)
    sections_raw = extract_sections(output)
    sections = [Section(title=s["title"], content=s["content"]) for s in sections_raw]
    return GenerateResponse(output=output, clarity_score=clarity, sections=sections)
