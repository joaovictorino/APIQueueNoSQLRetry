from flask import request, jsonify
from basket.infra.queueWrapper import QueueWrapper
from basket.infra.dao import Dao
from random import randint
import json
import common
app = common.app

@app.route("/order/finish", methods=["POST"])
def finishOrder():
    order = request.get_json()
    orderNumber = generateOrderNumber()
    order["number"] = orderNumber
    queueWrapper = QueueWrapper(common.getAddressQueue())
    queueWrapper.publish("order_finished", json.dumps(order))
    return { "orderNumber": orderNumber }, 200

@app.route("/order/<orderNumber>", methods=["GET"])
def findOrder(orderNumber):
    dao = Dao(common.getAddressDB())
    order = dao.findByNumber(orderNumber)
    return jsonify(order)

def generateOrderNumber():
    return randint(100000, 999999)
