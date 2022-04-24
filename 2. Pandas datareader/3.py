#1.3 one way to get a number of ticker data at once

import pandas as pd
import numpy as np

tickers = ['MSFT', 'AAPL', 'GOOG']
portfolio = np.empty([len(tickers)], dtype=object) #initializing a blank array of objects

i=0

 for ticker in tickers: 
     portfolio[i] = pdr.get_data_yahoo(ticker, start='2022-04-01', end='2022-04-22')
     output=pd.DataFrame.from_dict(portfolio[i]) #converting an object to a dataframe so that it can be written to an CSV file
     output.to_csv("C:\\Users\\...\\Python\\"+ticker+"sample2.csv")
     i=i+1
