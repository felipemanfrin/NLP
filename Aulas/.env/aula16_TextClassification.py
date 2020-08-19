''''Recall é a abilidade de encontrar todos os casos relevantes na dataset / Que podemos definir como numero de true positives/true posites + false negatives'''
# import numpy as np
# from sklearn.model_selection import train_test_split
# x, y = np.arange(10).reshape((5, 2)), range(5)
# print(x)
# list(y)
# print(y)

import numpy as np
# import pandas as pd
#
# df = pd.read_csv('../smsspamcollection.tsv', sep='\t')
# print(df.head())
# print('---------------------------------------')
# print(df.isnull())
# print('---------------------------------------')
# print(df.isnull().sum())
# print('---------------------------------------')
# print(len(df))
# print('---------------------------------------')
# print(df['label'].unique())
# print('---------------------------------------')
# print(df['label'].value_counts())
# print('---------------------------------------')
#
# from sklearn.model_selection import train_test_split
# # X feature data
# X = df[['length', 'punct']]
# # y is our label
# y = df['label']
# X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=42)
# print(X_train.shape)
# print('---------------------------------------')
# print(X_test.shape)
# from sklearn.linear_model import LogisticRegression
# lr_model = LogisticRegression(solver='lbfgs')
# print(lr_model.fit(X_train, y_train))
# from sklearn import metrics
# prediction = lr_model.predict(X_test)
# print(prediction)#aqui temos as prediçoes
# print(y_test)#aqui temos os true resultados que já sabemos
# #y_test
# print(metrics.confusion_matrix(y_test, prediction))
# df = pd.DataFrame(metrics.confusion_matrix(y_test, prediction), index=['ham', 'spam'], columns=['ham', 'spam'])
# print(df)
# print('---------------------------------------')
# print(metrics.classification_report(y_test, prediction))
#____________________________________________________________________________________
# vocab = {}
# i = 1
# with open('../textos/1.txt') as f:
#     x = f.read().lower().split()
#
# one = ['1.txt']+[0]*len(vocab)
#
# for word in x:
#     if word in vocab:
#         continue
#     else:
#         vocab[word] = i
#         i += 1
# print(vocab)
# with open('../textos/2.txt') as f:
#     x = f.read().lower().split()
#
# for word in x:
#     if word in vocab:
#         continue
#     else:
#         vocab[word] = i
#         i += 1
#
# print(vocab)
# one = ['1.txt']+[0]*len(vocab)
# with open('../textos/1.txt') as f:
#     x = f.read().lower().split()
# for word in x:
#     one[vocab[word]] += 1
# print(one)
# two = ['2.txt']+[0]*len(vocab)
# with open('../textos/2.txt') as f:
#     x = f.read().lower().split()
# for word in x:
#     two[vocab[word]] += 1
# print(two)
#____________________________________________________________________________________
#agora vamos contar a quantidade de palavras que temos repetidas em todos nosssos textos
import numpy as np
import pandas as pd

df = pd.read_csv('../textos/smsspamcollection.tsv', sep='\t')
# print(df.head())
# print(df.isnull().sum())#aqui voce encontrara se temos algum valor faltando, se der tudo zero porque nao falta nada mas esse comando não confere se tem alguma string vazia '  '
# print('-------------------------------------------------------------------------')
# print(df['label'].value_counts())

from sklearn.model_selection import train_test_split
X = df['message']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
# print(X)# aqui o texto sai sem estar formatado bonitinho
# #então temos que FIT o vectorizes na data (construindo o vocab, cu contar o numero de palavras
# count_vect.fit(X_train)#primeiro temos que encaixar (FIT)
# X_train_counts = count_vect.transform(X_train)#depois temos que tranformar
# #vamos transformar a mensagem original na mensagem de texto no vetor finalizando a etapa de 'FIT TRANSFORM'

X_train_counts = count_vect.fit_transform(X_train)# já aqui podemos fazer o de cima em uma linha somente
# print(X_train_counts)
print(X_train_counts.shape)
from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print(X_train_tfidf.shape)
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer
X_train_tfidf = vectorizer.fit_transform(X_train)
from sklearn.svm import LinearSVC# para treinar o classifier
