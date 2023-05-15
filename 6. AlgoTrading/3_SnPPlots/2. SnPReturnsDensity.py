import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def snpReturns(sd, ed):
    start_date = pd.Timestamp(sd)
    end_date = pd.Timestamp(ed)
    
    snp500 = web.DataReader('SP500', 'fred', start_date, end_date)
    return snp500

#--main--
# Calculate monthly returns then display them  over 10 years, 5 years, 2 years and 1 year

today = pd.Timestamp.today()
print(snpReturns('2014-01-01', '2015-01-01'))
print(type(snpReturns('2014-01-01', '2015-01-01')))

snp500_10 = snpReturns('2014-01-01', today).resample('M').mean()
snp500_5 = snpReturns('2018-01-01', today).resample('M').mean()
snp500_2 = snpReturns('2021-01-01', today).resample('M').mean()
snp500_1 = snpReturns('2022-01-01', today).resample('M').mean()

monthly_returns_10 = snp500_10["SP500"].pct_change()
monthly_returns_5 = snp500_5["SP500"].pct_change()
monthly_returns_2 = snp500_2["SP500"].pct_change()
monthly_returns_1 = snp500_1["SP500"].pct_change()

# Create subplots
fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(10, 8))

fig.suptitle("Density analysis of SnP returns over 1,2,5, 10yr horizons", fontsize=20)

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

