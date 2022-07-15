from flask import Flask, jsonify
from datetime import datetime
from numpy import choose
import requests
import json
import pygal



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
    stock_data= requests.get(url).json()
    #print(json.dumps(stock_data, indent=2)) 
    #json_string = json.dumps(stock_data, indent=2)
    #with open('json_data.json', 'w') as outfile:
    #    outfile.write(json_string)

    dates, opens, closes, highs, lows, volumes = [] , [], [], [], [], []
    for key in stock_data.keys():
            if key != "Meta Data":
                for x in stock_data[key]:
                    for z in stock_data[key][x]:
                        if x >= start_date and x <= end_date and (x not in dates):
                            dates.append(x)
                            for y in stock_data[key][x]:
                                if y == "1. open":
                                    opens.append(float(stock_data[key][x][y]))
                                elif y == "4. close":
                                    closes.append(float(stock_data[key][x][y]))
                                elif y == "2. high":
                                    highs.append(float(stock_data[key][x][y]))
                                elif y == "3. low":
                                    lows.append(float(stock_data[key][x][y]))
                                elif y == "5. volume":
                                    volumes.append(float(stock_data[key][x][y]))
    return dates, opens, closes, highs, lows, volumes

def graph_data_pygal(stock_name, chart_type, start_date, end_date, dates, opens, closes, highs, lows):
    # create a pygal chart

    if(chart_type == 2):
        chart = pygal.Line(x_label_rotation=90)
    else:
        chart = pygal.Bar(x_label_rotation=90)

    chart.title = stock_name + " Chart:   " + start_date + "  -  " + end_date
    chart.x_labels = dates
    chart.add('Open', opens)
    chart.add('Close', closes)
    chart.add('High', highs)
    chart.add('Low', lows)
    chart.render_in_browser()
    
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
    #choice = 2

    # pass symbol in and get url from this function

    if choice == 1:
        return f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=15min&outputsize=full&apikey={API_KEY}"
        # return "TIME_SERIES_INTRADAY"
    elif choice == 2:
        #return f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={API_KEY}"
        return f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={API_KEY}"
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
    #end_date = "2020-08-31"
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
        #symbol = "IBM"
        chart_type = get_chart_type()
        #chart_type = 1
        time_series = time_series_selection(symbol)
        start_date = get_start_date()
        #start_date = "2020-08-01"
        end_date = get_end_date(start_date)

        dates, opens, closes, highs,lows, volumes = get_data(time_series, start_date, end_date)
        graph_data_pygal(symbol, chart_type, start_date, end_date, dates, opens, closes, highs, lows)
        #graph_data_pygal(symbol, time_series, start_date, end_date, dates,prices)
        #p1 = chart.ChartMaker(opens, closes, highs, lows, symbol, dates, end_date, start_date)
        #p1.render_chart()
        

        another = input("\nWould you like to view more stock data? Press 'y' to continue: ")
        if another != "y":
            print("Thank you, goodbye!")
            break


main()
# print(url)
# app.run()


