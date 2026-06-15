print(">>> USING UPDATED SERVER.PY WITH REAL CLARITY ENGINE <<<")

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json


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
# Real Clarity Engine wrapper (with strict sectioning)
# -------------------------------------------------
from rameon_core.engine.clarity_scorer import score_sections

def run_clarity_engine(text: str):
    engine = SimpleEngine()
    engine.load(text)

    result = engine.pipeline.run(text)
    print("PIPELINE RESULT:", result)

    # -------------------------------------------------
    # 1. Expect dict output from MVP pipeline
    # -------------------------------------------------
    if isinstance(result, dict):
        improved = result.get("improved_text", "")
        sections = result.get("sections", [])
        trace = result.get("trace", [])
        quality = result.get("quality", {"score": 0})
    else:
        # Fallback for unexpected output
        improved = str(result)
        sections = []
        trace = []
        quality = {"score": 0}

    # -------------------------------------------------
    # 2. Apply clarity scoring
    # -------------------------------------------------
    quality = score_sections(sections)

    # -------------------------------------------------
    # 3. Return API contract
    # -------------------------------------------------
    return improved, sections, trace, quality


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

    body = json.dumps({
        "improved_text": improved,
        "sections": sections,
        "trace": trace,
        "quality": quality,
    })

    return Response(
        content=body,
        media_type="application/json",
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST, OPTIONS",
            "Access-Control-Allow-Headers": "*",
        }
    )
