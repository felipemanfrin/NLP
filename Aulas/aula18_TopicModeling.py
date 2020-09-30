#LDA latent dirichlet allocation

# import pandas as pd
#
# npr = pd.read_csv('05-Topic-Modeling/npr.csv')
# # print(npr.head())
# # print(npr['Article'][4000])
# print(len(npr))
#
# from sklearn.feature_extraction.text import CountVectorizer
#
# cv = CountVectorizer(max_df=0.9, min_df=2, stop_words='english')#esse df tu descarta as palavras que aparecem em 0.9(90% dos textos)
# dtm = cv.fit_transform(npr['Article'])
# # print(dtm)
#
# from sklearn.decomposition import LatentDirichletAllocation
# lda = LatentDirichletAllocation(n_components=7, random_state=42)
# lda.fit(dtm)
#
# #GRAB THE VOCABULARY OF WORDS
# # print(len(cv.get_feature_names()))
# # print(type(cv.get_feature_names()))
# # import random
# # random_word_id = random.randint(0, 54777)
# # print(cv.get_feature_names()[random_word_id])
#
# #GRAB THE TOPIC
# # print(len(lda.components_))
# # print(lda.components_.shape)
#
# single_topic = lda.components_[0]
# # print(single_topic.argsort())
# import numpy as np
# arr = np.array([10, 200, 1])
# # print(arr.argsort())
# top_ten = single_topic.argsort()[-10:]
# for index in top_ten:
#     print(cv.get_feature_names()[index])
#
# for i, topic in enumerate(lda.components_):
#     print(f'The top 15 words for topic #{i}')
#     print([cv.get_feature_names()[index] for index in topic.argsort()[-15:]])
#     print('\n')
#
# topic_results = lda.transform(dtm)
# print(topic_results, topic_results.shape, topic_results[0])

#NON NEGATIVE MATRIX FACTORIZATION

import pandas as pd
npr = pd.read_csv('05-Topic-Modeling/npr.csv')
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')
dtm = tfidf.fit_transform(npr['Article'])
# print(dtm)
from sklearn.decomposition import NMF

nmf_model = NMF(n_components=7, random_state=42)
nmf_model.fit(dtm)
print(tfidf.get_feature_names()[2300])
for index, topic in enumerate(nmf_model.components_):
    print(f'The top 15 words for topic #{index}')
    print([tfidf.get_feature_names()[i] for i in topic.argsort()[-15:]])

topic_result = nmf_model.transform(dtm)
print(topic_result[0].argmax())
npr['Topic'] = topic_result.argmax()
print(npr.head())







