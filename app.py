from flask import Flask, jsonify
import requests
from userPrompt import *



symbol = get_symbol()
chart = chart_type_selection()
timeSeries = time_series_selection()
startDate = get_start_date()
endDate = get_end_date(startDate)

# @app.route('/', methods=['GET'])

def get_url(symbol, timeSeries, API_KEY):
    return f"https://www.alphavantage.co/query?function={timeSeries}&symbol={symbol}&apikey={API_KEY}"

def get_data(url):
    res = requests.get(get_url(url))
    data = res.json()
    return data


url = get_url(symbol, timeSeries, API_KEY)
print(url)
# app.run()
