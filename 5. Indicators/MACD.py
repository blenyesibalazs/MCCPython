import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import pyEX as p

ticker = 'AMD'
timeframe = '6m'

df = p.chartDF(ticker, timeframe)
df = df[['close']]
df.reset_index(level=0, inplace=True)
df.columns=['ds','y']

exp1 = df.y.ewm(span=12, adjust=False).mean()
exp2 = df.y.ewm(span=26, adjust=False).mean()
exp3 = df.y.ewm(span=9, adjust=False).mean()

macd = exp1-exp2
exp3 = macd.ewm(span=9, adjust=False).mean()

plt.plot(df.ds, macd, label='AMD MACD', color = '#7067CF')

plt.legend(loc='upper left')
plt.show()