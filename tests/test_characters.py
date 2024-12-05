import pytest
from process_expression import check_full_validation_of_expression
from custom_exceptions import *
from implementing_custom_exceptions import *

def test_invalid_char():
    exp = "3+4N"
    with pytest.raises(InvalidCharacterInExpressionError):
        check_invalid_character(exp)

def test_gibberish():
    exp = "abcde"
    with pytest.raises(GibberishExpressionError):
        check_gibberish_expression(exp)