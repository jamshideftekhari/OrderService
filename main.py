from Models.EUOrderCatalog import EUOrderCataloge
from Models.EUOrder import EUOrder
from datetime import datetime


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # explain following 3 lines, explain ordercatalogs properties and behaviors
    orderCatalog = EUOrderCataloge()
    order = EUOrder(datetime.now(), "DK", 4, 100)
    print(order)

    # explain following 6 lines 5 lines of the code,
    # comment the code out and run. Do the program as expected? Proposal for improvement?
    orderCatalog.AddOrder(order)
    print(orderCatalog)
    order = EUOrder(datetime.now(), "DK", 10, 100)
    orderCatalog.AddOrder(order)
    order = EUOrder(datetime.now(), "DK", 20, 150)
    orderCatalog.AddOrder(order)
    print(orderCatalog)
    # explain following 5 lines of the code,
    # comment the code out and run. Do the program as expected? Proposal for improvement?
    # the program will fail explain the error and try to fix it
    print("**************order Catalog list (memory)")
    print(orderCatalog)
    # save order catalog to text file
    orderCatalog.SavetoTxtFile(order.__str__())
    print("**********read from text file***************")
    orderCatalog.ReadFromTxtFile()

    # explain following 3 lines of the code,
    # comment the code out and run. Do the program as expected? Proposal for improvement?
    # the program will fail explain the error and try to fix it
    print("**********write to csv***************")
    orderCatalog.SaveToCsv()
    print("**********read from CSV************")
    orderCatalog.ReadFromCsv()



# generate pdf
#  pdfRapport = PdfService("OrderRapport")
#  pdfRapport.AddTitle("order rapport")
# pdfRapport.savePdf()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
