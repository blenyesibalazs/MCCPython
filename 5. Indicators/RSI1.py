#Wilder 1978-ban vezette be az RSI fogalmat. Eredetileg szamos problema volt vele, mint peldaul a momentum gorbek erratikus oszcillalasa. Ezt kesobb egy masodik iteracio is kijavitotta

# 14 napos RSI, 14 napos periodusok armozgasaira van szuksegunk
# Legyen 1 nap 1 periodus
# Az elso 14 napos intervallumra, szamitsuk ki az aringadozasokat periodusrol periodusra
# Minden egyes periodusra (napra), "konyveljuk el" a pozitiv armozgast mind nyereseget, a negativ armozgast mint veszteseget
# A 14. perioduson szamitsuk ki az elozo 14 nap nyeresegeinek es vesztesegeinek szamtani kozepet. (nyereseg/14 es veszteseg/14)
# Ezek alapjan szamolunk RS-t
# RS-t felhasznalva szamolunk RSI-t
# Mindenik kovetkezo periodusra az elozo periodus RSI erteket felhasznalva tudjuk a kovetkezo RSIt szamolni. i.e. A teljes RSI-t 0-rol csak az elso periodusra szamolom ki
# 3 metodus: csak Python, pandas es pandas_ta

#csak tiszta python...

from audioop import avg
import numpy as np
import csv

from numpy import double

with open('wilder-rsi-data.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    wilder_data = [row[1] for row in list(reader)]

# bazis intervallum
window_length = 14 

# nyereseg es veszteseg tarolasa
gains = []
losses = []

# mozgo "ablak"
window = []

prev_avg_gain = int(0)
prev_avg_loss = int(0)

output = [['date', 'close', 'gain', 'loss', 'avg_gain', 'avg_loss', 'rsi']]

for i, price in enumerate(wilder_data):
    # inicializalom a valtozoimat, az elso ertekkel
    if i == 0:
        window.append(price)
        output.append([i+1, price, 0, 0, 0, 0, 0])
        continue
    # Elso lepes kiszamolom az arkulonbsegeket, kerekitve
    difference = round(float(wilder_data[i]) - float(wilder_data[i - 1]),2)
    #print(round(float(wilder_data[i]) - float(wilder_data[i-1]),2))
    #masodik lepes, nyereseged, veszteseget szamolok
    # nyereseg
    if difference > 0:
         gain = difference
         loss = 0
    elif difference < 0: # veszteseg
         gain = 0
         loss = abs(difference)
    else: # ez sem az sem
         gain = 0
         loss = 0
    # #feltoltom a nyeresegeket es vesztesegeket tartalmazo array-eket
    gains.append(gain)
    losses.append(loss)
    
    # if (gains[i]>losses[i]):
    #     print("gain[i]=", gains[i], "loss[i]=", losses[i])
    # elif (gains[i]<losses[i]):
    #     print("loss[i]", losses[i], "gain[i]=", gains[i])

    # feltoltom a tobbi adatomat is az elso 14 periodusig. A 14. periodus utan tudok csak RSI-t kezdeni szamolni
    if i < window_length:
         window.append(price)
         output.append([i+1, price, gain, loss, 0, 0, 0])
         #print(output[i])
        #print(sum(gains))
        #print(sum(losses))
    #  Masodik lepes, atlag arkulonbsegeket
    elif i == window_length:
        # harmadik lepes, atlag nyeresegek vesztesegeket szamolok
        avg_gain = sum(gains) / len(gains)
        avg_loss = sum(losses) / len(losses)
        rs = round(avg_gain / (avg_loss), 2)
        rsi = round(100 - (100 / (1 + rs)), 2)
        output.append([i+1, price, gain, loss, round(avg_gain,2), round(avg_loss,2), rsi])
        prev_avg_gain = avg_gain
        prev_avg_loss = avg_loss
    elif i > window_length: # Use WSM after initial window-length period
        avg_gain = (prev_avg_gain * (window_length - 1) + gain) / window_length
        avg_loss = (prev_avg_loss * (window_length - 1) + loss) / window_length

        # az elozo ertekek eszben tartasa
        prev_avg_gain = avg_gain
        prev_avg_loss = avg_loss
        # szebb az elet kereken
        avg_gain = round(avg_gain, 2)
        avg_loss = round(avg_loss, 2)
        prev_avg_gain = round(prev_avg_gain, 2)
        prev_avg_loss = round(prev_avg_loss, 2)
        
        # RS szamitas
        rs = round(avg_gain / avg_loss, 2)
        # RSI szamitas
        rsi = round(100 - (100 / (1 + rs)), 2)

        # Remove oldest values
        window.append(price)
        window.pop(0)
        gains.pop(0)
        losses.pop(0)

        output.append([i+1, price, gain, loss, avg_gain, avg_loss, rsi])

# az eredmenyek
with open('wilder-rsi-data-output.csv', 'w+', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(output)
