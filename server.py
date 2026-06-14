print(">>> LOADING SERVER.PY <<<")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# -------------------------------------------------
# FastAPI app
# -------------------------------------------------
app = FastAPI()

# -------------------------------------------------
# CORS (Codespaces-safe configuration)
# -------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://zany-computing-machine-gx47prv67g97fwpgv-5500.app.github.dev"
    ],
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
# Dummy clarity engine (replace with your real engine)
# -------------------------------------------------
def run_clarity_engine(text: str):
    improved = text.capitalize()
    sections = [{"title": "Main Idea", "content": improved}]
    trace = ["Engine started", "Engine finished"]
    quality = {"score": 0.8}
    return improved, sections, trace, quality

# -------------------------------------------------
# OPTIONS handler (must be ABOVE the POST route)
# -------------------------------------------------
@app.options("/clarity")
def clarity_options():
    return {}

# -------------------------------------------------
# API endpoint
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
