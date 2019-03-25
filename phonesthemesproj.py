import spacy
from spacy.vocab import Vocab


nlpsm = spacy.load('en_core_web_sm')
print("hey 2")
nlplg = spacy.load('en_core_web_lg')
print("hi")
vocab = Vocab(nlplg)

print("hello")
