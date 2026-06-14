from fastapi import FastAPI
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles
import json
import os

app = FastAPI()

# --- Serve UI folder ---
app.mount("/", StaticFiles(directory="ui", html=True), name="ui")


# --- GENERATE ENDPOINT (real engine connection) ---
@app.post("/generate")
def generate(payload: dict):
    text = payload.get("text", "")

    # --- IMPORT YOUR ENGINE ---
    from simple_engine import SimpleEngine
    engine = SimpleEngine()

    # --- RUN THE ENGINE ---
    result = engine.run(text)

    # --- RETURN ENGINE OUTPUT ---
    return {
        "output": result.get("final_text", ""),
        "sections": result.get("sections", []),
        "trace": result.get("trace", []),
        "quality": result.get("quality", {})
    }


# --- ANALYTICS ENDPOINT ---
@app.post("/analytics")
def analytics(event: dict):
    with open("analytics.log", "a") as f:
        f.write(json.dumps(event) + "\n")
    return {"ok": True}


# --- ANALYTICS LOG VIEWER (for dashboard) ---
@app.get("/analytics-log")
def analytics_log():
    if not os.path.exists("analytics.log"):
        return Response("", media_type="text/plain")

    with open("analytics.log") as f:
        return Response(f.read(), media_type="text/plain")
