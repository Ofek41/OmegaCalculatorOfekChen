import pytest
from operators_config import OPERATORS
from parsing_expression import *
from process_expression import *

@pytest.fixture
def operators():
    return OPERATORS

@pytest.fixture
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
def tokens_with_minus():
    return [
        (["-", "1", "+", "7"], ["UMinus", "1", "+", "7"]),
        (["3", "+", "-", "2"], ["3", "+", "UMinus", "2"]),
    ]


@pytest.fixture
def tokens_with_tilde():
    return [
        (["~", "3"], ["Negative", "3"]),
        (["~", "~", "3"], TildeError),
    ]


@pytest.fixture
def valid_tokens():
    return [
        ["3", "+", "4"],
        ["2", "*", "3", "+", "5"],
        ["-", "1", "+", "2"],
    ]


@pytest.fixture
def postfix_expressions():
    return [
        (["3", "4", "+"], 7),
        (["2", "3", "*", "5", "+"], 11),
        (["1", "2", "+"], 3),
    ]