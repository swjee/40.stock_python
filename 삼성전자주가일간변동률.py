
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

sec = pdr.get_data_yahoo('005930.KS',start='2018-05-04')
sec_dpc =  ( sec['Close'] /sec['Close'].shift(1) - 1 ) * 100
sec_dpc.iloc[0] = 0
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


import matplotlib.pyplot as plt




plt.plot( sec_dpc ,'b', label='Samsung Electronics DPC')

plt.legend(loc='best')

plt.show()
'-- histogram..'


plt.hist( sec_dpc , bins = 20)
plt.grid(True)
plt.show()

