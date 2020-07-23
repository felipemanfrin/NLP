# POS = part of speach
import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')
# matcher = Matcher(nlp.vocab)
# pattern = [{'LOWER': 'vanessa'}]
# doc = nlp(u"The quick brown fox jumped over the lazy dog's back")
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
# POS_counts = doc.count_by(spacy.attrs.POS)#aque voce consegue contar quantos atributos voce tem
# print(POS_counts, doc.text)
# # for token in doc:
# #     print(f'{token.pos} {token.text}')
# print(doc.vocab[84].text)
# for k,v in sorted(POS_counts.items()):
#     print(f'{k}. {doc.vocab[k].text:{5}} {v}')
#
# TAG_counts = doc.count_by(spacy.attrs.TAG)
# for k, v in sorted(TAG_counts.items()):
#     print(f'{k}. {doc.vocab[k].text:{5}} {v}')

#____________________________________________________________________________

# from spacy import displacy
# doc2 = nlp(u'This is a sentence. This is another sentence, possibly longer than the other.')
# # options = {'distance': 110, 'compact': True, 'color': 'yellow', 'bg': '#09a3d5', 'font': 'Times'}
# # displacy.serve(doc2, style='dep', options=options)
# #aqui nos temos as representações em desenho do que temos no texto e agora vamos ver algumas oçoes que podemos adaptar a imagem
# spans = list(doc2.sents)
# displacy.serve(spans, style='dep', options={'distance': 110})
#__________________________________________________________________________
#NAMED ENTITY RECOGNITION(NER)
doc3 = nlp(u'May i go to the Avengers in New York. And the place that i most want to travel is japan')
def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(f'{ent.text} - {ent.label_} - {str(spacy.explain(ent.label_))}')
            #ent.text + ' - '+ent.label_ + ' - '+str(spacy.explain((ent.label_ )))
    else:
        print('No entities found')
#
# show_ents(doc3)

# from spacy.tokens import Span
# doc = nlp(u'Tesla to build a BR factory for alot of money')
# ORG = doc.vocab.strings[u'ORG']
# print(ORG)
#
# print(doc.ents)

from spacy.tokens import Span
doc = nlp(u'Our company created a brand new vacuum cleaner This new vacuum-cleaner is the best in show'
       u'This new vacuum-cleaner is the best in show')
show_ents(doc)
from spacy.matcher import PhraseMatcher
encontrador = PhraseMatcher(nlp.vocab)
lista_frase = ['vacuum cleaner', 'vacuum-cleaner']
padroes_frase = [nlp(text) for text in lista_frase]
encontrador.add('novoproduto', None, *padroes_frase)
found_matches = encontrador(doc)
print(found_matches)
from spacy.tokens import Span
PROD = doc.vocab.strings[u'PRODUCT']#esse product é a tag da lista de tags que voce atribui para as palavras que quer adicionar
print(found_matches)
new_ents = [Span(doc, match[1], match[2], label=PROD) for match in found_matches]#aquei nos vamos atribuir a a match1 que eh o atributo 2 e o match2 que eh o terceiro atributo , sendo respectivamente onde começa e termina a palvra que queremos adicionar
doc.ents = list(doc.ents) + new_ents
show_ents(doc)
doc_encontra = nlp(u'Originally I paid $29.95 for this card, but now this card is much more expencive. It is now 50 dollars')
test = len([ent for ent in doc_encontra.ents if ent.label_ == 'MONEY'])
print(test)
