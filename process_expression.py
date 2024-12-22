from parsing_expression import *
from implementing_custom_exceptions import *
from operators import *
from operators_config import find_key_by_value

def check_full_validation_of_expression(expression: str) -> list:
    if not expression.strip():
        raise EmptyExpressionError("The expression is empty.")
    expression = expression.replace(" ", "")  # Remove spaces
    # Validating the characters:
    check_gibberish_expression(expression)
    check_invalid_character(expression)
    tokens = expression_to_list(expression)
    check_valid_decimal(tokens)
    tokens = process_parentheses(tokens)
    tokens = minus_parse(tokens)
    tokens = process_tilde(tokens)
    # Converting the operators to their class instance
    for index, token in enumerate(tokens):
        if token in OPERATORS:
            tokens[index] = OPERATORS[token]
    validate_left_operators(tokens)
    return tokens

def infix_to_postfix(tokens: list):
    """
    This function gets an infix expression and converting it into a postfix one.
    """
    # Operator stack:
    stack = []
    # Resulting postfix expression:
    postfix_expression = []
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
            # Remove the '(':
            stack.pop()
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
            # Unary operator:
            if arity == 1:
                if not stack:
                    key = find_key_by_value(OPERATORS, token)
                    raise UnmatchedOperandsAndOperatorsError(f"Operator '{key}' requires one operand.")
                operand = stack.pop()
                result = token.operate(operand)
                stack.append(result)
            # Binary operator:
            elif arity == 2:
                if len(stack) < 2:
                    key = find_key_by_value(OPERATORS, token)
                    raise UnmatchedOperandsAndOperatorsError(f"Operator '{key}' requires two operands.")
                value2 = stack.pop()
                value1 = stack.pop()
                # Calculating the result:
                result = token.operate(value1, value2)
                stack.append(result)
    # If there is more than one result in the stack
    if len(stack)>1:
        raise ValueError("There are missing operators in your expression!")
    return stack.pop()