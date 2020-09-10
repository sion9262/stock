
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import mpl_finance as mpf

df = pd.read_csv("sdf.csv", index_col="Date", parse_dates=True)

index = df.index.astype('str')
df['5day'] = df['Close'].rolling(window=5).mean()
df['20day'] = df['Close'].rolling(window=20).mean()
df['60day'] = df['Close'].rolling(window=60).mean()
df['120day'] = df['Close'].rolling(window=120).mean()
df['200day'] = df['Close'].rolling(window=200).mean()

fig, ax = plt.subplots(figsize=(12, 8))

# x축 날짜 조정
def x_date(x, pos):
    try:
        return index[int(x-0.5)][:7]

    except:
        return ''
ax.xaxis.set_major_locator(ticker.MaxNLocator(10))
ax.xaxis.set_major_formatter(ticker.FuncFormatter(x_date))

ax.plot(index, df['5day'], label='5day')
ax.plot(index, df['20day'], label='5day')
ax.plot(index, df['60day'], label='5day')
ax.plot(index, df['120day'], label='5day')
ax.plot(index, df['200day'], label='5day')
mpf.candlestick2_ohlc(ax, df['Open'], df['High'], df['Low'], df['Close'], width=0.5, colorup='r', colordown='b')
plt.show()

'''df['Close'].plot(label='Close')
df['Open'].plot(label='Open')

df_move = pd.DataFrame()
df_move['five'] = df['Close'].resample('D').mean()
print(df_move)
'''
'''plt.legend(loc='upper right')
plt.show()'''