from parsing_expression import *
from implementing_custom_exceptions import *
from operators import *
from main import OPERATORS

def check_full_validation_of_expression(expression: str) -> list:
    """
    This function gets the string expression and makes all the required validations,
    according to the functions in the parsing_expression file.
    """
    if not expression.strip(): # Checks if the expression is empty or including only white spaces
        raise ValueError("The expression is empty")
    check_invalid_character(expression)
    check_gibberish_expression(expression)
    tokens = expression_to_list(expression)
    tokens = deal_with_minus(tokens)
    tokens = process_parentheses(tokens)
    tokens = process_tilde(tokens)
    tokens = apply_tilde(tokens)
    validate_operators(tokens)
    return tokens

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
    Converts an infix expression to a postfix expression.
    Handles negative numbers and relies on `check_full_validation_of_expression` for validation.
    """
    tokens = check_full_validation_of_expression(expression)
    stack = []  # Stack for operators
    postfix_expression = []  # List for postfix result
    index = 0
    while index < len(tokens):
        token = tokens[index]
        if token not in OPERATORS.keys() and token not in "()":
            postfix_expression.append(token)
        # Negative number case:
        elif token == '-' and (index == 0 or tokens[index - 1] in OPERATORS.keys() or tokens[index - 1] == '('):
            if index + 1 < len(tokens) and tokens[index + 1].replace('.', '', 1).isdigit():
                postfix_expression.append('-' + tokens[index + 1])  # Combine the negative sign with the number
                index += 1
            else:
                raise ValueError("Invalid use of '-' operator.")
        # Opening parenthesis:
        elif token == '(':
            stack.append(token)
        # Closing parenthesis:
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix_expression.append(stack.pop())
            stack.pop()  # Remove the opening parenthesis
        # Operator:
        else:
            while (stack and stack[-1] != '(' and
                   OPERATORS.get(token).priority() <= OPERATORS.get(stack[-1]).priority()):
                postfix_expression.append(stack.pop())
            stack.append(token)
        index += 1
    # Pop any remaining operators in the stack
    while stack:
        postfix_expression.append(stack.pop())
    return ' '.join(postfix_expression)

def postfix_calculation(expression: str):
    """
    This function gets a postfix expression as a string and returns the result.
    """
    # Parse the expression into a list of tokens:
    tokens = expression.split()
    stack = []  # Stack to hold all the operands.
    for token in tokens:
        if token not in OPERATORS.keys():  # If the token is an operand, push it to the stack.
            if '.' in token:
                stack.append(float(token))
            else:
                stack.append(int(token))
        else:  # If the token is an operator, calculate the expression and push it back to the stack.
            operator = OPERATORS.get(token)
            position = operator.position()
            if position == "middle":
                value1 = stack.pop()
                value2 = stack.pop()
                stack.append(operator.operate(value2, value1))
            elif position == "left":
                value = stack.pop()
                stack.append(operator.operate(value))
            elif position == "right":
                value = stack.pop()
                stack.append(operator.operate(value))
    return stack.pop()











