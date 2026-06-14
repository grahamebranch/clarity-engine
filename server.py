print(">>> USING UPDATED SERVER.PY WITH REAL CLARITY ENGINE <<<")

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# -------------------------------------------------
# Import the REAL Clarity Engine
# -------------------------------------------------
from rameon_core.engine.simple_engine import SimpleEngine


# -------------------------------------------------
# FastAPI app
# -------------------------------------------------
app = FastAPI()

# -------------------------------------------------
# CORS (Codespaces‑safe)
# -------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_origin_regex=".*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------------------------------
# Request model
# -------------------------------------------------
class ClarityRequest(BaseModel):
    text: str


# -------------------------------------------------
# Real Clarity Engine wrapper
# -------------------------------------------------
def run_clarity_engine(text: str):
    engine = SimpleEngine()
    engine.load()  # loads config (even if empty)
    return engine.pipeline.run(text)


# -------------------------------------------------
# Explicit OPTIONS route (Fixes Codespaces CORS)
# -------------------------------------------------
@app.options("/clarity")
async def options_clarity():
    return Response(
        status_code=200,
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "*",
        }
    )


# -------------------------------------------------
# POST /clarity
# -------------------------------------------------
@app.post("/clarity")
def clarity_endpoint(payload: ClarityRequest):
    improved, sections, trace, quality = run_clarity_engine(payload.text)
    return {
        "improved_text": improved,
        "sections": sections,
        "trace": trace,
        "quality": quality,
    }
