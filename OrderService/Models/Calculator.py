from StatesTax import StatesTax
from Discount import Discount
from EUTax import EUTax


class Calculator (object):
    st = StatesTax
    dis = Discount
    eu = EUTax

    def __init__(self):
        print ("calculator object initialised ") 
        
    def getStateTaxValue(self, state):
        for s in self.st:
            if s.value[0] == state.upper():
                print("Record found: ")
                print(s.value)
                return s
        print("not found") 
        return s.NOTFound    

    def getEuTaxValue(self, state):
        for s in self.eu:
            if s.value[0] == state.upper():
                print("Record found: ")
                print(s.value)
                return s
        print("not found")
        return s.NOTFound

    def calculteprice(self, price, number, tax):
        return price*number+price*number*(tax/100)

    def getDiscountValue(self, number):
        for d in self.dis:
            if number<d.value[0]:
                print("discount tuple found:")
                print(d.value)
                return d
        print("no discount")
        