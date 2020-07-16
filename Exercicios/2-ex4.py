# import spacy
#
# nlp = spacy.load('en_core_web_sm')
# with open('../UPDATED_NLP_COURSE/TextFiles/owlcreek.txt') as f:
#     doc = nlp(f.read())
# for token in doc[13:35]:
#     print(f'{token.text:{10}} {token.pos_:{10}} {token.dep_}   {token.lemma_:>{8}} ')

import spacy

nlp = spacy.load('en_core_web_sm')
with open('../UPDATED_NLP_COURSE/TextFiles/owlcreek.txt') as f:
    doc = nlp(f.read())
sents = [sent for sent in doc.sents]
print(sents[3].text)
for token in sents[3]:
    print(f'{token.text:{15}} {token.pos_:{5}} {token.dep_:{10}} {token.lemma_:{15}}')