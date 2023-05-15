import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def filter_df_by_time_range(df, start_time, end_time):
    # Convert date columns to datetime type
    df['date'] = pd.to_datetime(df['date'])
    
    # Filter dataframe between start and end time
    filtered_df = df[(df['date'] >= start_time) & (df['date'] <= end_time)]
    filtered_df.set_index('date', inplace=True)

    return filtered_df

df = pd.read_csv('/Users/blenyesibalazs/DevProjects/MCCPython/6. AlgoTrading/Data/AAPLoutput_2003_2023.csv')

stock_10 = filter_df_by_time_range(df,'2013-01-01', '2023-01-01').resample('M').mean()
stock_5 = filter_df_by_time_range(df,'2018-01-01', '2023-01-01').resample('M').mean()
stock_2 = filter_df_by_time_range(df,'2021-01-01', '2023-01-01').resample('M').mean()
stock_1 = filter_df_by_time_range(df,'2022-01-01', '2023-01-01').resample('M').mean()

monthly_returns_10 = stock_10["last"].pct_change()
monthly_returns_5 = stock_5["last"].pct_change()
monthly_returns_2 = stock_2["last"].pct_change()
monthly_returns_1 = stock_1["last"].pct_change()

# Create subplots
fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(10, 8))

fig.suptitle("Density analysis of AAPL returns over 1,2,5, 10yr horizons", fontsize=20)

axs[0, 0].hist(monthly_returns_10, bins=20, edgecolor='black', density=True)
sns.kdeplot(monthly_returns_10, ax=axs[0, 0])
axs[0, 0].set_title("Density Plot of 10yr Monthly Returns")

axs[0, 1].hist(monthly_returns_5, bins=20, edgecolor='black', density=True)
sns.kdeplot(monthly_returns_5, ax=axs[0, 1])
axs[0, 1].set_title("Density Plot of 5yr Monthly Returns")

axs[1, 0].hist(monthly_returns_2, bins=20, edgecolor='black', density=True)
sns.kdeplot(monthly_returns_2, ax=axs[1, 0])
axs[1, 0].set_title("Density Plot of 2yr Monthly Returns")

axs[1, 1].hist(monthly_returns_1, bins=20, edgecolor='black', density=True)
sns.kdeplot(monthly_returns_1, ax=axs[1, 1])
axs[1, 1].set_title("Density Plot of 1yr Monthly Returns")

#overlaid density plots
sns.kdeplot(monthly_returns_10, ax=axs[0, 2])
sns.kdeplot(monthly_returns_5, ax=axs[0, 2])
sns.kdeplot(monthly_returns_2, ax=axs[0, 2])
sns.kdeplot(monthly_returns_1, ax=axs[0, 2])
axs[0,2].set_title("Overlaid density plots.")

# Add spacing between subplots
fig.tight_layout(pad=3.0)

# Show the plot
plt.show()

