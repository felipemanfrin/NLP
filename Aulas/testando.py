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
# par = 10
# def teste(valor):
#     resultado = valor * 2
#     return resultado
#
# print(teste(par))
# import spacy
# nlp = spacy.load('en_core_web_sm')
# doc = nlp(u'how many year this people has; and how many they spend in cloths.')
# # for token in doc:
# #     print(token, end=' - ')
# #     print(token.i)
# #     if token.text == 'year':
# #         print(True)
# for token in doc[:-1]:
#     if token.text == ';':
#         print(doc[token.i+1])
#
# def numbers_fuc(max_x):
#     lst = []
#     for number in range(max_x+ 1):
#         lst.append(number)
#     return lst

# def numbers_yield(max_x):
#     for n in range(max_x+ 1):
#         yield n
#
# my_generator = numbers_yield(5)
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))

# years_generator = (year for year in range(1, 5001))
# for year in years_generator:
#     print(year)
# def year_generator(start= 1, end= 5000):
#     for year in range(start, end+1):
#         yield year
#
#
# for year in year_generator(1900, 1910):
#     print(year)

# c = [1,2,3,4,5,6,7,8]
# for token in c:
#     print(token, end=' ')

# import spacy
# from spacy import displacy
#
# nlp = spacy.load('en_core_web_sm')
# with open('../UPDATED_NLP_COURSE/TextFiles/peterrabbit.txt') as f:
#     doc = nlp(f.read())
# POS_count = doc.count_by(spacy.attrs.POS)

# for k, v in sorted(POS_count.items()):
#     print(f'{k} {doc.vocab[k].text} {v}')

# square = list()
# for i in range(1,101):
#     square.append(i**2)
# print(square)

# square2 = [i**2 for i in range(1,101) if i<10]
# print(square2)
#
# movies = ['senhor dos aneis', 'senhor das armar', 'starwars', 'SAW']
# # gmovies = []
# # for title in movies:
# #     if title.startswith('s'):
# #         gmovies.append(title)
# # print(gmovies)
# gmovies = [title for title in movies if title.startswith('s')]
# print(gmovies)

movies = [('cidadao kane', 1941), ('cidade de deus', 2000), ('Bela dormecida', 2005), ('pinoquio', 1991), ('tartaruga ninja', 1995)]
gmovies = [title for (title, ano) in movies if ano < 2000]
print(gmovies)