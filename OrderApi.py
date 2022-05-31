import json

from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from Models.EUOrder import EUOrder
from Persistance.OrderMemoryDB import OrderDB

app = Flask(__name__)

orders = [{"id": 1, "timeStamp": datetime.now(), "unitPrice": 44, "number": 22},
          {"id": 2, "timeStamp": datetime.now()+timedelta(days=-1, hours=-5), "unitPrice": 44, "number": 22},
          {"id": 3, "timeStamp": datetime.now()+timedelta(days=-2, hours=-3), "unitPrice": 44, "number": 22}]

orderdb = OrderDB()
orderdb.CreateOrderTable()
orderdb.InsertTestOrder()


def find_next_id():
    return max(order["id"] for order in orders)+1



@app.get("/Orders")
def get_orders():
    return jsonify(orders)


@app.get("/EUOrders")
def get_EUOrders():
    orderlist = orderdb.GetTableData()
    objectJasonList = []
    for order in orderlist:
        orderObject = EUOrder(order[0], order[1], order[2], order[3])
        objectJasonList.append(orderObject.__dict__)
    #return jsonify(objectJasonList)
    return json.dumps(objectJasonList)


@app.post("/Orders")
def add_orders():
    if request.is_json:
        newOrder = request.get_json()
        newOrder["id"] = find_next_id()
        orders.append(newOrder)
        return newOrder, 201
    return {"error": "request must be jason"}, 415


@app.post("/EUOrders")
def add_EUOrders():
    if request.is_json:
        newOrder = request.get_json()
        # add order to the memory database
        order = EUOrder(newOrder["TimeStamp"], newOrder["Country"], newOrder["Number"], newOrder["Price"])
        print(order)
        orderdb.InsertOrder(order)
        return newOrder, 201
    return {"error": "request must be jason"}, 415


if __name__ == '__main__':
    app.run()