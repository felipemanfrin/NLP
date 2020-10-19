import numpy as np
from sklearn.datasets import load_iris
from keras.utils import to_categorical
import h5py

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
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
# print(y_test)
from sklearn.preprocessing import MinMaxScaler
print(np.array([5,10,15,20])/20)
scaler_object = MinMaxScaler()
scaler_object.fit(X_train)
scaled_X_train = scaler_object.transform(X_train)
scaled_X_test = scaler_object.transform(X_test)
# print(scaled_X_train)
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
model.add = (Dense(8, input_dim=4, activation='relu'))
model.add = (Dense(8, input_dim=4, activation='relu'))
model.add = (Dense(3, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())
model.fit(scaled_X_train, y_train, epochs=150, verbose=2)