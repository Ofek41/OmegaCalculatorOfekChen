from parsing_expression import *
from implementing_custom_exceptions import *
from operators import *

def check_full_validation_of_expression(expression: str) -> list:
    """
    This function gets the string expression and makes all the required validations,
    according to the functions in the parsing_expression file.
    """
    try:
        # Validate invalid characters or gibberish:
        check_invalid_character(expression)
        check_gibberish_expression(expression)
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
    except Exception as exc:
        raise ValueError(f"Validation error in the expression: {exc}")

def list_to_expression(tokens)->str:
    """
    This function gets the tokens list and make it back to expression string.
    """
    expression_string = ""
    for token in tokens:
        expression_string+=token
    return expression_string

def infix_to_postfix(expression: str):
    """
    This function gets a string expression in infix form and returns its postfix form.
    It also deals with float numbers and multi digits numbers.
    """
    tokens = expression_to_list(expression)
    stack = []  # Stack that holds all the operators
    postfix_expression = []  # List for the postfix expression
    for token in tokens:
        if token not in OPERATORS.keys() and token not in "()":
            postfix_expression.append(token)
        elif token == '(':  # Opening parenthesis
            stack.append(token)
        elif token == ')':  # Closing parenthesis
            while stack and stack[-1] != '(':
                postfix_expression.append(stack.pop())
            stack.pop()  # Remove the opening parenthesis
        else:
            while (stack and stack[-1] != '(' and
                   OPERATORS.get(token).priority() <= OPERATORS.get(stack[-1]).priority()):
                postfix_expression.append(stack.pop())
            stack.append(token)
    while stack:  # Pop any remaining operators
        postfix_expression.append(stack.pop())
    return ' '.join(postfix_expression)  # Return the postfix expression as a string.







