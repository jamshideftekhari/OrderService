import sqlite3
from datetime import datetime, timedelta
from Models.EUOrder import EUOrder


class OrderDB:
    def __init__(self):
        self.Connection = sqlite3.connect(":memory:", check_same_thread=False)
        self.Cursor = self.Connection.cursor()

    def CreateOrderTable(self):
        self.Cursor.execute("CREATE TABLE IF NOT EXISTS OrderTable(OrderTimeStamp DATETIME, Country TEXT, OrderNumber INT, UnitPrice DOUBLE)")

    def InsertOrder(self, order):
        self.Cursor.execute("INSERT INTO OrderTable VALUES (?, ?, ?, ?)", (order.TimeStamp, order.Country, order.Number, order.Price))

    def InsertTestOrder(self):
        testOrder = EUOrder(datetime.now(), 'DK', 25, 100)
        self.InsertOrder(testOrder)
        for i in range(6):
            testOrder = EUOrder(datetime.now() - timedelta(days=i * 1), 'DK', 25*i, 100+i)
            self.InsertOrder(testOrder)
        #self.Cursor.execute("INSERT INTO OrderTable VALUES ('30-05-2022','DK','25','100')")

    def GetTableData(self):
        return self.Cursor.execute("SELECT * FROM OrderTable")

    def GetOrderByDate(self, start, stop):
        if not stop:
            stop = datetime.now()
        return self.Cursor.execute("SELECT * FROM OrderTable WHERE OrderTimeStamp > ? AND OrderTimeStamp < ? ", (start, stop))