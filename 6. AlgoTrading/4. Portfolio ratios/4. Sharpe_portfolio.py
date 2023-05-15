import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Assume daily returns of a portfolio in pandas Series format
risk_free_rate = 0.04
no_trading_days = 252

aapl_df = pd.read_csv('/Users/blenyesibalazs/DevProjects/MCCPython/6. AlgoTrading/Data/AAPLoutput_2003_2023.csv', index_col='date', parse_dates=True)
goog_df = pd.read_csv('/Users/blenyesibalazs/DevProjects/MCCPython/6. AlgoTrading/Data/GOOGoutput_2003_2023.csv', index_col='date', parse_dates=True)
meta_df = pd.read_csv('/Users/blenyesibalazs/DevProjects/MCCPython/6. AlgoTrading/Data/METAoutput_2003_2023.csv', index_col='date', parse_dates=True)
amzn_df = pd.read_csv('/Users/blenyesibalazs/DevProjects/MCCPython/6. AlgoTrading/Data/AMZNoutput_2003_2023.csv', index_col='date', parse_dates=True)

#normalize the returns
aapl_df['NormReturn'] = aapl_df['last']/aapl_df.iloc[0]['last']
goog_df['NormReturn'] = goog_df['last']/goog_df.iloc[0]['last']
meta_df['NormReturn'] = meta_df['last']/meta_df.iloc[0]['last']
amzn_df['NormReturn'] = amzn_df['last']/amzn_df.iloc[0]['last']

print(aapl_df.iloc[0]['last'])
print(aapl_df.head())

#next, these stocks haven't been listed all at the same time, so let's check what data we have on them 
#print(len(goog_df))
#print(len(aapl_df))
#print(len(meta_df))
#print(len(amzn_df['date']))

#we need uniform length data
min_len = min(len(aapl_df['last']), len(goog_df['last']), len(meta_df['last']), len(amzn_df['last']))

aapl_df = aapl_df.iloc[:min_len, :]
goog_df = goog_df.iloc[:min_len, :]
meta_df = meta_df.iloc[:min_len, :]
amzn_df = amzn_df.iloc[:min_len, :]

#build an allocation table
allocation_aapl = 0.35
allocation_goog = 0.25
allocation_meta = 0.20
allocation_amzn = 0.20

# build the portfolio with allocations to various stocks, via a tuple, this is just a temporary data structure to iterate through everything
for portfolio_df, allocation in zip((aapl_df, goog_df, meta_df, amzn_df),[allocation_aapl,allocation_goog,allocation_meta,allocation_amzn]):
    portfolio_df['Allocation']= portfolio_df['NormReturn'] * allocation


#add position values in the mix

pos_value = 10000
for portfolio_df in (aapl_df, goog_df, amzn_df, meta_df):
    portfolio_df['Position'] = portfolio_df['Allocation'] * pos_value

# now we build a new dataframe to house all our portfolios

all_positions = [aapl_df['Position'], goog_df['Position'], meta_df['Position'], amzn_df['Position']]

portVal = pd.concat(all_positions, axis=1)
portVal.columns = ['AAPL Pos', 'GOOG Pos', 'META Pos', 'AMZN Pos']
# add a column to house everything
portVal['Total Pos'] = portVal.sum(axis=1)

portVal.to_csv('/Users/blenyesibalazs/DevProjects/MCCPython/6. AlgoTrading/4. Portfolio ratios/portfOutput2.csv', index=True)

portVal['Total Pos'].plot(figsize=(10,8))

portVal.drop('Total Pos', axis=1).plot(figsize=(10,8))
plt.show()


