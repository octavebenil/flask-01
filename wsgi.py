from flask import Flask
from flask import json, abort
app = Flask(__name__)

PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'Monde.fr' }
}

@app.route('/')
def hello():
    return "Hello Octave!" 

@app.route("/api/v1/products", methods=["GET"])
def products():
    return json.jsonify(PRODUCTS)

@app.route("/api/v1/products/<int:id>", methods=["GET"])
def product(id):
    if id in PRODUCTS.keys():
        return json.jsonify(PRODUCTS[id]), 200
    else:
        abort(404)