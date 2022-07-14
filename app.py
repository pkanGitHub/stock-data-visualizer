from flask import Flask, jsonify
from datetime import datetime
import requests
import json
# from userPrompt import *

app = Flask(__name__)
app.config.from_pyfile('config.py')

API_KEY = app.config.get("API_KEY")

# symbol = get_symbol()
# chart = chart_type_selection()

# startDate = get_start_date()
# endDate = get_end_date(startDate)

# @app.route('/', methods=['GET'])

# def get_url(symbol, timeSeries, API_KEY):
#     return f"https://www.alphavantage.co/query?function={timeSeries}&symbol={symbol}&apikey={API_KEY}"

def get_symbol():
    symbol = input("Enter the stock symbol you are looking for: ").upper()
    return symbol


def get_data(time_series, start_date, end_date):
    url = time_series
    # url = f"https://www.alphavantage.co/query?function={time_series}&symbol={symbol}&apikey={API_KEY}"
    # url = get_url(symbol, timeSeries, API_KEY)
    stock_data = requests.get(url).json()
    # print(stock_data['Weekly Time Series']['2022-07-13']['1. open'])
    for key, value in stock_data['Weekly Time Series'].items():
        # to print dates between start date and end date
        if (key > start_date) and (key < end_date):
            print(key, value)
            json_string = json.dumps(stock_data)
            with open('json_data.json', 'w') as outfile:
                outfile.write(json_string)


# prompt user for chart type
def get_chart_type():
    print("\nChart Types\n------------------")
    print("1. Bar")
    print("2. Line")
    try:
        choice = int(input("\nEnter the chart type you want (1,2): "))
        if choice < 1 or choice > 2:
            print("Please only select (1 or 2)")
            return get_chart_type()
        return choice
    except ValueError:
        print("Please enter the valid number")
        return get_chart_type()


def chart_type_selection():
    chart_type_choice = get_chart_type()
    if chart_type_choice == 1:
        return "this is bar type"
    elif chart_type_choice == 2:
        return "this is line type"


# prompt user for time series
def get_time_series():
    print("\nSelect the Time Series of the chart you want to generate\n-------------------------------------------------")
    print("1. Intraday")
    print("2. Daily")
    print("3. Weekly")
    print("4. Monthly")

    try:
        choice = int(input("\nEnter the time series option (1, 2, 3, 4): "))
        if choice < 1 or choice > 4:
            print("Please only select from 1-4")
            return get_time_series()
        return choice
    except ValueError:
        print("Please enter the valid number")
        return get_time_series()


def time_series_selection(symbol):
    choice = get_time_series()

    # pass symbol in and get url from this function

    if choice == 1:
        return f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={API_KEY}"
        # return "TIME_SERIES_INTRADAY"
    elif choice == 2:
        return f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
        # return "TIME_SERIES_DAILY"
    elif choice == 3:
        return f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={symbol}&apikey={API_KEY}"
        # return "TIME_SERIES_Weekly"
    elif choice == 4:
        return f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={symbol}&apikey={API_KEY}"
        # return "TIME_SERIES_Monthly"


# prompt user for start date
def get_start_date():
    start_date = str(input("\nEnter the start date(YYYY-MM-DD): "))
    valid_date = check_date_format(start_date)
    if not valid_date:
        print("Please enter the date in valid format(YYYY-MM-DD)")
        return get_start_date()
    return start_date


# prompt user for end date and check if end date is less than start date
def get_end_date(start_date):
    end_date = str(input("\nEnter the end date(YYYY-MM-DD): "))
    valid_date = check_date_format(end_date)
    if valid_date:
        if end_date < start_date:
            print("End date cannot be less than start date")
            return get_end_date(start_date)
        return end_date
    else:
        print("Please enter the date in valid format(YYYY-MM-DD)")
        return get_end_date(start_date)


# check date format
def check_date_format(date):
    try:
        if len(date) == 10:
            datetime.strptime(date, "%Y-%m-%d")
            return True
        return False
    except ValueError:
        return False


def main():
    while True:
        print("\nStock Data Visualizer\n-----------------------\n")
        symbol = get_symbol()
        chart_type = get_chart_type()
        time_series = time_series_selection(symbol)
        start_date = get_start_date()
        end_date = get_end_date(start_date)

        get_data(time_series, start_date, end_date)

        another = input("\nWould you like to view more stock data? Press 'y' to continue: ")
        if another != "y":
            print("Thank you, goodbye!")
            break


main()
# print(url)
# app.run()
