
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Lemon Engine API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://zenexa-lemon-engine.static.hf.space"
    ],
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

class ImageRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"message": "Lemon Engine API is running 🍋"}

@app.post("/generate")
def generate_image(request: ImageRequest):
    if not request.prompt.strip():
        return {"error": "Please enter a prompt"}

    return {
        "status": "received",
        "prompt": request.prompt,
        "message": "Image generation will be connected next."
    }
