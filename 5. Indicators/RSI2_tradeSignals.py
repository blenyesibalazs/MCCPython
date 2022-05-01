from numpy import NaN
import pandas as pd
import pandas_ta as ta

window_length = 14

df = pd.read_csv('wilder-rsi-data.csv', header=0).set_index(['period'])
df.ta.rsi(close='price', length=14, append=True, signal_indicators=True, xa=60, xb=40)


#xa=60, xb=40
print(df)

