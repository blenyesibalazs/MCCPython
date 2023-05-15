import pandas as pd
import numpy as np

# Import the necessary data for the portfolio and risk-free rate
df_aapl = pd.read_csv('/Users/blenyesibalazs/DevProjects/MCCPython/6. AlgoTrading/Data/AAPLoutput_2003_2023.csv')
df_snp = pd.read_csv('/Users/blenyesibalazs/DevProjects/MCCPython/6. AlgoTrading/Data/SNP500output_2003_2023.csv')

#calculate the daily returns of the portfolio and the market 
aapl_returns = df_aapl['last'].pct_change()
snp500_returns = df_snp['last'].pct_change()

#dropping NaN values
aapl_returns.dropna(inplace=True)
snp500_returns.dropna(inplace=True)

#print(len(aapl_returns))
#print(len(snp500_returns))

min_len = min(len(df_aapl), len(snp500_returns))
aapl_returns = aapl_returns.truncate(after=min_len - 1)
snp500_returns = snp500_returns.truncate(after=min_len - 1)

risk_free_rate = 0.04
excess_returns = aapl_returns - risk_free_rate

# Calculate the portfolio beta using linear regression
beta, alpha = np.polyfit(snp500_returns, aapl_returns, 1)
treynor_ratio = excess_returns.mean() / beta

print("The Treynor ratio is:", treynor_ratio)
