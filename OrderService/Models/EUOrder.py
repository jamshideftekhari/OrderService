from Calculator import Calculator


class EUOrder(object):
    Cal = Calculator()
    Discount = 0
    OrderPrice = 0
    PropList = []

    def __init__(self, timestamp, country, number, price):
        self.TimeStamp = timestamp
        self.Country = country
        self.Number = number
        self.Price = price
        self.TotalPrice = self.Cal.calculteprice(self.Price, self.Number, self.Cal.getEuTaxValue(self.Country).value[2])

    def OrderPrice(self):
        pass

    def GetProperList(self):
        self.PropList.append(str(self.TimeStamp))
        self.PropList.append(self.Country)
        self.PropList.append(str(self.Number))
        self.PropList.append(str(self.Price))
        self.PropList.append(str(self.TotalPrice))

    def GetProperRow(self):
        return f'{self.TimeStamp}, {self.Country}, {self.Number}, {self.Price}, {self.TotalPrice}'

    def __str__(self):
        return f'order date: {self.TimeStamp}, from {self.Country}, Number: {self.Number}, ' \
               f'Price: {self.Price}, Total price: {self.TotalPrice}'
