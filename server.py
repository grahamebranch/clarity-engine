from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

print(">>> USING UPDATED SERVER.PY WITH WILDCARD CORS <<<")

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
# Dummy clarity engine
# -------------------------------------------------
def run_clarity_engine(text: str):
    improved = text.capitalize()
    sections = [{"title": "Main Idea", "content": improved}]
    trace = ["Engine started", "Engine finished"]
    quality = {"score": 0.8}
    return improved, sections, trace, quality

# -------------------------------------------------
# **EXPLICIT OPTIONS ROUTE (Fixes Codespaces CORS)**
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
