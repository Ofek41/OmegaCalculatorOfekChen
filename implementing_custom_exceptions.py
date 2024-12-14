from custom_exceptions import *
from operators_config import OPERATORS

# List that defines all the valid characters of the expression (without the operators):
VALID_CHARACTERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '(', ')', '.']
def check_invalid_character(expression: str):
    """
    Checks if the expression contains invalid characters.
    If so, raises a single exception with all invalid character positions.
    """
    invalid_positions = [
        index + 1 for index, char in enumerate(expression)
        if char not in VALID_CHARACTERS and char not in OPERATORS.keys()
    ]
    if invalid_positions:
        raise InvalidCharacterInExpressionError(f"Invalid characters at positions: {invalid_positions}")

def check_gibberish_expression(expression: str):
    """
    This function checks if the expression is gibberish. If so, it raises the custom exception.
    """
    if all(char not in VALID_CHARACTERS and char not in OPERATORS.keys() for char in expression):
        raise GibberishExpressionError("The expression you inserted is gibberish!")