#1. data
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split

x = np.array([range(1, 101), range(311, 411), range(100)])
y = np.array((range(101, 201), range(711, 811), range(100)))



print(x)
print(x.shape) # (3,100)

#(100,3)의 형태로 변환을 시켜라 

print(x.T)
# print(x.transpose())
# print(np.transepose(x))
print(x.T.shape)
print(x.transpose())
x = x.T
y= y.T
# y~ 1, y ~2, y3 = w1x1 * w2x2 * w3x3 + b

x_train, x_test, y_train, y_test = train_test_split( x,y, train_size= 0.6, shuffle=True)

# x_train = np.array(list(x)[:60])) 
# x_test = np.array(list(x)[60:100])
# y_train = np.array(list(y)[60:100])
# y_test = np.array(list(y)[60:100])
print(x_train)

model = Sequential()
model.add(Dense(10 ,input_dim =3 ))
model.add(Dense(5))
model.add(Dense(3))

model.compile(loss='mse', metrics=['acc'], optimizer='adam')
model.fit(x_train, y_train, batch_size=1, epochs=100, validation_split=0.2)

loss, acc =model.evaluate(x_test, y_test, batch_size= 1)

y_predict = model.predict(x_test)

#-------------------------------------------------------------------------------------------
def RMSE(y_test, y_predict):
    return np.sqrt(mean_squared_error(y_test, y_predict))

def R2(y_test, y_predict):
    return r2_score(y_test,y_predict)

rmse = RMSE(y_test, y_predict)
r2 = R2(y_test, y_predict)

print("loss: ",loss)
print("RMSE:",rmse)
print("R2:",r2)
