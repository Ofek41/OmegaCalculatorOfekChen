from parsing_expression import *
from implementing_custom_exceptions import *
from operators import *
from operators_config import find_key_by_value

def check_full_validation_of_expression(expression: str) -> list:
    if not expression.strip():
        raise EmptyExpressionError("The expression is empty.")
    expression = expression.replace(" ", "")  # Remove spaces
    check_invalid_character(expression)
    check_gibberish_expression(expression)
    tokens = expression_to_list(expression)
    check_valid_decimal(tokens)
    tokens = minus_parse(tokens)  # Process minus signs
    tokens = process_tilde(tokens)  # Handle tilde
    for index, token in enumerate(tokens):
        if token in OPERATORS:
            tokens[index] = OPERATORS[token]
    validate_left_operators(tokens)
    return tokens

def infix_to_postfix(tokens: list):
    stack = []  # Operator stack
    postfix_expression = []  # Resulting postfix expression
    for token in tokens:
        if isinstance(token, str) and token.replace('.', '', 1).isdigit():  # Operand
            postfix_expression.append(token)
        elif isinstance(token, Operator):  # Operators
            while stack and isinstance(stack[-1], Operator) and (stack[-1].priority()>token.priority() or
                stack[-1].priority()==token.priority() and not isinstance(token, (UMinus, SMinus))):
                popped = stack.pop()
                postfix_expression.append(popped)
            if token.position()=="left":
                postfix_expression.append(token)
            else:
                stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                popped = stack.pop()
                postfix_expression.append(popped)
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
    stack = []
    for token in expression:
        if isinstance(token, str) and token.replace('.', '', 1).isdigit():  # Operand
            stack.append(float(token) if '.' in token else int(token))
        elif isinstance(token, Operator):  # Operator
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
                result = token.operate(a, b)
                stack.append(result)
    if len(stack)>1:
        raise ValueError("There are missing operators in your expression!")
    return stack.pop()