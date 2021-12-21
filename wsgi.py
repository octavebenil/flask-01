from flask import Flask
from flask import json, abort, request

#auto incrementation
import itertools

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
def readProduct(id):
    if id in PRODUCTS.keys():
        return json.jsonify(PRODUCTS[id]), 200
    else:
        abort(404)

@app.route("/api/v1/products/<int:id>", methods=["DELETE"])
def deleteProduct(id):
    PRODUCTS.pop(id, None)
    return None, 204 

@app.route("/api/v1/products", methods=["POST"])
def createProduct():
    posted_product = request.get_json()

    START_INDEX = len(PRODUCTS) + 1
    IDENTIFIER_GENERATOR = itertools.count(START_INDEX)

    new_id = next(IDENTIFIER_GENERATOR)
    PRODUCTS[new_id] = {'id': new_id, 'name': posted_product["name"]}

    return json.jsonify(PRODUCTS), 201   

@app.route('/api/v1/products/<int:id>', methods=["PATCH"])
def updateProduct(id):
    if id in PRODUCTS.keys():
        posted_product = request.get_json()

        if not posted_product["name"]:
            abort(422)
        else:
            PRODUCTS[id]["name"] = posted_product["name"]
            return json.jsonify(PRODUCTS[id]), 204 
    else:
        abort(404)          