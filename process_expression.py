from parsing_expression import *
from implementing_custom_exceptions import *
from operators import *

def check_full_validation_of_expression(expression: str) -> list:
    """
    This function gets the string expression and makes all the required validations,
    according to the function in the parsing_expression file.
    """
    print("Validating expression:", expression)
    try:
        # Convert the expression into a list of tokens:
        tokens = expression_to_list(expression)
        # Check all the minus signs:
        tokens = deal_with_minus(tokens)
        # Validate and process parentheses:
        tokens = process_parentheses(tokens)
        # Validate the usage of tilde:
        tokens = process_tilde(tokens)
        # Apply the effects of tilde into the list:
        tokens = apply_tilde(tokens)
        # Validate operators and operands:
        validate_operators(tokens)
        return tokens
    except Exception as e:
        raise ValueError(f"Validation error in the expression: {e}")

def list_to_expression(tokens)->str:
    """
    This function gets the tokens list and make it back to expression string.
    """
    expression_string = ""
    for token in tokens:
        expression_string+=token
    return expression_string
