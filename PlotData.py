import matplotlib
import matplotlib.pyplot as plt
from Models.EUOrderCatalog import EUOrderCataloge
import numpy as np
matplotlib.use('Agg')  # to not render in a window show() can not be used,

class PlotData:
    def __init__(self):
        print("MatPlotLib Version: " + matplotlib.__version__)
        self.OC = EUOrderCataloge()
        self.Orders = self.OC.ReadToOrderListFromCSV()

    def BarGraphExemple(self):
        x = np.array(["A", "B", "C", "D"])
        y = np.array([3, 8, 1, 10])

        bp = plt.figure(1)
        plt.bar(x, y)
        #plt.show()

    def LineGraphExemple(self):
        # reference: https://www.w3schools.com/python/matplotlib_line.asp
        ypoints = np.array([3, 8, 1, 10])

        lg = plt.figure(2)
        plt.plot(ypoints, linestyle='dotted')
        #plt.show()

    def OrderGraph(self):
        for row in self.Orders:
            print(row.GetProperRow())
        DKOrder = self.OC.CalculateOrdersPrice("DK")
        print(str(DKOrder))
        xArray = np.array(["DK", "BE", "DE", "NL", "FR"])
        #yArray = np.array([2000, 3000, 5000, 100000, 35000])
        yArray = np.array([self.OC.CalculateOrdersPrice("DK"), self.OC.CalculateOrdersPrice("BE"), self.OC.CalculateOrdersPrice("DE"), self.OC.CalculateOrdersPrice("NL"), self.OC.CalculateOrdersPrice("FR")])

        og = plt.figure(3)
        plt.bar(xArray, yArray)
        plt.savefig("static/images/ordersBarChart.png")


if __name__ == "__main__":
    pl = PlotData()
    pl.LineGraphExemple()
    pl.BarGraphExemple()
    pl.OrderGraph()
    plt.show()

