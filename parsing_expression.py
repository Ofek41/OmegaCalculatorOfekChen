# This module is used for parsing the expression and making it ready for calculation.
from custom_exceptions import InvalidParenthesesError, UnmatchedOperandsAndOperatorsError
from operators_config import OPERATORS

def expression_to_list(expression: str) -> list:
    """
    This functions gets a string expression and returns a list in which every char appears individually.
    The function ignores the spaces, if were inserted.
    Float numbers will be appended to the list as one string.
    """
    tokens = []
    number = ""
    for char in expression:
        if char.isdigit() or char == '.':
            number += char
        else:
            if number:
                tokens.append(number)
                number = ""
            if char.strip():
                tokens.append(char)
    if number:
        tokens.append(number)
    return tokens

def deal_with_minus(tokens) -> list:
    """
    This function deals with every minus in the expression and creates a new list.
    """
    new_tokens = []
    for index, token in enumerate(tokens):
        if token == '-':
            if index == 0 or tokens[index - 1] in OPERATORS.keys() or tokens[index - 1] == '(':
                # Replace unary minus with tilde:
                new_tokens.append('~')
            else:
                # Binary minus:
                new_tokens.append(token)
        else:
            new_tokens.append(token)
    return new_tokens

def process_parentheses(tokens)->list:
    """
    This function gets the tokens list after it was fixed by the minus function, and dealing with
    all the parentheses - Empty ones, unmatched between closing and opening ones and more.
    Eventually, it returns the list after all the changes.
    """
    stack = [] # Stack for tracking the parentheses. The stack is implemented with a list
    new_tokens = []
    for index, token in enumerate(tokens):
        if token=='(':
            stack.append(index)
            new_tokens.append(token)
        elif token==')':
            if not stack:
                # Checks unmatched closing parenthesis:
               raise InvalidParenthesesError("Unmatched closing parenthesis!")
            opening_index = stack.pop()
            if index - opening_index == 1:
                # Checks if empty parentheses were written in the expression:
                raise InvalidParenthesesError("You cannot write empty parentheses.")
            new_tokens.append(token)
        # Checks valid use of parenthesis:
        else:
            new_tokens.append(token)
        # Checks unmatched opening parenthesis:
    if stack:
        raise InvalidParenthesesError("Unmatched opening parenthesis!")
    return new_tokens

def process_tilde(tokens_list) -> list:
    """
    This function deals with the tilde sign in the expression, due to the rules of tilde must be
    adjacent to a number, it cannot be used after parenthesis or a number, it cannot be at the end
    of the expression.
    Eventually, the function returns the new tokens list after it was processed.
    """
    index = 0
    new_tokens = []
    while index < len(tokens_list):
        token = tokens_list[index]
        if token == '~':
            if index > 0:
                prev_token = tokens_list[index - 1]
                if prev_token.replace('.', '', 1).isdigit() or prev_token == ')':
                    raise ValueError("Tilde cannot be after a number or parenthesis.")
            if index + 1 >= len(tokens_list):
                raise ValueError("Invalid use of tilde at the end of expression.")
            next_token = tokens_list[index + 1]
            if next_token.replace('.', '', 1).isdigit():
                new_tokens.append('~')
                new_tokens.append(next_token)
                index += 1
            elif next_token == '(':
                new_tokens.append('~')
            elif next_token == '~':
                new_tokens.append('~')
            else:
                raise ValueError("Invalid token after tilde.")
        else:
            new_tokens.append(token)
        index += 1
    return new_tokens

def apply_tilde(tokens_list)->list:
    """
    This function applies all the tildes affects into the expression, and returns a new
    tokens list.
    """
    index = 0
    new_tokens = []
    while index < len(tokens_list):
        token = tokens_list[index]
        if token == '~':
            tilde_count = 1
            index += 1
            # Counting more than one tilde:
            while index < len(tokens_list) and tokens_list[index] == '~':
                tilde_count += 1
                index += 1
            if index >= len(tokens_list):
                raise ValueError("Invalid use of tilde at the end of expression.")
            next_token = tokens_list[index]
            # If the count of ~ is even they cancel each other:
            need_tilde = (tilde_count % 2 == 1)
            if next_token.replace('.', '', 1).isdigit():
                if need_tilde:
                    new_tokens.append('~')
                new_tokens.append(next_token)
                index += 1
            elif next_token == '(':
                if need_tilde:
                    new_tokens.append('~')
                new_tokens.append('(')
                index += 1
                paren_count = 1
                while index < len(tokens_list) and paren_count > 0:
                    mini = tokens_list[index]
                    if mini == '(':
                        paren_count += 1
                    elif mini == ')':
                        paren_count -= 1
                    new_tokens.append(mini)
                    index += 1
                if paren_count != 0:
                    raise ValueError("Unmatched parentheses after tilde operator.")
            else:
                raise ValueError("Invalid token after tilde.")
        else:
            new_tokens.append(token)
            index += 1
    return new_tokens

def validate_operators(tokens):
    """
    This function gets a token list of the expression and validates all the operators in it,
    including position and validation of the operands.
    """
    for index, token in enumerate(tokens):
        if token in OPERATORS.keys():
            operator = OPERATORS[token]
            position = operator.position()
            if position == "middle":
                if index == 0 or index == len(tokens) - 1:
                    raise UnmatchedOperandsAndOperatorsError(f"{token} needs to have operands from both sides!")
                if tokens[index - 1] in OPERATORS.keys() or tokens[index + 1] in OPERATORS.keys():
                    raise ValueError(f"Invalid operands for operator '{token}'!")
            elif position == "left":
                if index == 0:
                    if token == '~':
                        # Allow '~' at the beginning (unary minus)
                        continue
                    else:
                        raise UnmatchedOperandsAndOperatorsError(f"{token} needs to have an operand on the left side!")
                if tokens[index - 1] in OPERATORS.keys() and OPERATORS[tokens[index - 1]].position() != 'left':
                    raise ValueError(f"Invalid operand for operator '{token}'!")
            elif position == "right":
                if index == len(tokens) - 1:
                    raise UnmatchedOperandsAndOperatorsError(f"{token} needs to have an operand on the right side!")
                # Allow multiple prefix operators
                if tokens[index + 1] in OPERATORS.keys() and OPERATORS[tokens[index + 1]].position() != 'right':
                    raise ValueError(f"Invalid operand for operator '{token}'!")