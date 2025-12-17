import os
from app.model.grammar_model import GrammarScoringModel

BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.join(BASE_DIR, "grammar_scorer.pkl")


def load_model():
    """
    Load GrammarScoringModel wrapper
    """
    return GrammarScoringModel(MODEL_PATH)
