from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

print(">>> USING UPDATED SERVER.PY WITH WILDCARD CORS <<<")


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_origin_regex=".*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ClarityRequest(BaseModel):
    text: str

def run_clarity_engine(text: str):
    improved = text.capitalize()
    sections = [{"title": "Main Idea", "content": improved}]
    trace = ["Engine started", "Engine finished"]
    quality = {"score": 0.8}
    return improved, sections, trace, quality

@app.post("/clarity")
def clarity_endpoint(payload: ClarityRequest):
    improved, sections, trace, quality = run_clarity_engine(payload.text)
    return {
        "improved_text": improved,
        "sections": sections,
        "trace": trace,
        "quality": quality,
    }
