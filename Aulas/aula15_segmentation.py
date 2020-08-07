import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp(u'This is the firt sentence. This is the second sentence. this is the last sentence')
# for sent in doc.sents:
#     print(sent)
# print(list(doc.sents)[0])
# print(type(list(doc.sents)[0]))
doc1 = nlp(u'"Management is doing the right things; leadership is doing the right things." -Peter Drucker')
# print(doc1.text)
# for sent in doc1.sents:
#     print(sent)
#     print('\n')
#ADD A SEGMENTATION RULE
def set_custom_boundaries(doc):
    for token in doc:
        print(token, end=' - ')
        print(token.i)#o .i é para a index position
set_custom_boundaries(doc1)
print(doc[:-1])# voce imprime toda a sent menos a ultima palavra
doc1 = nlp(u'"Management is doing the right things; leadership is doing the right things." -Peter Drucker')
def set_custom_bomdaries(doc):
    for token in doc[:-1]:
        if token.text == ';':
            doc[token.i+1].is_sent_start = True
    return doc
nlp.add_pipe(set_custom_bomdaries, before='parser')#Não entendi para que serve mas acho que ele faz a def ser aplicada toda vez antes de algum txt da vida
print(nlp.pipe_names)
doc4 = nlp(u'"Management is doing the right things; leadership is doing the right things." -Peter Drucker')
for sent in doc4.sents:
    print(sent)
doc5 = nlp(u'This is the first sentense; This is the second sentence; This is the third and last sentence')
for sent in doc5.sents:
    print(sent)

#CHANGING THE SEGMENTATION RULES

# mystring = u'This is a sentence. This is another. \n\nThis is a \nthird sentence'
# # print(mystring)
# doc = nlp(mystring)
# for sent in doc.sents:
#     print(sent)
#
# from spacy.pipeline import SentenceSegmenter
#
# def split_newlines(doc):
#     start = 0
#     seen_newline = False
#
#     for word in doc:
#         if seen_newline:
#             yield doc[start:word.i]
#             start = word.i
#             seen_newline = False
#         elif word.text.startswith('\n'):
#             seen_newline = True
#     yield doc[start:]
# sbd = SentenceSegmenter(nlp.vocab, strategy=split_newlines)
# nlp.add_pipe(sbd)
# doc = nlp(mystring)
# for sentence in doc.sents:
#     print(sentence)