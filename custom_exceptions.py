# Creating custom exceptions for the calculator:
"""
Exception that is raised when the user made mistake when defining the parentheses in the expression.
"""
class InvalidParenthesesError(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return "Error message:",

"""
Exception that is raised when the user inserted invalid characters into the expression.
"""
class InvalidCharacterInExpressionError(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return "Error message:",

"""
Exception that is raised when the user inserted gibberish expression.
"""
class GibberishExpressionError(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return "Error message:",

"""
Exception that is raised when the user inserted an expression in which there are no matches between
the operands and the operators: for example, two operators next to each one
"""
class UnmatchedOperandsAndOperatorsError(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return "Error message:",