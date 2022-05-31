from enum import Enum


class EUTax(Enum):
    NOTFound = ("Not Found", "Not Found", 0)
    DK = ("DK", "Denmark", 25)
    BE = ("BE", "Belgium", 21)
    DE = ("DE", "Germany", 19)
    NL = ("NL", "Netherlands", 21)
    FR = ("FR", "France", 20)


