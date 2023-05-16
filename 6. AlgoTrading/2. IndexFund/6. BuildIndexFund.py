import pandas as pd
import math
import simplefix
import csv

#load the constituents into the dataframe
constituents_df = pd.read_csv('/Users/blenyesibalazs/DevProjects/MCCPython/6. AlgoTrading/SnP500/SNP500Constituents.csv')

#calculate number of shares to buy from each, based on volume
portfolio_size = float(10000000)
position_size = portfolio_size/len(constituents_df.index)

#calculate allocated funds to each position
total_volume = constituents_df['Volume'].sum()
constituents_df['Proportion of Portfolio'] = constituents_df['Volume'] / total_volume
constituents_df['Allocation'] = constituents_df['Proportion of Portfolio'] * portfolio_size

#calculate the number of shares
for i in range(0, len(constituents_df.index)):
    constituents_df.loc[i, 'Number of Shares to buy'] = math.floor(constituents_df.loc[i, 'Allocation'] / constituents_df.loc[i, 'LastPrice'])
    #this is just to provide a checkpoint
    constituents_df.loc[i, 'Position Value'] = constituents_df.loc[i, 'Number of Shares to buy'] * constituents_df.loc[i, 'LastPrice']

#initialize new writer object

with pd.ExcelWriter("Recommended trades.xlsx") as writer:
    constituents_df.to_excel(writer)

#now we build some FIX messages off of this

messages = []

for i in range(0, len(constituents_df.index)):
    msg = simplefix.FixMessage()
    msg.append_pair(8, "FIX.4.4")
    msg.append_pair(35, "D")
    msg.append_pair(49, "SENDER")
    msg.append_pair(56, "TARGET")
    msg.append_pair(112, "TR1")
    msg.append_pair(34, 4684, header=True)
    msg.append_utc_timestamp(52, precision=6, header=True)
    msg.append_pair(1, "This is my account")
    msg.append_pair(54, 1)
    msg.append_pair(40, 1)
    msg.append_pair(11, str(i))
    msg.append_pair(38, constituents_df.loc[i, 'Number of Shares to buy'])
    msg.append_pair(55, constituents_df.loc[i, 'Ticker'])
    print(msg.encode("utf-8"))
    messages.append(msg.encode("utf-8"))


with open('fix_messages.csv', 'a') as file:
    csv_writer = csv.writer(file)
    for message in messages:
        #encoded_message = str(message).encode("utf-8")
        csv_writer.writerow([message])
