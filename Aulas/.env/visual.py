import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
doc1 = nlp("This is a sentence.")
doc2 = nlp("This is another sentence.")
displacy.serve([doc1, doc2], style="dep")