from parsing_expression import *
from implementing_custom_exceptions import *
from operators import *
from operators_config import OPERATORS

def check_full_validation_of_expression(expression: str) -> list:
    """
    This function gets the string expression and makes all the required validations,
    according to the functions in the parsing_expression file.
    """
    if not expression.strip():
        raise ValueError("The expression is empty")
    expression = expression.replace(" ", "") # Removing all white spaces
    check_invalid_character(expression)
    check_gibberish_expression(expression)
    tokens = expression_to_list(expression)
    tokens = deal_with_minus(tokens)
    tokens = process_parentheses(tokens)
    tokens = process_tilde(tokens)
    tokens = apply_tilde(tokens)
    validate_operators(tokens)
    return tokens # Return tokens after all validations


def infix_to_postfix(expression: str):
    """
    Converts an infix expression to a postfix expression.
    """
    tokens = check_full_validation_of_expression(expression) # Get the exp after validations
    stack = []
    postfix_expression = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token not in OPERATORS.keys() and token not in "()": # The token is an operand
            postfix_expression.append(token)
            i += 1
            # Handle postfix operators:
            while i < len(tokens) and tokens[i] in OPERATORS.keys() and OPERATORS[tokens[i]].position() == 'left':
                postfix_expression.append(tokens[i])
                i += 1
        elif token == '(':
            stack.append(token)
            i += 1
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix_expression.append(stack.pop())
            if not stack or stack[-1] != '(':
                raise InvalidParenthesesError("Unmatched parentheses")
            stack.pop()
            i += 1
            # Handle postfix operators after parentheses:
            while i < len(tokens) and tokens[i] in OPERATORS.keys() and OPERATORS[tokens[i]].position() == 'left':
                postfix_expression.append(tokens[i])
                i += 1
        else:
            operator = OPERATORS[token]
            position = operator.position()
            if position == 'right':  # Prefix operator
                stack.append(token)
                i += 1
            elif position == 'middle':
                while (stack and stack[-1] != '(' and
                       OPERATORS.get(stack[-1]).priority() >= operator.priority()):
                    postfix_expression.append(stack.pop())
                stack.append(token)
                i += 1
            else:
                raise ValueError(f"Unexpected operator '{token}' in this context")
    while stack:
        if stack[-1] == '(' or stack[-1] == ')':
            raise InvalidParenthesesError("Unmatched parentheses")
        postfix_expression.append(stack.pop())
    return ' '.join(postfix_expression)


def postfix_calculation(expression: str):
    """
    This function gets a postfix expression as a string and returns the result.
    """
    # Parse the expression into a list of tokens:
    tokens = expression.split()
    stack = []
    for token in tokens:
        if token not in OPERATORS.keys():
            if '.' in token:
                stack.append(float(token))
            else:
                stack.append(int(token))
        else:
            operator = OPERATORS.get(token)
            position = operator.position()
            if position == "middle":
                if len(stack)<2:
                    raise UnmatchedOperandsAndOperatorsError("Nou enough operands for the operator!")
                value1 = stack.pop()
                value2 = stack.pop()
                stack.append(operator.operate(value2, value1))
            elif position == "left":  # Postfix operator
                value = stack.pop()
                stack.append(operator.operate(value))
            elif position == "right":  # Prefix operator
                value = stack.pop()
                stack.append(operator.operate(value))
    return stack.pop()
