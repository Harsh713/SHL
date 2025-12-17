import joblib
import numpy as np


class GrammarScoringModel:
    def __init__(self, model_path: str):
        """
        Load the trained grammar scoring model.
        """
        self.model = joblib.load(model_path)

        # IMPORTANT: Feature order must match training
        self.feature_order = [
            "num_sentences",
            "num_tokens",
            "avg_sentence_length",
            "num_verbs",
            "num_subjects",
            "pronoun_ratio",
            "conjunction_ratio",
            "verb_tense_variety",
        ]

    def predict(self, features: dict) -> int:
        """
        Predict grammar score from extracted features.
        """
        feature_vector = np.array(
            [[features.get(f, 0) for f in self.feature_order]]
        )

        score = self.model.predict(feature_vector)[0]
        return int(round(score))
