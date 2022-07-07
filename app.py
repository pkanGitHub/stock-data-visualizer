from flask import Flask, jsonify
import requests

app = Flask(__name__)
app.config.from_pyfile('config.py')

API_KEY = app.config.get("API_KEY")

@app.route('/', methods=['GET'])
def home():
    #example data for TIME_SERIES_DAILY
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={API_KEY}'
    res = requests.get(url)
    data = res.json()
    return jsonify(data)

app.run()