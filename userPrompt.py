from flask import Flask
from datetime import datetime

app = Flask(__name__)
app.config.from_pyfile('config.py')

API_KEY = app.config.get("API_KEY")

# prompt user for symbol
def get_symbol():
    symbol = input("Please enter a stock symbol: ").upper()
    return symbol

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
        return f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=60min&outputsize=full&apikey={API_KEY}"
    elif choice == 2:
        return f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={API_KEY}"
    elif choice == 3:
        return f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={symbol}&apikey={API_KEY}"
    elif choice == 4:
        return f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={symbol}&apikey={API_KEY}"


# prompt user for start date
def get_start_date():
    start_date = str(input("Enter the start date(YYYY-MM-DD): "))
    valid_date = check_date_format(start_date)
    if not valid_date:
        print("Please enter the date in valid format(YYYY-MM-DD)")
        return get_start_date()
    elif valid_date:
        currentDate = datetime.today().strftime("%Y-%m-%d")
        if start_date >= currentDate:
            print("start date cannot be from current date or later")
            return get_start_date()
        return start_date

# prompt user for end date and check if end date is less than start date
def get_end_date(start_date):
    end_date = str(input("Enter the end date(YYYY-MM-DD): "))
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
