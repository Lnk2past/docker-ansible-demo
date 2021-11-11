from flask import Flask

app = Flask(__name__)

@app.route("/v1")
def v1_hello_world_v1():
    return "<p>Hello, World!</p>"

@app.route("/")
@app.route("/v2")
def hello_world():
    return "<h1>NEW AND IMPROVED</h1><p>Hello, World!</p>"