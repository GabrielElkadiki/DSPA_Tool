import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import requests
import calendar
import csv
import sys
import os


def round_float(string):
    return round(float(string), 3)


def get_current_raw_cata(API_URL, symbol, data):
    try:
        response = requests.get(API_URL, data)
        print(response.status_code)
        json = response.json()
    except requests.exceptions.RequestException as e:
        print("Error: {}".format(e))
        sys.exit(1)
    raw_recent_data = (json['Time Series (Daily)'])
    keys = (raw_recent_data.keys())
    print("Stock Ticker: " + symbol.upper())
    return raw_recent_data, keys


def extract_data(raw_recent_data, keys):
    recent_data = []
    line_count = 0
    oldest_year = 0
    current_year = 0
    for key in keys:
        if line_count == 0:
            current_year = key.split("-")[0]
        else:
            recent_data.append(
                [key, round_float(raw_recent_data[key]['1. open']), round_float(raw_recent_data[key]['4. close'])])
        line_count += 1
    if not os.path.exists("./Historic_Data/" + str(symbol) + ".csv"):
        print("ERROR: Specified stock ticker historic data is unavailable")
    else:
        csv_file = open("./Historic_Data/" + str(symbol) + ".csv")
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        historic_data = []
        for row in csv_reader:
            if line_count == 1:
                oldest_year = row[0].split("-")[0]
            elif line_count != 0:
                historic_data.append([row[0], round_float(row[1]), round_float(row[4])])
            line_count += 1
        full_data = sorted(set(tuple(i) for i in (recent_data + historic_data)))
        year_span_size = int(current_year) - int(oldest_year) + 1
        year_span = []
        new_data_list = []
        for data_point in full_data:
            new_data_list.append([data_point[0], (data_point[1]), (data_point[2])])
        for i in range(year_span_size):
            year_span.append(int(oldest_year) + i)
        return new_data_list, year_span


API_URL = "https://www.alphavantage.co/query"
symbol = 'aapl'
monthRange = ["1", "2"]
data = {"function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": "compact",
        "apikey": "XXX"}
rawRecentData, keys = get_current_raw_cata(API_URL, symbol, data)
dataList, yearSpan = extract_data(rawRecentData, keys)
for data in dataList:
    print(data)
x = []
y = []
colorList = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w']  # Supports 8 years Max
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
i = 0
scale = []
for year in yearSpan:
    for data in dataList:
        dateSplit = data[0].split("-")
        if int(dateSplit[0]) == year:
            x.append(dateSplit[2] + "-" + dateSplit[1])
            y.append(round(((data[1] - data[2]) / data[1]), 3))
    xCount = 0
    plt.scatter(x, y, 3, label=year)
    plt.legend(loc=1)
    i += 1
    x.clear()
    y.clear()
    scale.clear()

plt.show()
plt.close()
