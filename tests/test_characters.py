import pytest
from implementing_custom_exceptions import *
from custom_exceptions import MathematicsError
from operators.hashtag_operator import Hashtag

def test_invalid_char():
    """
    Test an expression with an invalid char and checks if an exception is raised.
    """
    exp = "3+4N"
    with pytest.raises(InvalidCharacterInExpressionError):
        check_invalid_character(exp)

def test_gibberish():
    """
    Test a gibberish expression and checks if an exception is raised.
    """
    exp = "abcde"
    with pytest.raises(GibberishExpressionError):
        check_gibberish_expression(exp)

def test_hashtag():
    """
    Test the functionality of the hashtag operator.
    """
    number = 123
    hashtag = Hashtag()
    assert hashtag.operate(number)==6

def test_hashtag_exception():
    """
    Test the functionality of the hashtag operator.
    """
    hashtag = Hashtag()
    number = -56
    with pytest.raises(MathematicsError):
        hashtag.operate(number)

def test_double_hashtag():
    """
    Test the functionality of the hashtag operator.
    """
    hashtag = Hashtag()
    hashtag2 = Hashtag()
    calc = hashtag2.operate(178)
    assert hashtag.operate(calc)==7