import pandas as pd
import requests
from termcolor import colored as cl
import matplotlib.pyplot as plt

def get_historic_data(symbol):
    ticker = symbol
    sandbox_api_key = 'Tpk_996563da4d694cf09d8f14ae6de43d38'
    sandbox_api_url = f'https://sandbox.iexapis.com/stable/stock/{ticker}/chart/max?token={sandbox_api_key}'
    df = requests.get(sandbox_api_url).json()

    date = []
    open = []
    high = []
    low = []
    close = []
    
    for i in range(len(df)):
        date.append(df[i]['date'])
        open.append(df[i]['open'])
        high.append(df[i]['high'])
        low.append(df[i]['low'])
        close.append(df[i]['close'])
    
    date_df = pd.DataFrame(date).rename(columns = {0:'date'})
    open_df = pd.DataFrame(open).rename(columns = {0:'open'})
    high_df = pd.DataFrame(high).rename(columns = {0:'high'})
    low_df = pd.DataFrame(low).rename(columns = {0:'low'})
    close_df = pd.DataFrame(close).rename(columns = {0:'close'})
    
    frames = [date_df, open_df, high_df, low_df, close_df]
    df = pd.concat(frames, axis = 1, join = 'inner')
    df = df.set_index('date')
    
    df['close'].plot()
    plt.title('{} Historical Prices'.format(ticker), fontsize = 18)
    plt.xlabel('Date', fontsize = 14)
    plt.ylabel('Stock Price', fontsize = 14)
    plt.xticks(fontsize = 12)
    plt.yticks(fontsize = 12)
    plt.show()
    
    return df

get_historic_data('AAPL')