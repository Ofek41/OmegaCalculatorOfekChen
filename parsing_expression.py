from operators_config import *
from custom_exceptions import InvalidParenthesesError, TildeError, MinusError
from operators.SMinus_operator import SMinus
from operators.UMinus_operator import UMinus
from operators.sub_operator import Sub

def expression_to_list(expression: str) -> list:
    """
    Converts the expression string into a list of tokens.
    """
    tokens = []
    number = ""
    index = 0
    while index < len(expression):
        char = expression[index]
        if char.isdigit() or char == '.':
            number += char
            index += 1
        else:
            if number:
                tokens.append(number)
                number = ""
            if char.strip():
                tokens.append(char)
            index += 1
    if number:
        tokens.append(number)
    return tokens


def minus_parse(expression: list):
    """
    Parsing all the minus signs in the expression.
    """
    index = 0
    while index < len(expression):
        if expression[index] == '-':
            if index == 0 or expression[index - 1] == '(':
                expression[index] = UMinus()
                index += 1
                while index<len(expression) and expression[index]=='-':
                    expression[index]=UMinus()
                    index+=1
                if index < len(expression):
                    next_token = expression[index]
                    if not ((isinstance(next_token, str) and (next_token.replace('.', '', 1).isdigit() or next_token == '(')) or isinstance(next_token, (UMinus, SMinus))):
                        raise MinusError(f"Invalid token '{next_token}' after an unary minus.")
            elif index>0 and (expression[index-1].replace('.','',1).isdigit() or expression[index-1] in OPERATORS and OPERATORS[expression[index-1]].position()=="left"
                    or expression[index-1]==')'):
                expression[index] = Sub()
                index += 1
                while index < len(expression) and expression[index] == '-':
                    expression[index] = SMinus()
                    index += 1
                if index < len(expression):
                    next_token = expression[index]
                    if not ((isinstance(next_token, str) and (next_token.replace('.', '', 1).isdigit() or next_token == '(' or next_token=='~')) or isinstance(next_token, (UMinus, SMinus))):
                        raise MinusError(f"Invalid token '{next_token}' after a binary minus.")
            elif index>0 and expression[index-1] in OPERATORS:
                while index<len(expression) and expression[index]=='-':
                    expression[index]=SMinus()
                    index+=1
        else:
            index += 1
    return expression


def process_parentheses(tokens) -> list:
    """
    Validates and processes parentheses in the tokens list.
    """
    stack = []
    for index, token in enumerate(tokens):
        if token == '(':
            stack.append(token)
        elif token == ')':
            if not stack or stack[-1] != '(':
                raise InvalidParenthesesError("Unmatched closing parenthesis.")
            stack.pop()
    if stack:
        raise InvalidParenthesesError("Unmatched opening parenthesis.")
    return tokens


def process_tilde(tokens: list) -> list:
    """
    Processes the tilde (~) operator in the expression.
    """
    processed = []
    index = 0
    while index < len(tokens):
        token = tokens[index]
        if token == '~':
            # Check if tilde is in a valid position
            if index == 0 or tokens[index - 1] in OPERATORS or tokens[index - 1] == '('\
                    or isinstance(tokens[index-1], Sub):
                # Prevent multiple tildes
                if index + 1 < len(tokens) and tokens[index + 1] == '~':
                    raise TildeError("Multiple tildes are not allowed.")
                processed.append(Negative())
            else:
                raise TildeError(f"You tried to use ~ in an invalid position.")
        else:
            processed.append(token)
        index += 1
    return processed