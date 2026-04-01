from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return {"message": "Backend working!"}

@app.post("/analyze")
def analyze(logs: dict):
    return {
        "incident_type": "Test",
        "severity": "Low",
        "report": "Working"
    }
