"""
Clarity Engine Server — Unified Version
FastAPI server exposing:
- /run_engine  → ClarityEngine
- /lesson      → LessonEngine (LessonRouter)
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any

from clarity_engine import ClarityEngine
from lesson.lesson_router import LessonRouter


# -----------------------------
# Request / Response Models
# -----------------------------

class RunRequest(BaseModel):
    text: str


class RunResponse(BaseModel):
    text: str
    sections: list
    trace: dict
    quality: dict
    diagnostics: dict


class LessonRequest(BaseModel):
    topic: str
    level: str
    domain: str = "conversation"
    edition: str = "trainer"
    packs: List[str] = []


class LessonResponse(BaseModel):
    metadata: Dict[str, Any]
    sections: List[Dict[str, Any]]
    annexes: List[Dict[str, Any]]


# -----------------------------
# FastAPI App Setup
# -----------------------------

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# Engine Instances
# -----------------------------

clarity_engine = ClarityEngine()
lesson_router = LessonRouter()


# -----------------------------
# Clarity Engine Route
# -----------------------------

@app.post("/run_engine", response_model=RunResponse)
async def run_clarity(request: RunRequest):
    """
    Run the Clarity Engine on the provided text.
    """
    result = clarity_engine.process(request.text)

    return RunResponse(
        text=result.get("text", ""),
        sections=result.get("sections", []),
        trace=result.get("trace", {}),
        quality=result.get("quality", {}),
        diagnostics=result.get("diagnostics", {}),
    )


@app.options("/run_engine")
async def options_run():
    return {"status": "ok"}


# -----------------------------
# Lesson Engine Route
# -----------------------------

@app.post("/lesson", response_model=LessonResponse)
async def generate_lesson(request: LessonRequest):
    """
    Generate a structured lesson using the Lesson Engine.
    """
    lesson = lesson_router.generate(
        topic=request.topic,
        level=request.level,
        domain=request.domain,
        edition=request.edition,
        packs=request.packs,
    )

    return LessonResponse(
        metadata=lesson["metadata"],
        sections=lesson["sections"],
        annexes=lesson["annexes"],
    )


@app.options("/lesson")
async def options_lesson():
    return {"status": "ok"}


# -----------------------------
# Root Endpoint
# -----------------------------

@app.get("/")
async def root():
    return {"status": "Clarity Engine Server Running"}
