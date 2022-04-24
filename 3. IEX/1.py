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

# resp = requests.get(base_url + '/status')
# print(resp)

# print(resp.json())