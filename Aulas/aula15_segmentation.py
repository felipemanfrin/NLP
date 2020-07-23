import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp(u'This is the firt sentence. This is the second sentence. this is the last sentence')
# for sent in doc.sents:
#     print(sent)
# print(list(doc.sents)[0])
# print(type(list(doc.sents)[0]))
# doc1 = nlp(u'"Management is doing the right things; leadership is doing the right things." -Peter Drucker')
# print(doc1.text)
# for sent in doc1.sents:
#     print(sent)
#     print('\n')
#ADD A SEGMENTATION RULE
# def set_custom_boundaries(doc):
#     for token in doc:
#         print(token, end=' - ')
#         print(token.i)#o .i é para a index position
# set_custom_boundaries(doc1)
# print(doc[:-1])# voce imprime toda a sent menos a ultima palavra
doc1 = nlp(u'"Management is doing the right things; leadership is doing the right things." -Peter Drucker')
def set_custom_bomdaries(doc):
    for token in doc[:-1]:
        if token.text == ';':
            doc[token.i+1].is_sent_start = True
        return doc
nlp.add_pipe(set_custom_bomdaries, before='parser')
print(nlp.pipe_names)
print(set_custom_bomdaries(doc1))
# doc4 = nlp(u'"Management is doing the right things; leadership is doing the right things." -Peter Drucker')
for sent in set_custom_bomdaries(doc1).sents:
    print(sent)
