import os
import re
from preprocessing import clean_text

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(
    BASE_DIR,
    "wikitext-2-raw",
    "wiki.train.raw"
)

def wiki_text():
    with open(file_path, "r", encoding="utf-8") as f:
         #lines = f.readlines()[:10] 
         #print(lines) 
         #text = " ".join(lines) 
         #print(text)
         #cleaned = clean_text(text)
         #return cleaned
        text=f.read()
        cleaned_text=clean_text(text)
        #print(cleaned_text)
        return cleaned_text
#wiki_text()
    
    
         
   

    
    


