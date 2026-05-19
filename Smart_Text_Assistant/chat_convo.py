import json
import re
import os
from preprocessing import clean_text

BASE_DIR = os.path.dirname(__file__)
file_path = os.path.join(BASE_DIR, "chatbot_conversations.json")

def chatgpt_data(max_rows=200000):
    texts = []

    with open(file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):

            if i >= max_rows:
                break

            try:
                item = json.loads(line)
                #print(item)
                
            except:
                continue
            if item.get("role") != "user":
                continue
            msg = item.get("message", "")
            cleaned = clean_text(msg)

            if cleaned:
                texts.append(cleaned)
    
    return " ".join(texts)
    
#chatgpt_data(200000)