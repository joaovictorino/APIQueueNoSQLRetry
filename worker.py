from basket.infra.dao import Dao
from basket.infra.queueWrapper import QueueWrapper
from basket.infra.stockService import StockService
import common
import json

queueSystem = QueueWrapper(common.getAddressQueue())

def callback(body):
    dao = Dao(common.getAddressDB())
    order = json.loads(body)
    success = True
    result = ""
    for orderItem in order["order"]:
        service = StockService(common.getAddressStock())
        try:
            result = service.call({ "id" : orderItem["id"], "quantity": orderItem["quantity"] })
        except:
            print(result)
            success = False

    if success:
        order["status"] = "created"
    else:
        order["status"] = "error"

    dao.save(order)

queueSystem.receive("order_finished", callback, False)