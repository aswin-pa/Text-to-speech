import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from tts_engine import text_to_wav
from audio_utils import wav_to_mp3

app = FastAPI(title="Text to Speech API")

# Allow the frontend (opened from a file or another port) to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # restrict this to your domain before deploying publicly
    allow_methods=["*"],
    allow_headers=["*"],
)

class SynthesisRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=3000)
    format: str = Field("mp3", pattern="^(mp3|wav)$")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/synthesize")
def synthesize(req: SynthesisRequest):
    try:
        wav_path = text_to_wav(req.text.strip())
        if req.format == "wav":
            return FileResponse(wav_path, media_type="audio/wav", filename="speech.wav")
        mp3_path = wav_to_mp3(wav_path)
        os.remove(wav_path)
        return FileResponse(mp3_path, media_type="audio/mpeg", filename="speech.mp3")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Synthesis failed: {e}")
