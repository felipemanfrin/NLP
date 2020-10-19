from keras.models import Sequential
from keras.layers import Dense, Activation

model = Sequential([
    Dense(32, input_shape=(10), activation='relu'),
    Dense(2, activation='softmax')
])