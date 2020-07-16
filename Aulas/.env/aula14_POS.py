# POS = part of speach
import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')
# matcher = Matcher(nlp.vocab)
# pattern = [{'LOWER': 'vanessa'}]
doc = nlp(u"The quick brown fox jumped over the lazy dog's back")
# # print(doc.text)
# # print(doc[4].text, doc[4].pos_, doc[4].tag_, spacy.explain(doc[4].tag_))
# # # To view the coarse POS tag use token.pos_
# # # To view the fine-grained tag use token.tag_
# # # To view the description of either type of tag use spacy.explain(tag)
# # for token in doc:
# #     print(f'{token.text:{10}} {token.pos_:{8}} {token.tag_:{6}} {spacy.explain(token.tag_)}')
# doc = nlp(u'The vanessa is the best person i have aready meet!')
# matcher.add('ProcurandoVanessa', None, pattern)
# found_nessa = matcher(doc)
#para contar quantas POS temos em um texto
POS_counts = doc.count_by(spacy.attrs.POS)
print(POS_counts, doc.text)
# for token in doc:
#     print(f'{token.pos} {token.text}')
print(doc.vocab[84].text)
for k,v in sorted(POS_counts.items()):
    print(f'{k}. {doc.vocab[k].text:{5}} {v}')

TAG_counts = doc.count_by(spacy.attrs.TAG)
for k, v in sorted(TAG_counts.items()):
    print(f'{k}. {doc.vocab[k].text:{5}} {v}')

