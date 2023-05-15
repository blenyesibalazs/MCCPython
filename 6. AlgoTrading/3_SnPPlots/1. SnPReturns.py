import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

start_date = pd.Timestamp('2014-01-01')
end_date = pd.Timestamp.today()
snp500 = web.DataReader('SP500', 'fred', start_date, end_date)
snp500_monthly = snp500.resample('M').mean()
print(snp500_monthly)

# Calculate monthly returns
monthly_returns = snp500_monthly["SP500"].pct_change()

# Create subplots
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

fig.suptitle("10 yr analysis of SnP returns", fontsize=20)

# Plot box plot of monthly returns in fourth column
axs[0, 0].plot(snp500_monthly)
axs[0, 0].set_title("Monthly closing prices")

# Plot line plot of monthly returns in first column
axs[0, 1].plot(monthly_returns.index, monthly_returns)
axs[0, 1].set_title("Monthly Returns")

# Distribution plot ... under the curve means probability of observing values in the given range
axs[1, 0].hist(monthly_returns, bins=20, edgecolor='black', density=True)
sns.kdeplot(monthly_returns, ax=axs[1, 0])
axs[1, 0].set_title("Density Plot of Monthly Returns")

# Density plot ... under the curve means probability of observing values in the given range
axs[1, 1].hist(monthly_returns, bins=20, edgecolor='black')
axs[1, 1].set_title("Distribution of Monthly Returns")

# Add spacing between subplots
fig.tight_layout(pad=3.0)

# Show the plot
plt.show()

