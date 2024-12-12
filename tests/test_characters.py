import pytest
import operators.hashtag_operator
from implementing_custom_exceptions import *
from operators.hashtag_operator import Hashtag

def test_invalid_char():
    exp = "3+4N"
    with pytest.raises(InvalidCharacterInExpressionError):
        check_invalid_character(exp)

def test_gibberish():
    exp = "abcde"
    with pytest.raises(GibberishExpressionError):
        check_gibberish_expression(exp)

def test_hashtag():
    number = 123
    hashtag = Hashtag()
    assert hashtag.operate(number)==6

def test_hashtag_exception():
    hashtag = Hashtag()
    number = -56
    with pytest.raises(ValueError):
        hashtag.operate(number)