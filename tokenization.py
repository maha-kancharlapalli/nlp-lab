import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

text = """Natural Language Processing (NLP) is a field of AI that helps computers understand human language.
Python makes it easy to work with NLP thanks to libraries like NLTK and TextBlob."""

# Sentence tokenization
sentences = sent_tokenize(text)
print("Sentences:")
for s in sentences:
    print("-", s)

# Word tokenization
words = word_tokenize(text)
print("\nWords:")
print(words)
