import re
def clean_text(text):

    text = text.replace("’", "'")
    text = text.lower()
    
    text = re.sub(r"=+.*?=+", " ", text)
    
    text = re.sub(r"http\S+|www\S+", "", text)
    text = text.replace("@-@", " ")
    text = re.sub(r"[.!?]", " eos ",text)
    #print(text)
    text = re.sub(r"[^a-z0-9\s']", " ", text)
    #print(text)
    text = text.replace("eos", "EOS")
    #print(text)
    text = re.sub(r"\s+", " ", text).strip()
    #print(text)
    return text