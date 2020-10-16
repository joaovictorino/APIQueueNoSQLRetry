from flask import Flask, request, jsonify

app = Flask(__name__)

import random
import json

list = {
    1: 5,
    2: 500,
    3: 100,
    4: 20,
    5: 50    
}

@app.errorhandler(ValueError)
def handleExceptions(error):
    response = jsonify(str(error))
    response.status_code = 400
    return response
    

@app.route("/product", methods=['POST'])
def decrementProduct():
    if random.choice([True, False]):
        try:
            product = json.loads(request.get_json())
            if int(list[product["id"]]) >= int(product["quantity"]):
                list[product["id"]] -= product["quantity"]
                return 'OK', 200
            else:
                raise ValueError("Product out of stock, qtd {0}".format(list[product["id"]]))
        except KeyError:
            raise ValueError("Product doesn't exists")
    else:
        raise Exception("Error")

@app.route("/products", methods=['GET'])
def listProducts():
    return jsonify(list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)