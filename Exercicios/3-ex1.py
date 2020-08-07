import spacy
nlp = spacy.load('en_core_web_sm')
from spacy import displacy

with open('../UPDATED_NLP_COURSE/TextFiles/peterrabbit.txt') as f:
    doc = nlp(f.read())
print(doc)
