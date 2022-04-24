from ensurepip import version
import os
from sys import api_version
import pandas as pd
import requests

#print(os.environ.get('IEX_TOKEN')) check if we have the proper variable name stored

#check status of the main endpoint

# import requests 

base_url = 'https://cloud.iexapis.com/stable'
sandbox_url = 'https://sandbox.iexapis.com/stable'
token = os.environ.get('IEX_TOKEN')

params = {'token': token}
sandbox_params = {'token': 'Tpk_996563da4d694cf09d8f14ae6de43d38'}

def get_historical_data(_symbol, _range=None, _date=None):
    endpoint = f'{base_url}/stock/{_symbol}/chart'
    if _range:
        endpoint += f'/{_range}'
    elif _date:
        endpoint += f'/date/{_date}'
    
    resp = requests.get(endpoint, params=params)
    resp.raise_for_status()
    return pd.DataFrame(resp.json())

nvda_3m_df = get_historical_data('NVDA', _range='3m')
