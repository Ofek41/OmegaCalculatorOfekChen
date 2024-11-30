# Importing my modules:
from operators import *
# Global dictionary that holds all the operators:
OPERATORS = {"+": Add(),
             "-": Sub(),
             "*": Multiply(),
             "/": Division(),
             "^": Power(),
             "@": Average(),
             "$": Maximum(),
             "&": Minimum(),
            "%": Modulo(),
            "~":Negative(),
            "!": Factorial()
             }