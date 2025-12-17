import os
import uuid
import shutil
from fastapi import UploadFile, HTTPException

# Temporary directory for uploaded audio
TEMP_AUDIO_DIR = "temp_audio"

# Allowed audio extensions
ALLOWED_EXTENSIONS = {".wav", ".m4a", ".mp3", ".flac"}


def ensure_temp_dir():
    """
    Ensure temporary audio directory exists.
    """
    if not os.path.exists(TEMP_AUDIO_DIR):
        os.makedirs(TEMP_AUDIO_DIR)


def validate_audio_file(file: UploadFile):
    """
    Validate uploaded audio file.
    """
    if not file:
        raise HTTPException(status_code=400, detail="No audio file provided")

    ext = os.path.splitext(file.filename)[1].lower()

    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported audio format. Please upload a valid audio file."
        )


def save_audio_file(file: UploadFile) -> str:
    """
    Save uploaded audio file temporarily and return file path.
    """
    ensure_temp_dir()
    validate_audio_file(file)

    unique_filename = f"{uuid.uuid4()}{os.path.splitext(file.filename)[1]}"
    file_path = os.path.join(TEMP_AUDIO_DIR, unique_filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path


def cleanup_audio_file(file_path: str):
    """
    Delete temporary audio file after processing.
    """
    if os.path.exists(file_path):
        os.remove(file_path)
