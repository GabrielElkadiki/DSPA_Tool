import requests
import datetime
import time
import csv
import os

data_list = []


def round_float(string):
    return round(float(string), 3)


def get_date_today_plus_num_days(num_days):
    return datetime.date.today() + datetime.timedelta(days=num_days)


def convert_price_to_delta():
    global data_list
    if len(data_list[0]) == 4:
        return
    else:
        for data_point in data_list:
            open_price = data_point[1]
            close_price = data_point[2]
            if not open_price == 0:
                delta = 100 * ((close_price - open_price) / open_price)
                data_point.append(round_float(delta))
            else:
                data_point.append(0)


def get_data(API_URL, param, symbol):
    global data_list
    file_exists = os.path.exists("./Historic_Data/" + str(symbol) + ".csv")
    if not file_exists:
        try:
            response = requests.get(API_URL, param)
            json = response.json()
        except requests.exceptions.RequestException as e:
            print("Error: {}".format(e))
            return 0, 0
        for j in json:
            if j == "Error Message":
                return False
        csv_file = open("./Historic_Data/" + str(symbol) + ".csv", 'w+')
    else:
        csv_file = open("./Historic_Data/" + str(symbol) + ".csv", 'r')
    line_count = 0
    historic_data = []
    up_to_date = False
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[0] == str(get_date_today_plus_num_days(-1)):
            up_to_date = True
    csv_file = open("./Historic_Data/" + str(symbol) + ".csv")
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = [['Date', 'Open', 'Close']]
    for row in csv_reader:
        if line_count != 0:
            if len(row) != 3:
                historic_data.append([row[0], round_float(row[1]), round_float(row[4])])
            else:
                historic_data.append([row[0], round_float(row[1]), round_float(row[2])])
        line_count += 1
    full_data = []
    if not up_to_date and not file_exists:
        try:
            response = requests.get(API_URL, param)
            json = response.json()
        except requests.exceptions.RequestException as e:
            print("Error: {}".format(e))
            return 0, 0
        raw_recent_data = (json['Time Series (Daily)'])
        keys = (raw_recent_data.keys())
        recent_data = []
        line_count = 0
        if not keys == 0:
            for key in keys:
                if line_count != 0:
                    recent_data.append(
                        [key,
                         round_float(raw_recent_data[key]['1. open']),
                         round_float(raw_recent_data[key]['4. close']),
                         ])
                line_count += 1
        full_data_list_tuple = list(set(tuple(i) for i in (recent_data + historic_data)))
        for data in full_data_list_tuple:
            full_data.append([data[0], data[1], data[2]])
    else:
        full_data_list_tuple = list(set(tuple(i) for i in historic_data))
        for data in full_data_list_tuple:
            full_data.append([data[0], data[1], data[2]])
    full_data.sort(key=lambda date: time.mktime(time.strptime(date[0], "%Y-%m-%d")))
    with open("./Historic_Data/" + str((symbol)) + ".csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(csv_header)
    with open("./Historic_Data/" + str((symbol)) + ".csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(full_data)
    data_list = full_data
    convert_price_to_delta()
    return True


def clear_data():
    global data_list
    data_list = []


def get_year_span():
    global data_list
    oldest_year = min(int(data[0].split("-")[0]) for data in data_list)
    current_year = max(int(data[0].split("-")[0]) for data in data_list)
    year_span_size = int(current_year) - int(oldest_year) + 1
    year_span = []
    for i in range(year_span_size):
        year_span.append(int(oldest_year) + i)
    return year_span


def apply_month_range(month_range):
    global data_list
    filtered_data_list = []
    for data_point in data_list:
        if data_point[0].split("-")[1] in month_range:
            filtered_data_list.append(data_point)
    return filtered_data_list


def max_delta(filtered_data_list):
    if filtered_data_list is None:
        filtered_data_list = data_list
        max_delta_string = "Max Delta in present Data:"
    else:
        max_delta_string = ""
    max_increase = [0, ""]
    max_decrease = [0, ""]
    if len(data_list[0]) == 3:
        convert_price_to_delta(data_list)
    for data_point in filtered_data_list:
        delta = data_point[3]
        if delta > max_increase[0]:
            max_increase = [delta, data_point[0]]
        if delta < max_decrease[0]:
            max_decrease = [delta, data_point[0]]
        max_increase[0] = round_float(max_increase[0])
        max_decrease[0] = round_float(max_decrease[0])
    max_delta_string += (
            "\nMax Increase = " + str(max_increase[0]) + "   On " + max_increase[1] +
            "\nMax Decrease = " + str(max_decrease[0]) + "   On " + max_decrease[1]
    )
    return max_delta_string


def monthly_max_delta():
    global data_list
    month_range = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    month_name = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    count = 0
    monthly_maximum_delta_string = ""
    for month in month_range:
        monthly_maximum_delta_string += (
                "\n                 " + month_name[count] +
                max_delta(apply_month_range([month])) +
                "\n______________________________"
        )
        count += 1
    return monthly_maximum_delta_string


def compare_past_dates(start_date, stop_date):
    global data_list
    target_date_list = []
    start_date = start_date.toPyDate()
    stop_date = stop_date.toPyDate()
    for i in range((stop_date - start_date).days + 1):
        target_date = (start_date + datetime.timedelta(days=i))
        day = str(target_date.day)
        if len(day) == 1:
            day = "0" + day
        month = str(target_date.month)
        if len(month) == 1:
            month = "0" + month
        target_date_list.append(month + "-" + day)
    target_delta_list = []
    same_date_list = []
    for target in target_date_list:
        for data in data_list:
            if data[0].split("-")[1] + "-" + (data[0]).split("-")[2] == target:
                same_date_list.append(data)
        target_delta_list.append(same_date_list)
        same_date_list = []
    compare_past_dates_string = (
        "This is a list of comparisons made with past dates of the data available. " +
        "\nThis works best when there are multiple years of data within the CSV file" +
        "\n______________________________"
    )
    for target_list in target_delta_list:
        date = ""
        pos_count = 0
        neg_count = 0
        pos_delta_sum = 0
        neg_delta_sum = 0
        for target in target_list:
            date = target[0].split("-")[1] + "-" + (target[0]).split("-")[2]
            if target[3] >= 0:
                pos_count += 1
                pos_delta_sum += target[3]
            else:
                neg_count += 1
                neg_delta_sum += target[3]
        if pos_count + neg_count > 0:
            pbty_up = 100 * pos_count / (pos_count + neg_count)
            pbty_down = 100 * neg_count / (pos_count + neg_count)
            if pos_count > 0:
                avg_increase = str(round_float(pos_delta_sum / pos_count))
            else:
                avg_increase = "0"
            if neg_count > 0:
                avg_decrease = str(round_float(neg_delta_sum / neg_count))
            else:
                avg_decrease = "0"
            compare_past_dates_string += (
                    "\nOn " + date + ":" +
                    "\nProbability of increase = " + str(round_float(pbty_up)) + "%" +
                    "\nAverage increase change = " + avg_increase + "%" +
                    "\nProbability of decrease = " + str(round_float(pbty_down)) + "%" +
                    "\nAverage decrease change = " + avg_decrease + "%" +
                    "\nNumber of years = " + str(pos_count + neg_count) +
                    "\n______________________________"
            )
    return compare_past_dates_string


def calculate_price_delta(start_date, stop_date):
    global data_list
    start_date = start_date.toPyDate()
    stop_date = stop_date.toPyDate()
    if (stop_date - start_date).days < 0:
        return "Invalid Date Range Entered\nMake sure the Stop Date is after the Start Date"
    start_price = -1
    stop_price = -1
    start_date_string = "Start Date: "
    stop_date_string = "Stop Date: "
    for i in range(4):
        for data in data_list:
            if data[0] == str(start_date):
                start_price = data[1]
            if data[0] == str(stop_date):
                stop_price = data[2]
            if start_price > -1 and stop_price > -1:
                break
        if start_price == -1:
            start_date += datetime.timedelta(days=1)
            start_date_string = "Adjusted Start Date: "
        if stop_price == -1:
            stop_date += datetime.timedelta(days=1)
            stop_date_string = "Adjusted Stop Date: "
        if start_price > -1 and stop_price > -1:
            break
    if start_price == -1 or stop_price == -1:
        return "Data does not exist\nMake sure Dates can be found within local data file"
    percent_change = 100 * ((stop_price - start_price)/start_price)
    return (
            start_date_string + str(start_date) +
            "\n" + "Start Price = " + str(start_price) +
            "\n" + stop_date_string + str(stop_date) +
            "\n" + "Stop Price = " + str(stop_price) +
            "\nPercentage Change = " + str(round(percent_change, 3)) + "%"
    )


def reset(symbol):
    global data_list
    API_URL = "https://www.alphavantage.co/query"
    param = {"function": "TIME_SERIES_DAILY",
            "symbol": symbol,
            "outputsize": "compact",
            "apikey": "XXX"}
    data_list_string = ""
    valid_ticker = get_data(API_URL, param, symbol)
    if not valid_ticker:
        return False
    for data in data_list:
        delta_string = data[3]
        if delta_string > 0:
            delta_string = " " + str(delta_string)
        data_list_string += str(data[0]) + " = " + str(delta_string) + "%\n"
    return data_list_string

