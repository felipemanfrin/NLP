import spacy
nlp = spacy.load('en_core_web_sm')


with open('../UPDATED_NLP_COURSE/TextFiles/peterrabbit.txt') as f:
    doc = nlp(f.read())
# for token in doc:
#     print(f'{token.pos:{3}}. {token.pos_:{5}} :  ')
POS_counts = doc.count_by(spacy.attrs.POS)
for k, v in sorted(POS_counts.items()):
    print(f'{k} {doc.vocab[k].text} {v}')
print(POS_counts)
print(doc.vocab)
print(len(doc))
