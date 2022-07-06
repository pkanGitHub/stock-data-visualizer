import flask
app = flask.Flask(__name__)

@app.route('/', methods=['GET'])

def home():
    return "This is the stock visualizer"
app.run()