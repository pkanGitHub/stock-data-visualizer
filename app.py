import requests
import json
import pygal
from userPrompt import *

def get_data(time_series, start_date, end_date):
    url = time_series
    stock_data= requests.get(url).json()

    dates, opens, closes, highs, lows, volumes = [] , [], [], [], [], []
    for key in stock_data.keys():
            if key != "Meta Data":
                for x in stock_data[key]:
                    for z in stock_data[key][x]:
                        if x >= start_date and x <= end_date and (x not in dates):
                            dates.append(x)
                            dates.sort()

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

# create a pygal chart
def graph_data_pygal(stock_name, chart_type, start_date, end_date, dates, opens, closes, highs, lows):
    if(chart_type == 2):
        chart = pygal.Line(x_label_rotation=90)
    else:
        chart = pygal.Bar(x_label_rotation=90)

    chart.title = "Stock Data for " + stock_name + " :   " + start_date + "  to  " + end_date
    chart.x_labels = dates
    chart.add('Open', opens)
    chart.add('Close', closes)
    chart.add('High', highs)
    chart.add('Low', lows)
    chart.render_in_browser()
    
def main():
    while True:
        print("\nStock Data Visualizer\n-----------------------\n")
        symbol = get_symbol()
        chart_type = get_chart_type()
        time_series = time_series_selection(symbol)
        start_date = get_start_date()
        end_date = get_end_date(start_date)

        dates, opens, closes, highs,lows, volumes = get_data(time_series, start_date, end_date)
        graph_data_pygal(symbol, chart_type, start_date, end_date, dates, opens, closes, highs, lows)

        another = input("\nWould you like to view more stock data? Press 'y' to continue: ")
        if another != "y":
            print("Thank you, goodbye!")
            break

main()


