import requests
import csv
API_URL = "https://www.alphavantage.co/query"
symbol = 'aapl'
monthRange = ["1", "2"]
data = {"function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": "compact",
        "apikey": "XXX"}
response = requests.get(API_URL, data)
data = response.json()
print("Stock Ticker: " + symbol.upper())
rawRecentData = (data['Time Series (Daily)'])
keys = (rawRecentData.keys())
oldestYear = 0
currentYear = 0
recentData = []
for key in keys:
    recentData.append(key + " " + rawRecentData[key]['1. open'] + " " + rawRecentData[key]['4. close'])
csv_file = open("./Historic_Data/" + str(symbol) + ".csv")
csv_reader = csv.reader(csv_file, delimiter=',')
line_count = 0
historicData = []
for row in csv_reader:
    if line_count == 1:
        oldestYear = row[0].split("-")[0]
    historicData.append(row[0] + " " + row[1] + " " + row[4])
    line_count += 1
fullData = list(set(recentData + historicData))
for i in range(len(fullData)):
    fullDataEntry = fullData[i].split(" ")
    fullData[i] = [fullDataEntry[0], fullDataEntry[1], fullDataEntry[2]]
for data in fullData:
    print(data)
