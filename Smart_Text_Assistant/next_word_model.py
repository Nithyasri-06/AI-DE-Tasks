import nltk
from nltk.corpus import brown, nps_chat, gutenberg,webtext
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from collections import defaultdict

#nltk.download('punkt')
#nltk.download('brown')
#nltk.download('nps_chat')
#nltk.download('gutenberg')

text = (
    brown.raw() + " " +
    nps_chat.raw() + " " +
    gutenberg.raw('austen-emma.txt')+" "+
    webtext.raw()
)

tokens = word_tokenize(text.lower())

MODEL = defaultdict(list)

for w1, w2, w3 in ngrams(tokens, 3):
    MODEL[(w1, w2)].append(w3)

#print(MODEL)