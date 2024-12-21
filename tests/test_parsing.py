import pytest
from parsing_expression import *
from tests.conftest import tokens_with_tilde


def test_expression_to_list():
    expression = "3+5-6"
    expression_list = ['3','+','5','-','6']
    assert expression_to_list(expression) == expression_list

def test_expression_to_list2(valid_expressions):
    for expression in valid_expressions:
        tokens = expression_to_list(expression)
        assert isinstance(tokens, list)

def test_expression_not_to_list(invalid_expressions):
    for expression in invalid_expressions:
        try:
            tokens = expression_to_list(expression)
            assert False
        except ValueError:
            pass

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

def test_valid_tildes(tokens_with_tilde):
    for tokens, expected in tokens_with_tilde:
        if isinstance(expected, Exception):
            with pytest.raises(expected):
                process_tilde(tokens)
        else:
            parsed = process_tilde(tokens)
            assert all(str(type(t)) == e for t, e in zip(parsed, expected))