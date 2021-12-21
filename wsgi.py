from flask import Flask
from flask import json
app = Flask(__name__)

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
}

@app.route('/')
def hello():
    return "Hello Octave!" 

@app.route("/api/v1/products", methods=["GET"])
def products():
    return json.jsonify(PRODUCTS)    