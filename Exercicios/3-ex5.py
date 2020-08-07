import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')
with open('../UPDATED_NLP_COURSE/TextFiles/peterrabbit.txt') as f:
    doc = nlp(f.read())
    displacy.serve(list(doc.sents)[4], style='dep')