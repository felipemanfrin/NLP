import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')
with open('../UPDATED_NLP_COURSE/TextFiles/peterrabbit.txt') as f:
    doc = nlp(f.read())
for ent in doc.ents[:2]:
    print(f'{ent.text} - {ent.label_} - {spacy.explain(ent.label_)}')