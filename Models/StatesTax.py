from enum import Enum


class StatesTax(Enum):
    NOTFound = ("Not Found", "Not Found", 0)
    UT = ("UT", "Utah", 6.85)
    NV = ("NV", "New York", 8)
    TX = ("TX", "Texas", 6.25)
    AL = ("AL", "Alabama", 4)
    CA = ("CA", "California", 8.25)
