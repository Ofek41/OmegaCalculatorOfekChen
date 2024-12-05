import pytest
from process_expression import infix_to_postfix
from custom_exceptions import InvalidParenthesesError

def test_simple_expression():
    simple_expression = "3 + 4"
    assert infix_to_postfix(simple_expression) == "3 4 +"

def test_expression_including_parentheses():
    expression = "3*(4+2)"
    assert infix_to_postfix(expression)=="3 4 2 + *"

def test_expression_including_nested_parentheses():
    expression = "(3 + (2 * (4 - 1)))"
    assert infix_to_postfix(expression) == "3 2 4 1 - * +"

def test_expression_with_decimal_numbers():
    expression = "3.15*(2+1)"
    assert infix_to_postfix(expression) == "3.15 2 1 + *"

def test_expression_with_negative():
    expression = "-3+4"
    assert infix_to_postfix(expression)=="-3 4 +"

def test_special_operator():
    expression = "3+4 *2@6"
    assert infix_to_postfix(expression)=="3 4 2 6 @ * +"

def test_invalid():
    with pytest.raises(InvalidParenthesesError, match="Unmatched opening parenthesis"):
        expression = "3+4(*"
        infix_to_postfix(expression)

def test_empty():
    with pytest.raises(ValueError, match="The expression is empty"):
        infix_to_postfix("")