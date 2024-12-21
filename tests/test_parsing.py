import pytest
from parsing_expression import *
from tests.conftest import tokens_with_tilde
from process_expression import check_full_validation_of_expression

def test_expression_to_list():
    """
    Test if the expression is converted to list right.
    """
    expression = "3+5-6"
    expression_list = ['3','+','5','-','6']
    assert expression_to_list(expression) == expression_list

def test_expression_to_list2(valid_expressions):
    """
    Test if the expressions are converted to list right.
    """
    for expression in valid_expressions:
        tokens = expression_to_list(expression)
        assert isinstance(tokens, list)

def test_expression_not_to_list(invalid_expressions):
    """
    Check if an exception is raised when trying to full validate the expression.
    """
    for expression in invalid_expressions:
        try:
            tokens = check_full_validation_of_expression(expression)
            assert False
        except Exception:
            pass

def test_unmatched_closing_parentheses():
    """
    Test an expression with unmatched closing parentheses.
    """
    expression_list = ['(', '4', '+', '5']
    with pytest.raises(InvalidParenthesesError):
        process_parentheses(expression_list)

def test_unmatched_opening_parentheses():
    """
    Test an expression with unmatched opening parentheses.
    """
    expression_list = ['4', '+', '5', ')']
    with pytest.raises(InvalidParenthesesError):
        process_parentheses(expression_list)

def test_two_tildes_in_a_row():
    """
    Test an expression with two tildes in a row and checks if an exception is raised.
    """
    expression_list = ['~', '~', '5']
    with pytest.raises(TildeError):
        process_tilde(expression_list)

def test_invalid_tilde_position():
    """
    Test an expression with an invalid tilde position and checks if an exception is raised.
    """
    expression_list = ['5', '~']
    with pytest.raises(TildeError):
        process_tilde(expression_list)

def test_valid_tildes(tokens_with_tilde):
    """
    Test expression with valid tildes.
    """
    for tokens, expected in tokens_with_tilde:
        if isinstance(expected, type) and issubclass(expected, Exception):
            with pytest.raises(expected):
                process_tilde(tokens)
        else:
            parsed = process_tilde(tokens)
            assert all(isinstance(value1, type(value2)) for value1, value2 in zip(parsed, expected))