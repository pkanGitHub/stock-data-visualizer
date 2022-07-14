from flask import Flask, jsonify
import requests
import json
from userPrompt import *
import pandas as pd

app = Flask(__name__)
app.config.from_pyfile('config.py')
API_KEY = app.config.get("API_KEY")

# @app.route('/', methods=['GET'])

def get_url(symbol, timeSeries, API_KEY):
    return f"https://www.alphavantage.co/query?function={timeSeries}&symbol={symbol}&apikey={API_KEY}"

def get_data(url):
    res = requests.get(url)
    data = res.json()

    #print(json.dumps(data, indent=2))
    #print(data.keys())
    for key in data.keys():
        if key != "Meta Data":
            print(key,'\n',"-----------\n")
            for x in data[key]:
                for z in data[key][x]:
                    #print(x)
                    #print(z)
                    #print(data[key][x][z])
                    print(x, ":  ", z, " = ",data[key][x][z], sep="")
                    if(z == "5. volume"):
                        print("-----------")
    return data

def main():
    #symbol = get_symbol()
    #chart = chart_type_selection()
    #timeSeries = time_series_selection()
    #startDate = get_start_date()
    #endDate = get_end_date(startDate)

    #Test Varaibles
    symbol = "IBM"
    chart = 1
    timeSeries = "TIME_SERIES_DAILY"
    startDate = "2020-08-01"
    endDate = "2020-08-30"

    url = get_url(symbol, timeSeries, API_KEY)
    data = get_data(url)
    #print(data)
    #print(url)

main()

# app.run()

