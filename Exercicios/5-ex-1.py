import spacy
from scipy import spatial
nlp = spacy.load('en_core_web_lg')
# doc = nlp(u'queen king and prince')
# for doc1 in doc:
#     for doc2 in doc:
#         print(doc1.text, doc2.text, doc1.similarity(doc2))
# cosine_similarity = lambda x, y: 1 - spatial.distance.cosine(x, y)
# king = nlp.vocab['king'].vector
# man = nlp.vocab['man'].vector
# woman = nlp.vocab['woman'].vector
#
# new_vector = king - man + woman
# computed_similarities = []
# for word in nlp.vocab:
#     if word.has_vector:
#         if word.is_lower:
#             if word.is_alpha:
#                 similarity = cosine_similarity(new_vector, word.vector)
#                 computed_similarities.append((word, similarity))
# computed_similarities = sorted(computed_similarities, key=lambda item: -item[1])
# print([w[0].text for w in computed_similarities[:10]])

def vector_match(a, b, c):
    semelhança_cosseno = lambda x, y: 1 - spatial.distance.cosine(x, y)
    a = nlp.vocab[a].vector
    b = nlp.vocab[b].vector
    c = nlp.vocab[c].vector
    novo_vetor = a - b + c
    similaridades = []
    for palavra in nlp.vocab:
        if palavra.has_vector:
            if palavra.is_lower:
                if palavra.is_alpha:
                    simi = semelhança_cosseno(novo_vetor, palavra.vector)
                    similaridades.append((palavra, simi))
    similaridades = sorted(similaridades, key=lambda item: -item[1])
    print([w[0].text for w in similaridades[:10]])


vector_match('king', 'man', 'woman')

