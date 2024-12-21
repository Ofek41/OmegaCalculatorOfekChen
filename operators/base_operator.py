from abc import ABC, abstractmethod
# Creating an abstract class for all the operators:
class Operator(ABC):
    @abstractmethod
    def priority(self):
        # This function returns the operators priority comparing to the other ones.
        pass

    @abstractmethod
    def position(self):
        # This function returns the operator position in the expression.
        pass

    @staticmethod
    def validate(*args):
        """
           Function that gets the args of the function and checks if they are integers or floats.
           If not, raises a value error.
           """
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError("Invalid operators! Operators must be integers or floats!")

    @abstractmethod
    def arity(self):
        # This function returns 1 if the operators is unary, and 2 if binary.
        pass