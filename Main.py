import requests
import xlrd

API_URL = "https://www.alphavantage.co/query"
symbols = ['aapl']

for symbol in symbols:
    data = {"function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "outputsize": "compact",
            "apikey": "XXX"}
    response = requests.get(API_URL, data)
    data = response.json()
    print(symbol)
    a = (data['Time Series (Daily)'])
    keys = (a.keys())
    i = 0
    for key in keys:
        print(str(key) + ". " + a[key]['2. high'])
