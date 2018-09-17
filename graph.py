# libraries
import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import codecs
import csv

# Fill up the data
r = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
df = pd.DataFrame(index=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30'], dtype=np.float64)
df['General'] = 0.0
df['Finance'] = 0.0
df['Trade-In'] = 0.0
df['Test Drive'] = 0.0

file = open('Data/messages.csv', 'r')
reader = csv.reader(codecs.EncodedFile(file, 'utf-8', 'utf-8-sig'))

for row in reader:
    if row[1] == '1':
        df.at[row[0], "General"] += 1
    if row[1] == '2':
        df.at[row[0], 'Finance'] += 1
    if row[1] == '3':
        df.at[row[0], "Trade-In"] += 1
    if row[1] == '4':
        df.at[row[0], "Test Drive"] += 1

# From raw value to percentage
totals = [i + j + k + z for i, j, k, z in zip(df['General'], df['Finance'], df['Trade-In'], df['Test Drive'])]
general = [i / j * 100 for i, j in zip(df['General'], totals)]
finance = [i / j * 100 for i, j in zip(df['Finance'], totals)]
tradeIn = [i / j * 100 for i, j in zip(df['Trade-In'], totals)]
testDrive = [i / j * 100 for i, j in zip(df['Test Drive'], totals)]

# plot
barWidth = 0.85

x_axis = []
for i in range(1, 31):
    x_axis.append(i)

colorGreen = '#b5ffb9'
colorYellow = '#f9bc86'
colorBlue = '#a3acff'
colorOrange = '#cc4a01'

barGeneral = plt.bar(r, general, color=colorGreen, edgecolor='white', width=barWidth)
barTradeIn = plt.bar(r, tradeIn, bottom=general, color=colorYellow, edgecolor='white', width=barWidth)
barFinance = plt.bar(r, finance, bottom=[i + j for i, j in zip(general, tradeIn)], color=colorBlue, edgecolor='white',
        width=barWidth)
barTestDrive = plt.bar(r, testDrive, bottom=[i + j + z for i, j, z, in zip(general, finance, tradeIn)], color=colorOrange, edgecolor='white', width=barWidth)

# Custom x axis
plt.xticks(r, x_axis)
plt.xlabel("Vehicle enquiries over the month of August")
plt.legend((barGeneral, barTradeIn, barFinance, barTestDrive), ('General', 'Trade-In', 'Finance', 'Test Drive'))

# Show graphic
plt.show()
