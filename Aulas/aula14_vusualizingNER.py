import spacy
nlp = spacy.load('en_core_web_sm')
from spacy import displacy

doc = nlp(u'Over the last quarter Apple sold nearly 20 thousand iPods for a profit of $6 million'
          u' By contrastSony only sold 8 thousand Walkman music players')

# for sent in doc.sents:
#     displacy.serve(nlp(sent.text), style='ent')
colors = {'ORG': 'linear-gradient(90deg, orange, red)'}#tem o linear e o radiant
options = {'ents': ['ORG', 'PRODUCT'], 'colors': colors}
for sent in doc.sents:
    displacy.serve(doc, style='ent', options=options)
print(spacy.explain("LANGUAGE"))

