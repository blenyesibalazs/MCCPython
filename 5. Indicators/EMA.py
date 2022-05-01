import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import pyEX as p

ticker = 'TSLA'
timeframe = '1y'

df = p.chartDF(ticker, timeframe)
df = df[['close']]
df.reset_index(level=0, inplace=True)
df.columns=['ds','y']

exp1 = df.y.ewm(span=20, adjust=False).mean()
exp2 = df.y.ewm(span=50, adjust=False).mean()

plt.plot(df.ds, df.y, label='TSLA')
plt.plot(df.ds, exp1, label='TSLA 20 Day EMA', color='orange')
plt.plot(df.ds, exp2, label='TSLA 50 Day EMA', color='magenta')
plt.legend(loc='upper left')
plt.show()