import spacy
from collections import Counter

# Load spaCy English model once
nlp = spacy.load("en_core_web_sm")


def extract_grammar_features(transcript: str) -> dict:
    """
    Extract grammar-related features from a transcript.

    Args:
        transcript (str): Speech-to-text output

    Returns:
        dict: Grammar feature dictionary
    """
    doc = nlp(transcript)

    sentences = list(doc.sents)
    num_sentences = len(sentences)

    tokens = [token for token in doc if not token.is_punct and not token.is_space]
    num_tokens = len(tokens)

    # Average sentence length
    avg_sentence_length = (
        num_tokens / num_sentences if num_sentences > 0 else 0
    )

    # POS tag distribution
    pos_counts = Counter([token.pos_ for token in tokens])

    # Verb tense indicators
    verb_tenses = Counter(
        [token.morph.get("Tense")[0] for token in tokens if token.pos_ == "VERB" and token.morph.get("Tense")]
    )

    # Subject–verb agreement proxy
    subject_count = sum(1 for token in tokens if token.dep_ == "nsubj")
    verb_count = sum(1 for token in tokens if token.pos_ == "VERB")

    # Simple grammar quality proxies
    pronoun_count = sum(1 for token in tokens if token.pos_ == "PRON")
    conjunction_count = sum(1 for token in tokens if token.pos_ == "CCONJ")

    features = {
        "num_sentences": num_sentences,
        "num_tokens": num_tokens,
        "avg_sentence_length": avg_sentence_length,
        "num_verbs": verb_count,
        "num_subjects": subject_count,
        "pronoun_ratio": pronoun_count / num_tokens if num_tokens > 0 else 0,
        "conjunction_ratio": conjunction_count / num_tokens if num_tokens > 0 else 0,
        "verb_tense_variety": len(verb_tenses),
    }

    return features
