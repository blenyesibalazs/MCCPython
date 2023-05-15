import pandas as pd

df_aapl = pd.read_csv('/Users/blenyesibalazs/DevProjects/MCCPython/6. AlgoTrading/Data/AAPLoutput_2003_2023.csv')

# create a sample time series with daily returns

returns = df_aapl['last'].pct_change()
returns.dropna(inplace=True)

# calculate the cumulative returns
cum_returns = (1 + returns).cumprod()

# calculate the previous peaks
prev_peaks = cum_returns.cummax()

# calculate the drawdowns
drawdowns = (cum_returns - prev_peaks) / prev_peaks

# calculate the maximum drawdown and the index of its occurrence
max_drawdown = drawdowns.min()
max_drawdown_index = drawdowns.idxmin()

# calculate the duration of the maximum drawdown
max_drawdown_duration = (drawdowns[max_drawdown_index:] < 0).sum()

# print the results
print('Drawdowns:')
print(drawdowns)
print(f'Maximum drawdown: {max_drawdown:.2%}')
print(f'Maximum drawdown duration: {max_drawdown_duration} days')
