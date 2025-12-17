def generate_explanation(features: dict, score: int) -> list:
    """
    Generate human-readable explanations for the grammar score.

    Args:
        features (dict): Extracted grammar features
        score (int): Predicted grammar score

    Returns:
        list: Explanation strings
    """
    explanations = []

    # Sentence structure
    if features.get("num_sentences", 0) > 1:
        explanations.append("Sentence structure is mostly consistent.")
    else:
        explanations.append("Limited sentence structure detected.")

    # Sentence length
    avg_len = features.get("avg_sentence_length", 0)
    if avg_len >= 8:
        explanations.append("Sentence length suggests adequate grammatical complexity.")
    else:
        explanations.append("Short sentence patterns may limit grammatical complexity.")

    # Verb usage
    if features.get("num_verbs", 0) >= features.get("num_sentences", 1):
        explanations.append("Verb usage aligns with sentence structure.")
    else:
        explanations.append("Verb usage may be inconsistent across sentences.")

    # Verb tense consistency
    if features.get("verb_tense_variety", 0) <= 2:
        explanations.append("Verb tense usage is relatively consistent.")
    else:
        explanations.append("Multiple verb tenses detected, indicating possible inconsistencies.")

    # Overall score interpretation (neutral)
    if score >= 75:
        explanations.append("Overall grammatical quality is strong.")
    elif score >= 50:
        explanations.append("Overall grammatical quality is moderate.")
    else:
        explanations.append("Overall grammatical quality may need improvement.")

    return explanations
