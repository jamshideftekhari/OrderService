import sys
sys.path.append('../')
from Persistance.Repository import Repository


class EUOrderCataloge(object):

    def __init__(self):
        self.OrderCatalog = []
        self.Repo = Repository()

    def AddOrder(self, neworder):
        self.OrderCatalog.append(neworder)

    def RemoveOrder(self, index):
        self.OrderCatalog.pop(index)

    def SavetoTxtFile(self, neworder):
        self.Repo.WriteOrderText(neworder)

    def ReadFromTxtFile(self):
        self.Repo.ReadOrderText()

    def SaveToCsv(self):
        self.Repo.WriteOrderCSV(self.OrderCatalog)

    def ReadFromCsv(self):
        self.Repo.ReadOrderCSV()

    def ReadToOrderListFromCSV(self):
        self.Repo.ReadOrderListFromCSV(self.OrderCatalog)
        return self.OrderCatalog

    def CalculateOrdersPrice(self, countryCode):
        price = 0
        for row in self.OrderCatalog:
            if row.Country == countryCode:
                price = price + row.TotalPrice
        return price

    def __str__(self):
        for item in self.OrderCatalog:
            print(item)
        return "end of list"



