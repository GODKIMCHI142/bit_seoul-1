from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

#1. 정제된 데이터 세팅
x = np.array([1,2,3,4,5])
y = np.array([1,2,3,4,5])

#2. 모델 구성
model = Sequential()
model.add(Dense(1, input_dim=1))
model.add(Dense(3))
model.add(Dense(5))
model.add(Dense(3))
model.add(Dense(1))

#3. 데이터 모델 훈련
model.compile(loss='mse', optimizer='adam', metrics=['acc'])
model.fit(x, y, epochs=100, batch_size=1)

loss, acc = model.evaluate(x, y, batch_size=1)

print('acc:',acc)
print('loss: ',loss)