import whisper
import torch


class SpeechToText:
    def __init__(self, model_size: str = "base"):
        """
        Initialize the ASR model once.
        model_size: tiny | base | small | medium
        """
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print("Whisper running on:", self.device)

        self.model = whisper.load_model(model_size, device=self.device)

    def transcribe(self, audio_path: str) -> str:
        """
        Convert speech audio to text.

        Args:
            audio_path (str): Path to the audio file

        Returns:
            str: Transcribed text
        """
        result = self.model.transcribe(audio_path)
        transcript = result.get("text", "").strip()
        return transcript
