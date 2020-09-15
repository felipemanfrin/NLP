import spacy
nlp = spacy.load('en_core_web_lg')
# print(nlp(u'lion').vector)
# print(nlp(u'The quick brown fox jumped').vector.shape)
# tokens = nlp(u'lion cat pet')
# for token1 in tokens:
#     for token2 in tokens:
#         print(token1.text, token2.text, token1.similarity(token2))
# print('---------------------------')
# print(len(nlp.vocab.vectors))
# print(nlp.vocab.vectors.shape)

# tokens = nlp(u'dog cat nargle')
# for token in tokens:
#     print(token.text, token.has_vector, token.vector_norm, token.is_oov)#out of vocabulary (oov)
# from scipy import spatial
#
# cosine_similarity = lambda vec1, vec2: 1 - spatial.distance.cosine(vec1, vec2)
# king = nlp.vocab['king'].vector
# man = nlp.vocab['man'].vector
# woman = nlp.vocab['woman'].vector
#
# new_vector = king-man+woman
# computed_similarities = []
# # PARA TODAS AS PALAVRAS NO VOCAB
# for word in nlp.vocab:
#     if word.has_vector:
#         if word.is_lower:
#             if word.is_alpha:
#                 similarity = cosine_similarity(new_vector, word.vector)
#                 computed_similarities.append((word, similarity))
# computed_similarities = sorted(computed_similarities, key=lambda item: -item[1])#vai mostrar em ordem decrescente a similaridade
# print([t[0].text for t in computed_similarities[:10]])

#-------------------------------------------------------------------------------
#VADER ( VALENCE AWARE DICTIONARY FOR SENTIMENT REASONING) ta no pacote NLTK

import nltk
# nltk.download('vader_lexicon')

# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# sid = SentimentIntensityAnalyzer()
# a = "This is a good movie"
# b = 'This was the best, most awesome movie EVER MADE!!@!'
# print(sid.polarity_scores(a))
# print(sid.polarity_scores(b))
# import pandas as pd
# df = pd.read_csv('textos/amazonreviews.tsv', sep='\t')
# print(df.head())
# print(df['label'].value_counts())
# df.dropna(inplace=True)
# blanks = []
# for i, lb, rv in df.itertuples():
#     if type == str:
#         if rv.isspace():
#             blanks.append()
# #df.drop(blanks, inplace=True) se precisar tirar alguma coisa faltando
# print(df.iloc[0]['review'])
# print(sid.polarity_scores(df.iloc[0]['review']))
# df['scores'] = df['review'].apply(lambda review: sid.polarity_scores(review))
# df['compound'] = df['scores'].apply(lambda d:d['compound'])
# print(df.head())
# df['comp_score'] = df['compound'].apply(lambda score: 'pos' if score >=0 else 'neg')
# print(df.head())
# from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
# print(accuracy_score(df['label'], df['comp_score']))
# print(classification_report(df['label'], df['comp_score']))
# print(confusion_matrix(df['label'], df['comp_score']))
import numpy as np
import pandas as pd
df = pd.read_csv('textos/moviereviews.tsv', sep='\t')
print(df.head())
df.dropna(inplace=True)
blanks = []
for i, lb, rv in df.itertuples():
    if type(rv) == str:
        if rv.isspace():
            blanks.append(i)
print(blanks)
df.drop(blanks, inplace=True)
print(df['label'].value_counts())
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
df['scores'] = df['review'].apply(lambda review: sid.polarity_scores(review))
df['compound'] = df['scores'].apply(lambda d:d['compound'])
print(df.head())
df['comp_score'] = df['compound'].apply(lambda score: 'pos' if score >= 0 else 'neg')
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
print(accuracy_score(df['label'], df['comp_score']))
print(classification_report(df['label'], df['comp_score']))
print(confusion_matrix(df['label'], df['comp_score']))


