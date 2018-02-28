import pandas as pd
import pandas_datareader.data as web # Package and modules for importing data; this code may change depending on pandas version
import datetime
import matplotlib.pyplot as plt
import numpy
import talib


# We will look at stock prices over the past year, starting at January 1, 2016
start = datetime.datetime(1999, 1, 1)
end = datetime.datetime(2018,1,1)

# Let's get Apple stock data; Apple's ticker symbol is AAPL
# First argument is the series we want, second is the source ("yahoo" for Yahoo! Finance), third is the start date, fourth is the end date

SPY = web.DataReader("SPY", "google", start, end)
SPY.name = 'SPY'
XLF = web.DataReader("XLF", "google", start, end)
XLF.name = 'XLF'
XLE = web.DataReader("XLE", "google", start, end)
XLE.name = 'XLE'
XLK = web.DataReader("XLK", "google", start, end)
XLK.name = 'XLK'
XLU = web.DataReader("XLU", "google", start, end)
XLU.name = 'XLU'
XLP = web.DataReader("XLP", "google", start, end)
XLP.name = 'XLP'
XLI = web.DataReader("XLI", "google", start, end)
XLI.name = 'XLI'
XLY = web.DataReader("XLY", "google", start, end)
XLY.name = 'XLY'


myStocks = [SPY, XLF, XLE, XLK, XLU, XLP, XLI, XLY]



#print(SPY.head())
#SPY["Close"].plot(grid=True)
#plt.show()
#SPY = SPY.Close.values
#real = talib.RSI(SPY.Close.values)
#print(len(real))

#path = '~\Desktop\BigData\Project\Data'
for s in myStocks:
    s.Volume = s.Volume.astype(float)
    s['RSI'] = talib.RSI(s.Close.values)
    s['AROONOSC'] = talib.AROONOSC(s.High.values, s.Low.values)
    s['MFI'] = talib.MFI(s.High.values,s.Low.values,s.Close.values,s.Volume.values)
    s['MOM'] = talib.MOM(s.Close.values)
    s['MA50'] = talib.MA(s.Close.values,timeperiod=50)
    s['MA200'] = talib.MA(s.Close.values,timeperiod=200)
    s['OBV'] = talib.OBV(s.Close.values,s.Volume.values)
    s.to_csv(s.name+'.csv')


#SPY['RSI'] = talib.RSI(SPY.Close.values)
#SPY['AROONOSC'] = talib.AROONOSC(SPY.High.values,SPY.Low.values)


#print(SPY.head())
#print(type(SPY.Close[1]))