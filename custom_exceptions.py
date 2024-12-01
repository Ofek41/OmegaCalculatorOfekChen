# Creating custom exceptions for the calculator:
class InvalidParenthesesError(Exception):
    """
    Exception that is raised when the user made mistake when defining the parentheses in the expression.
    """
    def __init__(self, message):
        super().__init__(message)

class InvalidCharacterInExpressionError(Exception):
    """
    Exception that is raised when the user inserted invalid characters into the expression.
    """
    def __init__(self, message):
        super().__init__(message)

class GibberishExpressionError(Exception):
    """
    Exception that is raised when the user inserted gibberish expression.
    """
    def __init__(self, message):
        super().__init__(message)


class UnmatchedOperandsAndOperatorsError(Exception):
    """
    Exception that is raised when the user inserted an expression in which there are no matches between
    the operands and the operators: for example, two operators next to each one
    """
    def __init__(self, message):
        super().__init__(message)
