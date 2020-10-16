import pymongo
import json

class Dao:

    def __init__(self, address): 
        client = pymongo.MongoClient(address)
        self.db = client.order

    def save(self, order):
        self.db.order.insert_one(order)

    def findByNumber(self, orderNumber):
        order = self.db.order.find_one({ 'number' : int(orderNumber) })
        return { "number": order["number"], "status" : order["status"] }