# Creating custom exceptions for the calculator. Every exception inherits from the upper class Exception,
# so in the function main, if an error was caught, it will be raised and presented to the user.
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

class TildeError(Exception):
    """
    Exception that is raised when the user inserted a tilde in an invalid way.
    """
    def __init__(self, message):
        super().__init__(message)

class MinusError(Exception):
    """
    Exception that is raised when the user inserted a minus in an invalid way.
    """
    def __init__(self, message):
        super().__init__(message)

class EmptyExpressionError(Exception):
    """
    Exception that is raised when the user inserted an empty expression.
    """
    def __init__(self, message):
        super().__init__(message)

class MathematicsError(Exception):
    """
    Exception that is raised when the user inserted an expression with a mathematics error.
    """
    def __init__(self, message):
        super().__init__(message)

class InvalidDecimalNumber(Exception):
    """
    Exception that is raised when the user inserted an invalid decimal number.
    """
    def __init__(self, message):
        super().__init__(message)
