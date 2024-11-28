# Importing my modules:
from operands_class import *
from exceptions import *
# Global dictionary that holds all the operands:
OPERANDS = {"+": Add(),
             "-": Sub(),
             "*": Multiply(),
             "/": Division(),
             "^": Power(),
             "@": Average(),
             "$": Maximum(),
             "&": Minimum(),
            "%": Modulo(),
            "~":Negative(),
            "!": Factorial()}