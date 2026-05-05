from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from wordfreq import zipf_frequency, top_n_list
from next_word_model import MODEL

STOPWORDS = set(stopwords.words("english"))
LOW_VALUE = {"one", "like", "would", "could", "also"}

RULES = {
    ("am", "feeling"): ["happy", "sad", "tired", "good", "excited"],
    ("going", "to"): ["school", "office", "home", "market", "work"],
    ("i", "am"): ["happy", "ready", "fine", "busy", "tired"],
    ("are", "you"): ["okay", "sure", "there", "coming", "ready"],
    ("do", "you"): ["know", "want", "like", "need", "think"]
}
def is_valid_input(words):
    return all(w.isalpha() for w in words)

def fallback_words(n,context=None):
    words = top_n_list("en", 500)

    filtered = [
        w for w in words
        if w not in STOPWORDS
        and w not in LOW_VALUE
        and w.isalpha()
        and len(w) > 3
    ]

    sorted_words = sorted(
        filtered,
        key=lambda w: zipf_frequency(w, "en"),
        reverse=True
    )
    if context:
        context_words = RULES.get(context, [])
        for w in reversed(context_words):
            if w in sorted_words:
                sorted_words.remove(w)
                sorted_words.insert(0, w)

    return sorted_words[:n]

    

def predict_next_words(input_text, n=10):
    words = word_tokenize(input_text.lower())

    if len(words) < 2:
        return ["Enter at least 2 words"]

    if not is_valid_input(words):
        return ["Invalid input"]

    last_two = (words[-2], words[-1])
    model_output = []
    freq = {}

    if last_two in MODEL and len(MODEL[last_two]) > 0:
        suggestions = MODEL[last_two]

       
        for w in suggestions:
            freq[w] = freq.get(w, 0) + 1

        sorted_model_words = sorted(
            freq,
            key=lambda w: (freq[w], zipf_frequency(w, "en")),
            reverse=True
        )

        model_output = [
            w for w in sorted_model_words
            if w not in STOPWORDS
            and w not in LOW_VALUE
            and w.isalpha()
        ]
    rule_output = RULES.get(last_two, [])
    candidates = set(model_output + rule_output)

    if not candidates:
        candidates = set(fallback_words(n, context=last_two))

    scored = []

    for w in candidates:
        if not w.isalpha():
            continue
        if w in STOPWORDS or w in LOW_VALUE:
            continue

        model_score = freq.get(w, 0)
        zipf_score = zipf_frequency(w, "en")

        score = model_score + zipf_score
        scored.append((w, score))

    scored.sort(key=lambda x: x[1], reverse=True)

    return [w for w, _ in scored[:n]]