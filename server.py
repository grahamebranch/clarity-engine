print(">>> LOADING SERVER.PY <<<")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# -------------------------------------------------
# FastAPI app
# -------------------------------------------------
app = FastAPI()

# Allow UI → Backend communication inside Codespaces
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
    # Placeholder logic — your real engine goes here
    improved = text.capitalize()
    sections = [{"title": "Main Idea", "content": improved}]
    trace = ["Engine started", "Engine finished"]
    quality = {"score": 0.8}

    return improved, sections, trace, quality

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
