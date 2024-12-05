import pytest
from parsing_expression import *
from custom_exceptions import InvalidParenthesesError

def test_exp_to_list():
    exp = "3+4"
    assert expression_to_list(exp)== ["3", "+", "4"]

def test_dealing_with_minus():
    lst = ["-", "3", "+", "4"]
    assert deal_with_minus(lst)==["-3", "+", "4"]

def test_parentheses():
    lst = ["(", "3", "+", "4"]
    with pytest.raises(InvalidParenthesesError):
        process_parentheses(lst)

def test_tilde():
    lst = ["~", "3"]
    assert process_tilde(lst)==["-3"]