import sys
sys.path.append('../')
import datetime
from Models.Order import Order
from pathlib import Path
import csv
from Models.EUOrder import EUOrder


class Repository(object):
    RowsList = []
    myOrders = Order()
    WorkingPath = Path.cwd()
    #staticPath = Path(r"C:\Users\Jamshid Eftekhari\PycharmProjects\OrderService\static\OrderFile.txt")
    staticPath = WorkingPath/"static/OrderFile.txt"
    #staticCsvPath = Path(r"C:\Users\Jamshid Eftekhari\PycharmProjects\OrderService\static\OrderFile.csv")
    staticCsvPath = WorkingPath/"static/OrderFile.csv"
    print(staticCsvPath)

    def __init__(self):
        pass

    # can be made by parameter

    def GenerateTestOrder(self):
        for i in range(5):
            self.myOrders.addOrder(datetime.datetime.now() + datetime.timedelta(hours=i * 1), 100, 5, "UV")
        return self.myOrders.orders

    def ReadOrderText(self):
        # open file in write Mode
        # write
        # close file
        print(f" file path for reading is: {self.staticPath}")
        # a = append w = write
        with self.staticPath.open(mode='r', encoding='utf-8') as orders:
            txt = orders.read()
            print(txt)

    def WriteOrderText(self, order):
        # open file in write Mode
        # write
        # close file
        homePath = Path.home()
        print(homePath)
        #staticPath = Path(r"C:\Users\Jamshid Eftekhari\PycharmProjects\flaskProject\static\OrderFile.txt")
        print(f" file path for writing is: {self.staticPath}")
        # a = append w = write
        with self.staticPath.open(mode='a', encoding='utf-8') as orders:
            orders.write(order)
            orders.write('\n')  # new line

    def ReadOrderCSV(self):
        #open file in read mode, read close
        with self.staticCsvPath.open(mode="r", encoding="utf-8") as ordercsv:
            reader = csv.reader(ordercsv)
            for row in reader:
                print(row)

    def WriteOrderCSV(self, orders):
        # open file in write mode
        # write
        # close file
        print(f"file path for writing to CSV: {self.staticCsvPath}")
        print("***read order CSV****")
        # open the file in write mode
        with self.staticCsvPath.open(mode='w', encoding='utf-8', newline="") as ordercsv:
            writer = csv.writer(ordercsv)
            rownr = 0
            for row in orders:
                print(row.GetProperRow())
                writer.writerow([row.TimeStamp, row.Country, row.Number, row.Price, row.TotalPrice, row.Discount, row.DiscountPrice])
                rownr += 1
                print(f'Row {rownr} added')

    def ReadOrderListFromCSV(self, orders):
        print("***read order CSV****")
        print(f"file path for writing to CSV: {self.staticCsvPath}")
        with self.staticCsvPath.open(mode="r", encoding="utf-8") as ordercsv:
            reader = csv.reader(ordercsv)
            for row in reader:
                csvorder = EUOrder(row[0], row[1], int(row[2]), float(row[3]))
                orders.append(csvorder)

"""
if __name__ == '__main__':
    re = Repository()
    re.Connect2DB()
    print("************state values***********")
    re.GetTableElements("taxtable")
    print("**************discount table**************")
    re.GetTableElements("discounttable")
    re.InsertDiscount(3000, 5)
    print("**************discount table one row added**************")
    re.GetTableElements("discounttable")
"""