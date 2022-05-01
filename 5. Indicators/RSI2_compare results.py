from numpy import NaN
import pandas as pd
import pandas_ta as ta

window_length = 14

df = pd.read_csv('wilder-rsi-data.csv', header=0).set_index(['period'])
df.ta.rsi(close='price', length=14, append=True)
#df.to_csv('wilder-rsi-pandasta-output.csv')
print(df)
print('--------------------------------------------------')

Wilder_RSI = [74.36, 74.55, 65.75, 59.68, 61.98, 66.44, 65.75, 67.0, 71.43, 70.5, 72.14, 67.95, 60.78, 55.56, 56.71, 49.49, 48.19, 52.38, 50.0, 43.5, 45.36, 42.53, 44.14, 44.75]
v = pd.DataFrame(pd.concat([pd.Series(["NaN"] * (window_length)), pd.Series(Wilder_RSI)])).reset_index(level=0).drop(['index'], axis=1) #tarolom az uj sorozatomat es az ures helyeket feltoltom NaN-el
v.index = list(range(1, len(v) + 1))  # ujraindexelek mindent (nem feltetlen kotelezo, de jo gyakorlatnak)
# kulonbsegek
df['diff_rsi'] = ((df['RSI_14'] - v.values).abs())
df['diff_pct'] = ((df['RSI_14'] - v.values) / v.values * 100).abs()
# kerekites
df['diff_rsi'] = df['diff_rsi'].apply(lambda x: round(x, 2))
df['diff_pct'] = df['diff_pct'].apply(lambda x: round(x, 2))

print(df)