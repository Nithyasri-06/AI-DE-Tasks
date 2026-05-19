import nltk
from nltk.corpus import brown, nps_chat, gutenberg,webtext
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from collections import defaultdict,Counter
from chat_convo import chatgpt_data
from wikitext import  wiki_text
from chat_convo import chatgpt_data
import re


text = (
    wiki_text()+" "+chatgpt_data(200000)
)

tokens=re.findall(r"\w+(?:'\w+)?", text)
#print(tokens)

MODEL = defaultdict(Counter)

for w1, w2, w3 in ngrams(tokens, 3):
    if "EOS" in (w1, w2, w3):
        continue

    MODEL[(w1, w2)][w3]+=1
    
#import pickle

#with open("trigram_model.pkl", "wb") as f:
    #pickle.dump(MODEL, f)

#print("Model exported successfully!")

#print(MODEL)
    
#for key,counter in MODEL.items():
    
    #print(f"{key} -> {dict(counter)}")
    

