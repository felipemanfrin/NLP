# import spacy
#
# nlp = spacy.load("en_core_web_sm")
# tokens = nlp("dog cat banana afskfsd")
#
# for token in tokens:
#     print(token.text, token.has_vector, token.vector_norm, token.is_oov)

# import spacy
# nlp = spacy.load('en_core_web_sm')
# doc = nlp(u'This is the first sentence. This is the second sentence. This is the last sentence.')
# for sent in doc.sents:
#     print(sent)
# print(doc[1])
# print(list(doc.sents)[0])
par = 10
def teste(valor):
    resultado = valor * 2
    return resultado

print(teste(par))
