from flask import Flask, jsonify
from usurl import usurl
from urls import urls
import pandas as pd
import requests
import json
from pprint import pprint

app = Flask(__name__)

data = []

for x in urls:
    response = requests.get(x)
    data.append(response.json())

us_response = requests.get(usurl)
us_data = us_response.json()

@app.route("/")
def home():
    return jsonify(data)

@app.route("/total")
def total():
    return jsonify(us_data)

if __name__ == "__main__":
    app.run(debug=True)
