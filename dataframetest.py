import pandas as pd

df = pd.DataFrame({'KOSPI':[1200,1300,1250,1500],
                   'KOSDAQ':[540,541,600,530]})

print(df)

df = pd.DataFrame({'KOSPI':[1200,1300,1250,1500],
                   'KOSDAQ':[540,541,600,530]},
                  index=[2014,2015,2016,2017])

print(df)

df.describe()

df.info()


"--------------------"

print(df.index)

for i in df.index:
    print( i , df['KOSPI'][i], df['KOSDAQ'][i])


print('-----------------')

for row in df.itertuples(name='KRX'):
    print(row)

for row in df.itertuples(name='KRX2'):
    print(row[0],row[1],row[2])


print('---- iterrows. ---- ')
for idx,row in df.iterrows():
    print(idx,row[0],row[1])


print('---- iterrows. 2 ---- ')
for idx,row in df.iterrows():
    print(idx)
    print(row.index)
    print(row.values)
    print('----')
    print(idx , row[0] , row[1])



