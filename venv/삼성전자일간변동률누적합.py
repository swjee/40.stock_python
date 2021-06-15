
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

sec = pdr.get_data_yahoo('005930.KS',start='2018-05-04')
sec_dpc =  ( sec['Close'] /sec['Close'].shift(1) - 1 ) * 100
sec_dpc.iloc[0] = 0
sec_dpc_cs = sec_dpc.cumsum()

msft = pdr.get_data_yahoo('MSFT',start='2018-05-04')
msft_dpc =  ( msft['Close'] /msft['Close'].shift(1) - 1 ) * 100
msft_dpc.iloc[0] = 0
msft_dpc_cs = msft_dpc.cumsum()




from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


import matplotlib.pyplot as plt



plt.plot( sec_dpc_cs ,'b', label='Samsung Electronics DPC')
plt.plot( msft_dpc_cs ,'r--', label='MSFT  DPC')

plt.ylabel('change %')
plt.legend(loc='best')

plt.show()
