from custom_exceptions import *
from operators_config import OPERATORS

# List that defines all the valid characters of the expression (without the operators):
VALID_CHARACTERS = "0123456789()."
def check_invalid_character(expression: str):
    """
    Checks if the expression contains invalid characters.
    If so, raises a single exception with all invalid character positions and the chars themselves.
    """
    invalid_positions = []
    for index, char in enumerate(expression):
        if char not in VALID_CHARACTERS and char not in OPERATORS.keys():
            invalid_positions.append((char, index+1))
    if invalid_positions:
        # A message for any invalid character in expression:
        message_parts = [f"'{char}' in position {position}" for char, position in invalid_positions]
        # Combine all the messages together:
        error_message = "Invalid characters in expression: " + ", \n".join(message_parts)
        # Raise the exception if needed, if the all the chars are invalid, raise the gibberish exception:
        if len(invalid_positions) == len(expression):
            raise GibberishExpressionError("The expression you inserted is gibberish!")
        else:
            raise InvalidCharacterInExpressionError(error_message)

def check_valid_decimal(expression: list):
    """
    Validates that all numbers in the expression are valid decimals with only one decimal point.
    """
    for token in expression:
        if isinstance(token, str) and token.count('.') > 1:
            raise InvalidDecimalNumber(f"Invalid decimal number: {token}")