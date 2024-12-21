import pytest
from custom_exceptions import TildeError
from operators import *
from operators_config import OPERATORS


@pytest.fixture
# Returning the global OPERATORS dictionary.
def operators():
    return OPERATORS


@pytest.fixture
# A list of valid expressions.
def valid_expressions():
    return [
        "3 + 4",
        "2 * (3 + 5)",
        "-1 + 2",
        "4 / 2",
        "7 - ~3",
        "2! + 5",
        "3 # 2",
    ]


@pytest.fixture
# A list of invalid expression.
def invalid_expressions():
    return [
        "3 ++ 4",
        "2 * (3 + 5",
        "4 / 0",
        "7 - * 3",
        "2.3.5 + 4",
        "!3 + 5",
        "# 2",
    ]


@pytest.fixture
# A list of expression with different kinds of minus signs.
def tokens_with_minus():
    return [
        (["-", "1", "+", "7"], [UMinus(), "1", "+", "7"]),
        (["3", "-", "-", "2"], ["3", Sub(), UMinus(), "2"]),
    ]


@pytest.fixture
# A list of expression with tildes.
def tokens_with_tilde():
    return [
        (["~", "3"], [Negative(), "3"]),
        (["~", "~", "3"], TildeError),
    ]


@pytest.fixture
# Another list of valid expressions.
def valid_tokens():
    return [
        ["3", "+", "4"],
        ["2", "*", "3", "+", "5"],
        ["-", "1", "+", "2"],
    ]


@pytest.fixture
# A list of expressions in their postfix notations.
def postfix_expressions():
    return [
        (["3", "4", Add()], 7),
        (["2", "3", Multiply(), "5", Add()], 11),
        (["1", "2", Add()], 3),
    ]