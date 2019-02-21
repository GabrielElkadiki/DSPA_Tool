import matplotlib.pyplot as plt
import requests
import csv
import sys
import os


def getCurrentData(API_URL, symbol, data):
    try:
        response = requests.get(API_URL)
        print(response.status_code)
        data = response.json()
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(1)
    rawRecentData = (data['Time Series (Daily)'])
    keys = (rawRecentData.keys())
    print("Stock Ticker: " + symbol.upper())
    return rawRecentData, keys


API_URL = "https://www.alphavantage.co/query"
symbol = 'aapl'
monthRange = ["1", "2"]
data = {"function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": "compact",
        "apikey": "XXX"}
rawRecentData, keys = getCurrentData(API_URL, symbol, data)
oldestYear = 0
currentYear = 0
recentData = []
lineCount = 0
for key in keys:
    if lineCount == 0:
        currentYear = key.split("-")[0]
    else:
        recentData.append([key, round(float(rawRecentData[key]['1. open']), 3), round(float(rawRecentData[key]['4. close']), 3)])
    lineCount += 1
if not os.path.exists("./Historic_Data/" + str(symbol) + ".csv"):
    print("END: Specified stock ticker historic data is unavailable")
else:
    csv_file = open("./Historic_Data/" + str(symbol) + ".csv")
    csv_reader = csv.reader(csv_file, delimiter=',')
    lineCount = 0
    historicData = []
    for row in csv_reader:
        if lineCount == 1:
            oldestYear = row[0].split("-")[0]
        elif lineCount != 0:
            historicData.append([row[0], round(float(row[1]), 3), round(float(row[4]), 3)])
        lineCount += 1
    fullData = sorted(set(tuple(i)for i in (recentData + historicData)))
    yearSpanSize = int(currentYear) - int(oldestYear) + 1
    yearSpan = []
    for i in range(yearSpanSize):
        yearSpan.append(int(oldestYear) + i)
    print(yearSpan)
