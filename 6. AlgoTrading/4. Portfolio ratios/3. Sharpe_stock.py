import pandas as pd
import numpy as np

# Assume daily returns of a portfolio in pandas Series format
risk_free_rate = 0.04
no_trading_days = 252

df_aapl = pd.read_csv('/Users/blenyesibalazs/DevProjects/MCCPython/6. AlgoTrading/Data/AAPLoutput_2003_2023.csv')

portfolio_returns = df_aapl['last'].pct_change()
portfolio_returns.dropna(inplace=True)

df_aapl['daily returns'] = portfolio_returns

df_aapl.drop([0, len(df_aapl)-1], inplace=True)


excess_returns = (df_aapl['daily returns'] - risk_free_rate)

# Calculate annualized average excess return
avg_excess_return = excess_returns.mean() * no_trading_days
print(avg_excess_return)

# Calculate annualized standard deviation of excess returns
std_excess_return = excess_returns.std() * np.sqrt(no_trading_days)

# Calculate the Sharpe Ratio
sharpe_ratio = avg_excess_return / std_excess_return
annualized_sharpe_ratio = np.sqrt(no_trading_days) * sharpe_ratio

# Print the Sharpe Ratio
print("The Sharpe Ratio is:", sharpe_ratio)
print("The Annualized Sharpe Ratio is:", annualized_sharpe_ratio)
