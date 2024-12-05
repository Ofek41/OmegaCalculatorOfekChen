import pytest
from process_expression import infix_to_postfix, check_full_validation_of_expression

def test_simple_expression():
    simple_expression = "3 + 4"
    assert infix_to_postfix(simple_expression) == "3 4 +"

def test_expression_including_parentheses():
    expression = "3 * (4 + 2)"
    assert infix_to_postfix(expression)=="3 4 2 + *"