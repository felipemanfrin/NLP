import spacy

nlp = spacy.load('en_core_web_sm')
with open('../UPDATED_NLP_COURSE/TextFiles/peterrabbit.txt') as f:
    doc = nlp(f.read())
# total = 0
# for sent in doc.sents:
#     total += 1
#     print(sent)
# print(total)
print(len(list(doc.sents)))