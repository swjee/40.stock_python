#최대손실 낙폭. Maximum drawdown.
#( 최저점 - 최고점)/최저점

#1980년의 모든종목의 시가총액의 합을 기준지수 100포인트로 집계.
#만약 현재 지수가 2500 이라면 증시가 25배 올랐음을 의미.

# 야후 파이낸스에서 KOSPI지수데이터 로드하여 최대손실낙폭구한다.

# ^KS11
# 252: 1년 개장일의 어림치.
# 종가칼럼에서



from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

kospi = pdr.get_data_yahoo('^KS11',start='2004-05-04')

window = 252

peak = kospi['Adj Close'].rolling(window,min_periods=1).max()
dd = kospi['Adj Close']/peak -1
max_dd = dd.rolling(window,min_periods=1).min()

print(max_dd.min() )

#print( max_dd[max_dd==-0.5453665130144085] )


from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


import matplotlib.pyplot as plt

plt.figure(figsize=(9,7))
plt.subplot( 211)
kospi['Adj Close'].plot( label ='KOSPI',title='KOSPI MDD',grid=True,legend=True)

plt.subplot( 212)
dd.plot(c='blue',label='KOSPI DD',grid=True,legend=True)
max_dd.plot(c='red',label='KOSPI MDD',grid=True,legend=True)

plt.show()


