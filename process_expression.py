from parsing_expression import *
from implementing_custom_exceptions import *
from operators import *
from operators_config import find_key_by_value

def check_full_validation_of_expression(expression: str) -> list:
    if not expression.strip():
        raise EmptyExpressionError("The expression is empty.")
    expression = expression.replace(" ", "")  # Remove spaces
    # Validating the characters:
    check_invalid_character(expression)
    check_gibberish_expression(expression)
    tokens = expression_to_list(expression) # Making the string expression a list expression
    check_valid_decimal(tokens) # Checks for invalid decimal numbers
    tokens = minus_parse(tokens)  # Process minus signs
    tokens = process_tilde(tokens)  # Handle tilde
    for index, token in enumerate(tokens): # Converting the operators to their class instance
        if token in OPERATORS:
            tokens[index] = OPERATORS[token]
    validate_left_operators(tokens) # Validating all left operators from the OPERATORS dictionary
    return tokens

def infix_to_postfix(tokens: list):
    """
    This function gets an infix expression and converting it into a postfix one.
    """
    stack = []  # Operator stack
    postfix_expression = []  # Resulting postfix expression
    for token in tokens:
        # Check for operands:
        if isinstance(token, str) and token.replace('.', '', 1).isdigit():
            postfix_expression.append(token)
        # Check for operators:
        elif isinstance(token, Operator):
            while stack and isinstance(stack[-1], Operator) and (stack[-1].priority()>token.priority() or
                stack[-1].priority()==token.priority() and not isinstance(token, (UMinus, SMinus))):
                popped = stack.pop()
                postfix_expression.append(popped)
            if token.position()=="left":
                postfix_expression.append(token)
            else:
                stack.append(token)
        # Check for parentheses:
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                popped = stack.pop()
                postfix_expression.append(popped)
            # Check for unmatched parentheses:
            if not stack or stack[-1] != '(':
                raise InvalidParenthesesError("Unmatched parentheses.")
            stack.pop()  # Remove the '('
    while stack:
        if stack[-1] == '(':
            raise InvalidParenthesesError("Unmatched parentheses.")
        popped = stack.pop()
        postfix_expression.append(popped)
    return postfix_expression


def postfix_calculation(expression: list):
    """
    This function gets the expression with its postfix form and returns the result.
    """
    stack = []
    for token in expression:
        # Check for operands:
        if isinstance(token, str) and token.replace('.', '', 1).isdigit():
            stack.append(float(token) if '.' in token else int(token))
        # Check for operators:
        elif isinstance(token, Operator):
            arity = token.arity()
            if arity == 1:  # Unary operator
                if not stack:
                    key = find_key_by_value(OPERATORS, token)
                    raise UnmatchedOperandsAndOperatorsError(f"Operator '{key}' requires one operand.")
                operand = stack.pop()
                result = token.operate(operand)
                stack.append(result)
            elif arity == 2:  # Binary operator
                if len(stack) < 2:
                    key = find_key_by_value(OPERATORS, token)
                    raise UnmatchedOperandsAndOperatorsError(f"Operator '{key}' requires two operands.")
                b = stack.pop()
                a = stack.pop()
                result = token.operate(a, b) # Calculating the result
                stack.append(result)
    if len(stack)>1: # If there is more than one result in the stack
        raise ValueError("There are missing operators in your expression!")
    return stack.pop()