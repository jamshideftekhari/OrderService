import sqlite3


class orderDB:
    def __init__(self):
        self.Connection = sqlite3.connect("OrderDB.db")
        self.Cursor = self.Connection.cursor()

    def CreateTable(self):
        self.Cursor.execute("CREATE TABLE IF NOT EXISTS EUTax(Name TEXT, Country TEXT, Value INT)")

    def CreateOrderTable(self):
        self.Cursor.execute("CREATE TABLE IF NOT EXISTS Order(TimeStamp DATETIME, Country TEXT, Number INT, Price DOUBLE)")

    def InsertData(self):
        self.Cursor.execute("INSERT INTO EUTax VALUES ('DK', 'Denmark', 25)")

    def GetTableData(self):
        return self.Cursor.execute("SELECT * FROM EUTax")

    def CloseConnection(self):
        self.Connection.commit()
        self.Connection.close()

    def InsertDataParameter(self, id, country, vat):
        self.Cursor.execute("INSERT INTO EUTax VALUES (?, ?, ?)", (id, country, vat))

    def MigrateData(self):
        pass


if __name__ == '__main__':
    db = orderDB()
    db.CreateTable()
    db.InsertData()
    db.InsertDataParameter("FR", "France", 20)
    for row in db.GetTableData():
        print(row)
    db.CloseConnection()