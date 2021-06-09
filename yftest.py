from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

sec = pdr.get_data_yahoo('005930.KS',start='2018-05-04')
msft = pdr.get_data_yahoo('MSFT',start='2018-05-04')

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


import matplotlib.pyplot as plt

plt.plot( sec['Close'] ,'b', label='Samsung Electronics')
plt.plot( msft['Close'] ,'r--', label='Microsoft')

plt.legend(loc='best')

plt.show()

