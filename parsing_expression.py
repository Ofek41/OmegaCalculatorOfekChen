# This module is used for parsing the expression and making it ready for calculation.
from custom_exceptions import InvalidParenthesesError
from main import OPERATORS
def expression_to_list(expression: str) -> list:
    """
    This functions gets a string expression and returns a list in which every char appears individually.
    The function ignores the spaces, if were inserted.
    Float numbers will be appended to the list as one string.
    """
    tokens = []
    number=""
    for char in expression:
        if char.isdigit() or char=='.': number+=char
        else:
            if number:
                tokens.append(number)
                number = ""
            if char.strip(): tokens.append(char)
    if number: tokens.append(number)
    return tokens

def deal_with_minus(expression_list)->list:
    """
    This function deals with every minus in the expression and creates a new list.
    """
    tokens = []
    index = 0
    while index < len(expression_list):
        token = expression_list[index]
        if token == '-':
            if index==0 or (tokens and tokens[-1] in OPERATORS.keys()):
                next_token = expression_list[index+1] if index+1<len(expression_list) else None
                if isinstance(next_token, (int, float)):
                    tokens.append(-next_token)
                    index+=1
                else:
                    raise ValueError("You used minus operator in an invalid way.")
            else:
                tokens.append(token)
        else:
            tokens.append(token)
    index+=1
    return tokens

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

def process_tilde(tokens_list)->list:
    """
    This function deals with the tilde sign in the expression, due to the rules of tilde must be
    adjacent to a number, it cannot be used after parenthesis or a number, it cannot be at the end
    of the expression.
    Eventually, the function returns the new tokens list after it was processed.
    """
    index = 0
    new_tokens = []
    while index<len(tokens_list):
        token = tokens_list[index]
        if token=='~':
            # Tilde cannot be after a number or an opening parenthesis:
            if index>0:
                prev_token = tokens_list[index-1]
                if isinstance(prev_token, (int, float)) or prev_token==')':
                    raise ValueError("Tilde cannot be after a number or parenthesis.")
                # Tilde cannot be at the end of the expression:
            if index+1>=len(tokens_list):
                raise ValueError("Invalid using of tilde at the end!")
            next_token = tokens_list[index+1]
            # Checks valid use of tilde:
            if isinstance(next_token, (int,float)) or next_token in ['~', '-', '(']:
                new_tokens.append(token)
                index+=1
            else:
                raise ValueError("Tilde must be followed by a number, another tilde, or parenthesis.")
        else:
            new_tokens.append(token)
            index+=1
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
            # Count following tildes:
            while index < len(tokens_list) and tokens_list[index] == '~':
                tilde_count += 1
                index += 1
            # Check the next token after the tildes
            if index >= len(tokens_list):
                raise ValueError("Invalid use of tilde at the end of expression at.")
            next_token = tokens_list[index]
            negative = tilde_count % 2 == 1  # Check if necessary to negate the number
            if isinstance(next_token, (int,float)):
                # Convert the number and apply negation if necessary
                number = float(next_token)
                if negative:
                    number = -number
                new_tokens.append(str(number))
                index += 1
            elif next_token == '-':
                # Deals with negative numbers after the tilde, and make them positive:
                index += 1
                if index >= len(tokens_list):
                    raise ValueError("Invalid use of minus after tilde.")
                num_token = tokens_list[index]
                if isinstance(num_token, (int,float)):
                    number = float(num_token)
                    if negative:
                        number = -(-number)
                    else:
                        number = -number
                    new_tokens.append(str(number))
                    index += 1
                else:
                    raise ValueError("Invalid token after using tilde and then minus.")
            elif next_token == '(':
                # Deals with parenthesis in the expression:
                if negative:
                    # If we need to negate, add a minus sign before the opening parenthesis
                    new_tokens.append('-')
                # Add the opening parenthesis
                new_tokens.append('(')
                index += 1
                paren_count = 1
                while index < len(tokens_list) and paren_count > 0:
                    token = tokens_list[index]
                    if token == '(':
                        paren_count += 1
                    elif token == ')':
                        paren_count -= 1
                    new_tokens.append(token)
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
    This function gets a token list of the expression and validating all the operators in it,
    including position and validation of the operands.
    """
    for index, token in enumerate(tokens):
        # Checking if the token in the expression is an operator from the global OPERATORS dict.
        # If so, the function gets its details.
        if token in OPERATORS.keys():
            operator = OPERATORS[token]
            position = operator.position()
            if position == "middle": # If the position is middle, check both sides of the operator:
                if index == 0 or index == len(tokens) - 1:
                    raise ValueError(f"{token} needs to have operands from both sides!")
                left_operand = tokens[index -1]
                right_operand = tokens[index+1]
                # Validating the operands' types:
                operator.validate(left_operand, right_operand)
            elif position == "left": # If the position is middle, check right side of the operator:
                if index == len(tokens) - 1:
                    raise ValueError(f"{token} needs to have an operand on the right side!")
                right_operand = tokens[index+1]
                operator.validate(right_operand)
            elif position == "right": # If the position is right, check left side of the operator:
                if index == 0:
                    raise ValueError(f"{token} needs to have an operand on the left side!")
                left_operand = tokens[index-1]
                operator.validate(left_operand)