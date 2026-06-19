"""
Clarity Engine Server — Final Production Version
FastAPI server exposing the /run endpoint for the Clarity Engine.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from rameon_engine import RameonEngine


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
    allow_origins=["*"],          # UI on 3000, Postman, browser, etc.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# Engine Instance
# -----------------------------

engine = RameonEngine()


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
        text=result,
        sections=[],       # EL3–EL10 currently return text only
        trace={},
        quality={},
        diagnostics={}
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
