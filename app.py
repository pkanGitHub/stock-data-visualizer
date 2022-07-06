import flask
import requests

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])

def home():
    apikey = ""
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={apikey}'
    res = requests.get(url)
    data = res.json()
    # print(data)
    return (f"This is the stock visualizer\n{data}")

app.run()