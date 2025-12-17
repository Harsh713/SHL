from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import uuid

from app.asr.speech_to_text import SpeechToText
from app.features.grammar_features import extract_grammar_features
from app.model.model_loader import load_model

app = FastAPI()

# Allow frontend (React) to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load ASR + Grammar model ONCE at startup
asr = SpeechToText(model_size="base")
model = load_model()

UPLOAD_DIR = "temp_audio"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/score")
async def score_audio_api(file: UploadFile = File(...)):
    """
    Accept audio file → transcribe → extract grammar features → predict score
    """
    # Save uploaded file temporarily
    file_ext = file.filename.split(".")[-1]
    temp_name = f"{uuid.uuid4()}.{file_ext}"
    temp_path = os.path.join(UPLOAD_DIR, temp_name)

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # 1. Speech-to-text
        transcript = asr.transcribe(temp_path)

        # 2. Grammar feature extraction
        features = extract_grammar_features(transcript)

        # 3. Grammar score prediction
        score = model.predict(features)

    finally:
        # Cleanup temp file
        if os.path.exists(temp_path):
            os.remove(temp_path)

    return {
        "score": score,
        "transcript": transcript
    }
