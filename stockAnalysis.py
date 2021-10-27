#first install pip install yfinance --upgrade --no-cache-dir
# pip install bsedata
# pip install fbprophet

import pandas_datareader.data as pdr
import datetime
import yfinance as yf
import matplotlib.pyplot as plt
from bsedata.bse import BSE
from fbprophet import Prophet

stock_name= 'ITC.NS'

yf.Ticker(stock_name)

start = datetime.datetime(2021,4,1)
end = datetime.datetime(2021,10,18)


# download dataframe
data = pdr.get_data_yahoo(stock_name, start, end)
data.head()
data['Open'].plot(label ='open price' , figsize=(15,7))
data['Close'].plot(label ='close price')
data['High'].plot(label ='high price')
data['Low'].plot(label ='low price')
#data['Volume'].plot(label ='Volume')
plt.legend()
plt.title('stock analysis')
plt.xlabel('date')
plt.ylabel('price')
plt.show()
data.to_csv('data.csv')