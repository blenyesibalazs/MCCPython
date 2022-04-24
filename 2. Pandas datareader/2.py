#1.2 request the data only from a certain time period

from datetime import datetime
data2 = pdr.get_data_yahoo('AMD', datetime(2022, 2, 20))
print(data2.info())
data2.to_csv("C:\\Users\\...\\Python\\sample2.csv")
