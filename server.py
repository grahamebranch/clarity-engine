"""
Clarity Engine Server — Final Production Version
FastAPI server exposing the /run endpoint for the Clarity Engine.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from clarity_engine.simple_engine import SimpleEngine


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
    allow_origins=["*"],          # UI on 5500, Postman, browser, etc.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# Engine Instance
# -----------------------------

engine = SimpleEngine()


# -----------------------------
# Routes
# -----------------------------

@app.post("/run", response_model=RunResponse)
async def run_clarity(request: RunRequest):
    """
    Run the Clarity Engine on the provided text.
    """
    result = engine.run(request.text)

    return RunResponse(
        text=result.get("text", ""),
        sections=result.get("sections", []),
        trace=result.get("trace", {}),
        quality=result.get("quality", {}),
        diagnostics=result.get("diagnostics", {})
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
