from fastapi import APIRouter, UploadFile, File
from app.asr.speech_to_text import SpeechToText
from app.features.grammar_features import extract_grammar_features
from app.model.model_loader import GrammarScoringModel
from app.explanation.explanation_generator import generate_explanation
from app.utils.audio_utils import save_audio_file, cleanup_audio_file

router = APIRouter()

# Initialize models once (loaded at startup time conceptually)
asr_model = SpeechToText(model_size="base")
grammar_model = GrammarScoringModel(
    model_path="app/model/grammar_model.pkl"
)


@router.post("/analyze")
async def analyze_audio(file: UploadFile = File(...)):
    """
    Analyze spoken audio and return grammar score with explanation.
    """
    audio_path = None

    try:
        # 1. Save uploaded audio temporarily
        audio_path = save_audio_file(file)

        # 2. Speech-to-text
        transcript = asr_model.transcribe(audio_path)

        # 3. Grammar feature extraction
        features = extract_grammar_features(transcript)

        # 4. Grammar score prediction
        score = grammar_model.predict(features)

        # 5. Explanation generation
        explanation = generate_explanation(features, score)

        return {
            "transcript": transcript,
            "grammar_score": score,
            "explanation": explanation
        }

    finally:
        # 6. Cleanup temporary file
        if audio_path:
            cleanup_audio_file(audio_path)
