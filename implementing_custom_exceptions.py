from custom_exceptions import *
from operators_config import OPERATORS

# List that defines all the valid characters of the expression (without the operators):
VALID_CHARACTERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '(', ')']
def check_invalid_character(expression: str):
    """
    This function checks if the expression contains any invalid characters. If so, it raises the custom
    exception with a matching message and the exact position and char.
    """
    index = 0
    for char in expression:
        if char not in VALID_CHARACTERS and char not in OPERATORS.keys():
            raise InvalidCharacterInExpressionError(f"Invalid character '{char}' in position {index + 1}.")
        index += 1

def check_gibberish_expression(expression: str):
    """
    This function checks if the expression is gibberish. If so, it raises the custom exception.
    """
    if all(char not in VALID_CHARACTERS and char not in OPERATORS.keys() for char in expression):
        raise GibberishExpressionError("The expression you inserted is gibberish!")