import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense,Dropout,Conv2D,Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping, TensorBoard

#라벨링 1개 x컬럼3
dataset = load_iris()

x = dataset.data
y = dataset.target

scaler = MinMaxScaler()
scaler.fit(x)
x = scaler.transform(x)

# x= x.reshape(x.shape[0], x.shape[1]  )

print(x.shape) #150,4
print(y.shape) #150, 
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8)
print(x_train.shape,x_test.shape) #120,4 /30,4
print(y_train.shape,y_test.shape) #120,3 /30,3

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

model = Sequential()
model.add(Dense(10, activation='relu', input_shape=(4,)))
model.add(Dense(20, activation='relu'))
model.add(Dense(30, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(3, activation='softmax'))


model.compile(loss='categorical_crossentropy', metrics=['acc'], optimizer='adam')
ealystopping = EarlyStopping(monitor='loss',patience=20, mode='auto')
# to_hist = TensorBoard(log_dir='grahp',write_graph=True, write_images=True, histogram_freq=0)
hist =model.fit(x_train, y_train, epochs=300, batch_size=512, validation_split=0.2, callbacks=[ealystopping])

loss, acc=model.evaluate(x_test, y_test, batch_size=512)

x_predict = x_test[20:30]
y_answer = y_test[20:30]


y_predict = model.predict(x_predict)

y_predict = np.argmax(y_predict, axis=1)
y_answer = np.argmax(y_answer, axis=1)

print("acc",acc)
print("loss",loss)
print("정답",y_answer)
print("예상값",y_predict)


plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])

plt.title('loss & va_loss')
plt.ylabel("loss, val_loss")
plt.xlabel('epoches')
plt.legend(['loss', 'val_loss'])



plt.show()

'''
acc 0.9666666388511658
loss 0.06045258417725563
정답 [1 1 0 2 0 0 1 1 2 2]
예상값 [1 2 0 2 0 0 1 1 2 2]
'''