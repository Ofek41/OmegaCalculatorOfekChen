import pytest
from process_expression import *
from implementing_custom_exceptions import *

def test_check_full_validation_of_expression_valid():
    """
    Test a valid expression
    """
    expression = "3 + 4 * 2 / (1 - 5)^2^3"
    tokens = check_full_validation_of_expression(expression)
    assert isinstance(tokens, list)
    assert len(tokens) > 0

def test_check_full_validation_of_expression_empty():
    """
    Test that an empty expression raises ValueError
    """
    expression = "   "
    with pytest.raises(EmptyExpressionError):
        check_full_validation_of_expression(expression)


def test_check_full_validation_of_expression_invalid_characters():
    """
    Test that an expression with invalid characters raises ValueError
    """
    expression = "3 + 4a * 2"
    with pytest.raises(InvalidCharacterInExpressionError):
        check_invalid_character(expression)


def test_infix_to_postfix_unmatched_parentheses():
    """
    Test infix to postfix conversion with unmatched parentheses raises InvalidParenthesesError
    """
    tokens = ['(', '3', '+', '4', '*', '2']
    with pytest.raises(InvalidParenthesesError):
        infix_to_postfix(tokens)


def test_validate_left_operators_invalid():
    """
    Test the validation of left unary operators.
    """
    invalid_tokens =  [["3", "!"], ["2", "#"]]
    for tokens in invalid_tokens:
        validate_left_operators(tokens)

def test_postfix_calculation(postfix_expressions):
    """
    Test some expression in calculating postfix.
    """
    for expression, expected in postfix_expressions:
        result = postfix_calculation(expression)
        assert result == expected