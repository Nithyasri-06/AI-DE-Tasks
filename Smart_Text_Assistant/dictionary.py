from nltk.corpus import wordnet

def get_meaning(word):
    synsets=wordnet.synsets(word)
    if not synsets:
        return "No meaning found"
    meaning=synsets[0].definition()
    if '-' in meaning:
        meaning = meaning.split('-')[0].strip()
    return meaning
        
def get_synonym(word):
    synsets=wordnet.synsets(word)
    synonyms=set()
    for synset in synsets:
        for lemma in synset.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)
    