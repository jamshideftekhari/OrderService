from Models.StatesTax import StatesTax
import datetime


class Order(object):
    order = {}
    orders = []

    def __init__(self):
        print("add, edit and remove orders")
        self.order = {"orderDate": None, "orderItemPrice": None, "orderNumber": None, "State": None}
        self.orders.append(self.order)

    def addOrder(self, date, price, number, state):
        print("adding one order to the list")
        self.order = {"orderDate": date, "orderItemPrice": price, "orderNumber": number, "State": state}
        self.orders.append(self.order)

    def getOrders(self):
        return self.orders

    def __str__(self):
        return str(self.order)


class OrderObject:
    def __init__(self, date, price, number, place):
        self.Date = date
        self.Price = price
        self.number = number
        self.place = place

    def __str__(self):
        return f"{self.Date}"


if __name__ == '__main__':
    myOrders = Order()
    # st = StatesTax
    for s in StatesTax:
        print(s.value)
    # i = 0
    # myOrders.addOrder(datetime.datetime.now() + datetime.timedelta(hours=i * 1), 100*i, 5*i, st.value[0])
    # i = i + 1

    print(myOrders)
    for i in range(5):
        myOrders.addOrder(datetime.datetime.now() + datetime.timedelta(hours=i * 1), 100, 5, "UV")
    print(myOrders)
    print("list content:")
    for x in myOrders.orders:
        print(x)
