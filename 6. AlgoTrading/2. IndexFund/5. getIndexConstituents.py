import requests
import pandas as pd
import datetime as dt

def scrapeSNP500():
        table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
        df = table[0]
        df.to_csv('/Users/blenyesibalazs/DevProjects/MCCPython/6. AlgoTrading/SnP500/S&P500-Info.csv')
        df.to_csv('/Users/blenyesibalazs/DevProjects/MCCPython/6. AlgoTrading/SnP500S&P500-Symbols.csv', columns=['Symbol'])
        df['Symbol']

        return df

def login(username, password):
        #generic login credentials and request counter
        request_ID = '8'
        #login request JSON
        LoginParams = {"request_data": request_ID, 
            "md_login_request": {
                "login_id": username, 
                "password": password, 
                "client_application": "WEB", 
                "client_application_version": "1.0", 
                "country_code": "SE", 
                "language_code": "En" }}
        #service routing requests JSON
        getServiceRoutingRequestsParams = {"get_service_routings_request": {
                "login_id": username, 
                "password": password, 
                "client_application": "WEB", 
                "client_application_version": "1.0", 
                "country_code": "SE", 
                "language_code": "En" }}
        #JSON requests
        #login
        login = requests.post(url='https://mws8.infrontservices.com:8089', json=LoginParams).json()
        session_token = login['session_token']
        return session_token

session_token=login("balazs.blenyesi","Infront2021!")

def getHistoryRequest(session_token, feed, ticker, start_date, end_date):
        request_ID = '2'

        getHistoryRequestParams = {
        "session_token": session_token,
        "md_get_history_request": {
                "instruments": [
                        { "feed": feed,
                        "ticker": ticker
                        }
                ],
                "start_date": start_date,
                "end_date": end_date 
                }
        }

        getHistory = requests.post(url='https://mws8.infrontservices.com:8089', json=getHistoryRequestParams).json()

        date = getHistory['md_get_history_response']['trades'][0]['date']
        closing_price = getHistory['md_get_history_response']['trades'][0]['last']
        ticker = getHistory['md_get_history_response']['trades'][0]['ticker']
        volume = getHistory['md_get_history_response']['trades'][0]['volume']

        return ticker, date, closing_price, volume


#all tickers
tickerss=scrapeSNP500()

#then separating out the tickers into the likely venue of listing
NYSETickers = []
NASDAQTickers = []

NYSETickers = tickerss[tickerss['Symbol'].apply(lambda x: len(str(x)) == 3)]
NASDAQTickers = tickerss[tickerss['Symbol'].apply(lambda x: len(str(x)) == 4)]

NASDAQSymbol_list = NASDAQTickers["Symbol"].tolist()
NYSESymbol_list = NYSETickers["Symbol"].tolist()

OutputData = []

for ticker in NASDAQSymbol_list:
        print("Ticker is:",ticker)
        try:
            NASDAQdata = getHistoryRequest(session_token, 15, ticker, '2023-05-05', '2023-05-05')
            OutputData.append(NASDAQdata)
        except KeyError:
            print(f"No historical trading data found for NASDAQ ticker {ticker}, trying NYSE.")
            NASDAQdata = getHistoryRequest(session_token, 14, ticker, '2023-05-05', '2023-05-05')
            OutputData.append(NASDAQdata)

print("Finished writing NASDAQ data to memory")

for ticker in NYSESymbol_list:
        print("Ticker is:",ticker)
        try:
            NYSEData = getHistoryRequest(session_token, 14, ticker, '2023-05-05', '2023-05-05')
            OutputData.append(NYSEData)
        except KeyError:
            print(f"No historical trading data found for NYSE ticker {ticker}, trying NASDAQ.")
            NYSEData = getHistoryRequest(session_token, 15, ticker, '2023-05-05', '2023-05-05')
            OutputData.append(NYSEData)

print("Finished writing NYSE data to memory")

df = pd.DataFrame(OutputData)
df.to_csv('/Users/blenyesibalazs/DevProjects/MCCPython/6. AlgoTrading/Data/SNP500Constituents.csv', index=False)

print("Finished writing data CSV")


#don't run this yet. this is too much to bombard MWS with


