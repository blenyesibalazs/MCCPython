from numpy import NaN
import pandas as pd
import pandas_ta as ta

window_length = 14

df = pd.read_csv('wilder-rsi-data.csv', header=0).set_index(['period'])
df.ta.rsi(close='price', length=14, append=True)
df.to_csv('wilder-rsi-pandasta-output.csv')

