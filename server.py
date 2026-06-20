"""
Clarity Engine Server — Hybrid Version
FastAPI server exposing the /run endpoint for the Clarity Engine.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from clarity_engine import ClarityEngine


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
# Engine Instance
# -----------------------------

engine = ClarityEngine()


# -----------------------------
# Routes
# -----------------------------

@app.post("/run", response_model=RunResponse)
async def run_clarity(request: RunRequest):
    """
    Run the Clarity Engine on the provided text.
    """
    result = engine.process(request.text)

    return RunResponse(
        text=result.get("text", ""),
        sections=result.get("sections", []),
        trace=result.get("trace", {}),
        quality=result.get("quality", {}),
        diagnostics=result.get("diagnostics", {}),
    )


@app.options("/run")
async def options_run():
    """
    Handle CORS preflight requests.
    """
    return {"status": "ok"}


# -----------------------------
# Root Endpoint
# -----------------------------

@app.get("/")
async def root():
    return {"status": "Clarity Engine Server Running"}
