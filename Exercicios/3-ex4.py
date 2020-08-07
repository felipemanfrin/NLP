import spacy
nlp = spacy.load('en_core_web_sm')

with open('../UPDATED_NLP_COURSE/TextFiles/peterrabbit.txt') as f:
    doc = nlp(f.read())
POS_counts = doc.count_by(spacy.attrs.POS)
print(POS_counts)
# total = noun = 0
# for k, v in sorted(POS_counts.items()):
#     print(f'{k} {doc.vocab[k].text} {v}')
#     total += v
#     if k == 92:
#         noun += v
# print(f'{noun}/{total} = {total/noun}')
print((POS_counts[92]/len(doc))*100, '%')
