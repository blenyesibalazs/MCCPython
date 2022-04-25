import pandas as pd
import requests
from termcolor import colored as cl
import os
from sys import api_version

def get_latest_updates(*symbols):
    for i in symbols:
        ticker = i
        iex_api_key = os.environ.get('IEX_TOKEN')
        sandbox_api_key = 'Tpk_996563da4d694cf09d8f14ae6de43d38'
        api_url = f'https://cloud.iexapis.com/stable/stock/{ticker}/quote?token={iex_api_key}'
        sandbox_url = f'https://sandbox.iexapis.com/stable/stock/{ticker}/quote?token={sandbox_api_key}'
        df = requests.get(api_url).json()
        
        print(cl('Latest Updates of {}\n--------------'.format(ticker), attrs = ['bold']))
        attributes = ['symbol', 
                      'latestPrice', 
                      'marketCap', 
                      'peRatio']
        for i in attributes:
            print(cl('{} :'.format(i), attrs = ['bold']), '{}'.format(df[i]))    
        print(cl('--------------\n', attrs = ['bold']))

get_latest_updates('FB', 'AAPL', 'AMZN', 'NFLX', 'GOOGL')

