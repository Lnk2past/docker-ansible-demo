from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/v1")
def hello_world():
    return "<p>Hello, World!</p>"