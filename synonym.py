import nltk
from nltk.corpus import wordnet

# Download WordNet data (if not already downloaded)
nltk.download('wordnet')

def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return synonyms

word = "smallest"
synonyms = get_synonyms(word)

# if synonyms:
#     print(f"Synonyms of '{word}': {', '.join(synonyms)}")
# else:
#     print(f"No synonyms found for '{word}'.")
