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


