import sys
sys.path.append('../')
from Persistance.Repository import Repository
from Persistance.PdfService import PdfService
from EUOrder import EUOrder
from datetime import datetime


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

    def __str__(self):
        for item in self.OrderCatalog:
            print(item)
        return "end of list"


if __name__ == '__main__':
    # explain following 3 lines, explain ordercatalogs properties and behaviors
      orderCatalog = EUOrderCataloge()
    # order = EUOrder(datetime.now(), "DK", 4, 100)
    # print(order)

    # explain following 6 lines 5 lines of the code,
    # comment the code out and run. Do the program as expected? Proposal for improvement?
    # orderCatalog.AddOrder(order)
    # print(orderCatalog)
    # order = EUOrder(datetime.now(), "DK", 10, 100)
    # orderCatalog.AddOrder(order)
    # order = EUOrder(datetime.now(), "DK", 20, 150)
    # orderCatalog.AddOrder(order)

    #explain following 5 lines of the code,
    # comment the code out and run. Do the program as expected? Proposal for improvement?
    #the program will fail explain the error and try to fix it
    # print("**************order Catalog list (memory)")
    # print(orderCatalog)
    # #save order catalog to text file
    # orderCatalog.SavetoTxtFile(order.__str__())
    # print("**********read from text file***************")
    # orderCatalog.ReadFromTxtFile()

    # explain following 3 lines of the code,
    # comment the code out and run. Do the program as expected? Proposal for improvement?
    # the program will fail explain the error and try to fix it
    # print("**********write to csv***************")
    # orderCatalog.SaveToCsv()
    # print("**********read from CSV************")
    # orderCatalog.ReadFromCsv()

    # generate pdf
    # pdfRapport = PdfService("OrderRapport")
    # pdfRapport.AddTitle("order rapport")
    # pdfRapport.savePdf()
