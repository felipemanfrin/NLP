import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')
with open('../UPDATED_NLP_COURSE/TextFiles/peterrabbit.txt') as f:
    doc = nlp(f.read())
list_sents = [nlp(sent.text) for sent in doc.sents]
list_ners = [doc for doc in list_sents if doc.ents]
print(len(list_ners))
displacy.serve(list_sents[0], style='ent')