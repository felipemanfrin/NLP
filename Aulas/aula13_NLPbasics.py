# Import spaCy and load the language library
import spacy
nlp = spacy.load('en_core_web_sm')

# # Create a Doc object
# doc = nlp(u'Tesla is looking at buying U.S. startup for $6 million')
#
# # Print each token separately
# for token in doc:
#     print(token.text, token.pos_, token.dep_)
# print(nlp.pipeline)
# print(doc[0].pos_)

# doc3 = nlp(u'Although commmonly attributed to John Lennon from his song "Beautiful Boy", \
# the phrase "Life is what happens to us while we are making other plans" was written by \
# cartoonist Allen Saunders and published in Reader\'s Digest in 1957, when Lennon was 17.')
# life_quote = doc3[16:30]
# print(life_quote)
# print(type(life_quote))#ele fala que é span porque ele pegou um pedaço do um doc maior
#
# doc4 =  nlp(u'This is the first sentence. This is another sentence. This is the laste sentense')
# print(doc4[6].is_sent_start)#ve se é o começo de uma sentença
# for sentence in doc4.sents:
#     print(sentence)

# TOKENIZATION

# mystring = '"We \'re moving to L.A.!"'# nesse caso nos temos a contra barra para poder usar a aspas simples dentro ,mesmo tento todas aspas no local
# print(mystring)
# doc = nlp(mystring)
# for token in doc:
#     print(token.text)
# print(len(doc))
# print(len(doc.vocab))#quer dizer que ele tem 483 diferente tokens para essa situação
# doc8 = nlp(u'Apple to build a Hong Kong factory for $6 million')
# # for token in doc8:
# #     print(token.text,end=' | ')
# for entity in doc8.ents:#ele sabe quando são entidades com esse ents
#     print(entity)
#     print(entity.label_)
#     print(str(spacy.explain((entity.label_))))#legal aqui que consegue explicar certinho quais o que as label significam
#     print('\n')#
# doc9 = nlp(u'Autonomous car shift insurance liability toward manufactures')
# for chunk in doc9.noun_chunks:
#     print(chunk)

#Tokenization Visualized

# from spacy import displacy# esse aqui vai tornar mais visual a interface
# doc = nlp(u'Apple is going to build a U.K. factory for $6 million.')
# # displacy.serve(doc, style="dep",options={'distance':50})#com diplacy.server voce consegue no seu localhost visualizar os graficos com setinhas sobre a estrutura
# displacy.serve(doc,style='ent')#demonstra com corzinha quais são as entidades

#Stemming #é um metodo de catalogar palavras relacionadas

import nltk
# from nltk.stem.porter import PorterStemmer
# p_stemmer = PorterStemmer()
# words = ['run', 'runner', 'ran', 'runs', 'easily', 'fairly']
# for word in words:
#     print(word + '---->' + p_stemmer.stem(word))
#
# from nltk.stem.snowball import SnowballStemmer
# s_stemmer = SnowballStemmer(language='english')
# for word in words:
#     print(word + '---->' + s_stemmer.stem(word))

#Lemmatization aqui nos não olhamos somente para a palavra em si e sim consideramos o vocabulario para aplicar a analize morfologica da palavra

# doc1 = nlp(u'I am a runner running in a race because I love to run since i ran to much')
# def show_lemmas(text):
#     for token in doc1:
#         print(f'{token.text:{8}} \t {token.pos_} \t {token.lemma} \t {token.lemma_}')
#
# doc2 = nlp(u'I saw ten mice today!')
# print(show_lemmas(doc2))

#STOP WORDS

# print(nlp.Defaults.stop_words)
# print(len(nlp.Defaults.stop_words))
# print(nlp.vocab['is'].is_stop)#diz se a palavra esta na lista de condição de parada
# nlp.Defaults.stop_words.add('PONTOFINAL')#nessa aqui estamos adicionando uma palavra a lista de stop
# nlp.vocab['PONTOFINAL'].is_stop = True
# print(len(nlp.Defaults.stop_words))
# print(nlp.vocab['PONTOFINAL'].is_stop)
# nlp.Defaults.stop_words.remove('beyond')#vai remover essa palvra da lista
# nlp.vocab['beyond'].is_stop
# print(nlp.vocab['beyond'].is_stop)

#VOCABULARY AND MATCHING

# from spacy.matcher import Matcher
# matcher = Matcher(nlp.vocab)
# # pattern1 = [{'LOWER': 'solarpower'}]#uma lista de dicionarios quero achar SolarPower
# # pattern2 = [{'LOWER': 'solar'}, {'IS_PUNCT': True}, {'LOWER': 'power'}]#vai achar solar-power
# # pattern3 = [{'LOWER': 'solar'}, {'LOWER': 'power'}]#vai achar solar power
# # matcher.add('SolarPower', None, pattern1, pattern2, pattern3)
# # doc = nlp(u'The solar power industry continues to grow a solarpower increases. Solar-power is the cleanest of the energies')
# # found_matches = matcher(doc)
# # print(found_matches)#o numero grande é o ID o segundo é onde começa e o 3 onde termina a palavra encontrada
# # for match_id, start, end in found_matches:
# #     string_id = nlp.vocab.strings[match_id]
# #     span = doc[start:end]
# #     print(match_id, string_id, start, end, span.text)
# # matcher.remove('SolarPower')#aqui remove a palavra escolhida
# pattern11 = [{'LOWER': 'solarpower'}]
# pattern22 = [{'LOWER': 'solar'}, {'IS_PUNCT': True, 'OP': '*'}, {'LOWER': 'power'}]
# matcher.add('SolarPower', None, pattern11, pattern22)
# doc2 = nlp(u'Solar--power is solarpower yay!')
# found_matches = matcher(doc2)
# print(found_matches)
from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)
with open('../UPDATED_NLP_COURSE/TextFiles/reaganomics.txt') as f:
    doc3 = nlp(f.read())
phrase_list = ['voodoo economics', 'supply-side economics', 'trickle-down economics']
phrase_patterns = [nlp(text) for text in phrase_list]
matcher.add('EconMatcher', None, *phrase_patterns)#passa como argumento essas phrase patterns individualmente e passar nesse matcher add
found_matches = matcher(doc3)
print(found_matches)
for match_id, start, end, in found_matches:
    string_id = nlp.vocab[match_id]
    span = doc3[start: end]#se quiser mostrar algumas palavras a mais só fazer [start+5: end+5]
    print(match_id, string_id, start, end, span.text)