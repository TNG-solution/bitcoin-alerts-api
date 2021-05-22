# %%
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import pandas_datareader as web
import datetime as dt

from itertools import chain
from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler 
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.models import Sequential

crypto_currency = "BTC"
against_currency = "USD"

start = dt.datetime(2016,1,1)
end = dt.datetime.now()
end = end.today() - dt.timedelta(days=1)

data = web.DataReader(f"{crypto_currency}-{against_currency}", "yahoo", start, end)

# Prepare Data
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1,1))

# %%
prediction_days = 90
future_day = 0

x_train, y_train = [], []

#x : 60 -> 1964
for x in range(prediction_days, len(scaled_data) - future_day):
    x_train.append(scaled_data[x-prediction_days: x, 0])
    y_train.append(scaled_data[x + future_day,0])

x_train, y_train = np.array(x_train), np.array(y_train)

x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

#Create a Neural Network
#1.19.5

model = Sequential()

model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1))

model.compile(
    optimizer="adam", loss="mean_squared_error"
)

model.fit(x_train, y_train, epochs=50, batch_size=32)

# %%
#Testing the model

test_start = dt.datetime(2020, 1, 1)
test_end = dt.datetime.now()
test_end = test_end.today() - dt.timedelta(days=1)

test_data = web.DataReader(f"{crypto_currency}-{against_currency}", "yahoo", test_start, test_end)
actual_prices = test_data["Close"].values

total_dataset = pd.concat((data["Close"], test_data["Close"]), axis=0)

# 2467 - 503 1964 - 60 1904 
# (1964 + 503) - 503 - 60 = 1906
model_inputs = total_dataset[len(data) - prediction_days:].values

model_inputs = model_inputs.reshape(-1,1)
model_inputs = scaler.fit_transform(model_inputs)

x_test = []

for x in range(prediction_days, len(model_inputs)):
    x_test.append(model_inputs[x-prediction_days: x, 0])

x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

prediction_prices = model.predict(x_test)
prediction_prices = scaler.inverse_transform(prediction_prices)

#%%
print(len(x_test))
print(len(prediction_prices))

from sklearn.metrics import r2_score
y_predict = [x[0] for x in prediction_prices]

score = r2_score(actual_prices, y_predict)

print(score)

date_list = [test_end - dt.timedelta(days=x) for x in range(len(actual_prices))]
date_list = date_list[::-1]

plt.plot(date_list, actual_prices,  'r--', color="red", label="Actual Prices")
plt.plot(date_list, prediction_prices, color="green", label="Predicted Prices")
plt.title(f"{crypto_currency} price prediction")
plt.xlabel("Time")
plt.ylabel("Price")
plt.legend(loc="upper left")

# Predict Next Day
# 1904 + 1 1905 - 60 1845 : 1905
print( len(model_inputs) + 1 - prediction_days)
print(len(model_inputs) + 1)
real_data = [model_inputs[len(model_inputs) + 1 - prediction_days:len(model_inputs) + 1, 0]]
real_data = np.array(real_data)
real_data = np.reshape(real_data, (real_data.shape[0], real_data.shape[1], 1))


prediction = model.predict(real_data)
prediction = scaler.inverse_transform(prediction)
print(prediction)
plt.scatter([date_list[len(date_list) - 1] + dt.timedelta(days=1)], prediction)

plt.show()
# %%
