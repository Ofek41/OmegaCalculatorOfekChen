from operators import *
from operators.hashtag_operator import Hashtag

# Global dict that holds all the operators and an instance of their class.
OPERATORS = {
    "+": Add(),
    "-": Sub(),
    "*": Multiply(),
    "/": Division(),
    "^": Power(),
    "@": Average(),
    "$": Maximum(),
    "&": Minimum(),
    "%": Modulo(),
    "~": Negative(),
    "!": Factorial(),
    "#": Hashtag()
}
