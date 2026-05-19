from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from wordfreq import zipf_frequency, top_n_list
from next_word_model import MODEL
import nltk


def is_valid_input(words):
    return all(w.isalpha() for w in words)


def fallback_words(n):
    words = top_n_list("en", 200)

    filtered = [
        w for w in words
        if w.isalpha()
        and len(w) > 2
    ]
    sorted_words = sorted(
        filtered,
        key=lambda w: zipf_frequency(w, "en"),
        reverse=True
    )

    return sorted_words[:n]


def predict_next_words(input_text, n=10):
    words = word_tokenize(input_text.lower())

    if len(words) <= 2:
        return ["Enter at least 2 words"]

    if not is_valid_input(words):
        return ["Invalid input"]


    last_two = (words[-2], words[-1])

    if last_two in MODEL and len(MODEL[last_two]) > 0:
        
        freq=MODEL[last_two]
        
        sorted_words = sorted(
            freq,
            key=lambda w: (freq[w], zipf_frequency(w, "en")),
            reverse=True
        )

        filtered = [
            w for w in sorted_words
            #if w not in LOW_VALUE
            if w.isalpha()
        ]

        if filtered:
            return filtered[:n]

    return fallback_words(n)