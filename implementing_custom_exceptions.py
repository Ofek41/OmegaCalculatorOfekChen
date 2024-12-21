from custom_exceptions import *
from operators_config import OPERATORS

# List that defines all the valid characters of the expression (without the operators):
VALID_CHARACTERS = "0123456789()."
def check_invalid_character(expression: str):
    """
    Checks if the expression contains invalid characters.
    If so, raises a single exception with all invalid character positions.
    """
    for index, char in enumerate(expression):
        if char not in VALID_CHARACTERS and char not in OPERATORS.keys():
            raise InvalidCharacterInExpressionError(f"Invalid character {char} in position {index+1}")

def check_gibberish_expression(expression: str):
    """
    This function checks if the expression is gibberish. If so, it raises the custom exception.
    """
    if all(char not in VALID_CHARACTERS and char not in OPERATORS.keys() for char in expression):
        raise GibberishExpressionError("The expression you inserted is gibberish!")

def check_valid_decimal(expression: list):
    """
    Validates that all numbers in the expression are valid decimals with only one decimal point.
    """
    for token in expression:
        if isinstance(token, str) and token.count('.') > 1:
            raise InvalidDecimalNumber(f"Invalid decimal number: {token}")
