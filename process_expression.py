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
        # Validate invalid characters or gibberish:
        check_invalid_character(expression)
        check_gibberish_expression(expression)
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

def infix_to_postfix(expression:str):
    """
    This function gets a string expression in infix form and returns its postfix form.
    """
    stack = [] # Stack that holds all the operators
    postfix_expression = ""
    for index in range(len(expression)):
        char = expression[index]
        # If the char is an operand:
        if char not in OPERATORS.keys() and char not in "()":
            postfix_expression+=char
        elif char=='(': stack.append('(') # If the char is a parenthesis
        elif char==')':
            while stack[-1]!='(':
                postfix_expression+=stack.pop()
            stack.pop()
        else: # If the char is an operator:
            temp = OPERATORS.get(stack[-1]) # Get the operator on the top of the stack
            while stack and OPERATORS.get(char).priority() <= temp.priority():
                postfix_expression+=stack.pop()
            stack.append(char)
    while stack:
        postfix_expression+=stack.pop()
    return postfix_expression





