from flask import Flask, render_template, request, redirect, url_for, jsonify
from Persistance.Repository import Repository
from Models.EUOrderCatalog import EUOrderCataloge
from Models.EUOrder import EUOrder
from datetime import datetime
from PlotData import PlotData
import requests
import json

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return '<h1 text>Order system!</h1>' \
           '<a href="http://127.0.0.1:5000/EUOrders"> Link To Order Page </a> <br>' \
           '<a href="http://127.0.0.1:5000/WeatherData"> Link To weather data </a> <br>' \
           '<a href="http://127.0.0.1:5000/EUOrdersJason"> Link To weather data </a> <br>'


@app.route('/EUOrders')
def EUOrders():
    catalog = EUOrderCataloge()
    PlotOrders = PlotData()
    PlotOrders.OrderGraph()
    return render_template("EUOrder.html", orders=catalog.ReadToOrderListFromCSV())


@app.route('/AddOrder', methods=['POST'])
def AddOrder():
    order = EUOrder(datetime.now(), request.form['country'], int(request.form['number']), float(request.form['price']))
    catalog = EUOrderCataloge()
    catalog.ReadToOrderListFromCSV()
    catalog.AddOrder(order)
    catalog.SaveToCsv()
    # return render_template("EUOrder.html", orders=catalog.ReadToOrderListFromCSV())
    return redirect(url_for('EUOrders'))


@app.route('/RemoveOrder', methods=['POST'])
def RemoveOrder():
    index = int(request.form['index'])
    catalog = EUOrderCataloge()
    catalog.ReadToOrderListFromCSV()
    catalog.RemoveOrder(index)
    catalog.SaveToCsv()
    return redirect(url_for('EUOrders'))


@app.route('/EUOrdersJason')
def EuOrdersJason():
    catalog = EUOrderCataloge()
    orderList = catalog.ReadToOrderListFromCSV()
    objectJasonList = []
    for order in orderList:
        objectJasonList.append(order.__dict__)
    return jsonify(objectJasonList)


@app.route('/WeatherData')
def WeatherData():
    response = requests.get('https://envs2.au.dk/luftdata/API/api/Meteorology/copenhagen/2022-05-26/2022-05-27')
    return jsonify(response.json())
        #"'f<h1 text>Response code: {str(response.status_code)}</h1><br>' \
        #   '{response}'


if __name__ == '__main__':
    app.run()