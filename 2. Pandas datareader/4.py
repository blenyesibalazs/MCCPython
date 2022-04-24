#1.4 get historic FX rates
from pandas_datareader import data
eurusd = data.get_data_fred('DEXUSEU')
print(eurusd) #https://fred.stlouisfed.org/series/DEXUSEU resource to check on the various currency pairs. 