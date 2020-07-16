# import spacy
#
# nlp = spacy.load('en_core_web_sm')
# with open('../UPDATED_NLP_COURSE/TextFiles/owlcreek.txt') as f:
#     doc = nlp(f.read())
#     total = 0
#     for sentence in doc.sents:
#         total += 1
# print(total)
import spacy

nlp = spacy.load('en_core_web_sm')
with open('../UPDATED_NLP_COURSE/TextFiles/owlcreek.txt') as f:
    doc = nlp(f.read())
sents = [sent for sent in doc.sents]
print(len(sents))