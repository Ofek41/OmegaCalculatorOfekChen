import pytest
from parsing_expression import *

def test_expression_to_list():
    expression = "3+5-6"
    expression_list = ['3','+','5','-','6']
    assert expression_to_list(expression) == expression_list

def test_unmatched_closing_parentheses():
    expression_list = ['(', '4', '+', '5']
    with pytest.raises(InvalidParenthesesError):
        process_parentheses(expression_list)

def test_unmatched_opening_parentheses():
    expression_list = ['4', '+', '5', ')']
    with pytest.raises(InvalidParenthesesError):
        process_parentheses(expression_list)

def test_two_tildes_in_a_row():
    expression_list = ['~', '~', '5']
    with pytest.raises(TildeError):
        process_tilde(expression_list)

def test_invalid_tilde_position():
    expression_list = ['5', '~']
    with pytest.raises(TildeError):
        process_tilde(expression_list)