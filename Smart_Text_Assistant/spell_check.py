from textblob import Word
from wordfreq import zipf_frequency

def spelling_correct(word):
    word = word.lower()

    candidates = Word(word).spellcheck()

    results = []

    for w, confidence in candidates:
        score = confidence + zipf_frequency(w, "en")
        results.append((w, score))

    # sort best first
    results.sort(key=lambda x: x[1], reverse=True)

    return [w for w, _ in results[:3]]   # top 3 suggestions