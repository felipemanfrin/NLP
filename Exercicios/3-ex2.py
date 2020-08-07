import spacy

nlp = spacy.load('en_core_web_sm')
with open('../UPDATED_NLP_COURSE/TextFiles/peterrabbit.txt') as f:
    doc = nlp(f.read())
# sents = [sent for sent in doc.sents]
# print(sents[4])
# for sent in sents[4]:
#     print(f'{sent.text:{8}} -  {sent.pos_:{5}} - {sent.tag_:{8}} - ')
for token in list(doc.sents)[4]:
    print(f'{token.text:{10}} {token.pos_:{10}} {token.tag_:{10}} {str(spacy.explain(token.tag_))}')
