import numpy as np
from sklearn.datasets import load_iris
from keras.utils import to_categorical

iris = load_iris()
# print(type(iris))
# print(iris.DESCR)
x = iris.data
# print(x)#prista a nunpy array de 4 instancias sao 4 medias das flores
y = iris.target
# print(y)
# class 0 --> [1,0,0]
# class 1 --> [0,1,0]
# class 2 --> [0,0,1]

y = to_categorical(y)
# print(y.shape)
# print(y)
from sklearn.model_selection import train_test_split
train_test_split()
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
print(X_train)
