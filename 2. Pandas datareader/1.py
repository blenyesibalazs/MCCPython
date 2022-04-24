#1.1  Request data via Yahoo public API

import pandas_datareader as pdr

data = pdr.get_data_yahoo('NVDA')
print(data.info()) #print column headers
#output the data we got as a csv to a target directory.
data.to_csv("C:\\Users\\...\\Python\\sample.csv")
