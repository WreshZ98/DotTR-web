import matplotlib.pyplot as pplt
import yfinance as yf
import numpy as np


def run_forecast_view(forecastedPrice, finalDate, ticker):
    tickerData = ticker.history(period="max")

msft = yf.Ticker("MSFT")
dataPandas = msft.history(period="max")

dataNumpy = dataPandas["Close"].to_numpy()
dataNumpy.round(2,dataNumpy)
print(dataNumpy)    
dataNumpy.tofile("data.csv",sep=",")
newData = dataNumpy
for i in range(50):
    newData = np.append(newData,0)

newData = np.append(newData,460)    


pplt.plot(newData)
pplt.show()