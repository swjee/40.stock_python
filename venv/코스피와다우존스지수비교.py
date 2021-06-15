
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

kospi   = pdr.get_data_yahoo('^KS11',start='2000-01-04')
dow     = pdr.get_data_yahoo('^DJI',start='2000-01-04')



from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


import matplotlib.pyplot as plt

plt.figure(figsize=(9,10))
plt.subplot(211)
plt.title('simple compare')
plt.plot(dow.index,dow.Close , 'r--',label='Dow Jones Industrial')
plt.plot(kospi.index,kospi.Close , 'b',label='KOSPI')
plt.grid(True)
plt.legend(loc='best')


plt.subplot(212)
plt.title('indexation compare')
d = dow.Close / dow.Close.loc['2000-01-04']
k = kospi.Close / kospi.Close.loc['2000-01-04']
plt.plot(d.index,d , 'r--',label='Dow Jones Industrial')
plt.plot(k.index,k , 'b',label='KOSPI')


plt.grid(True)
plt.legend(loc='best')


plt.show()



