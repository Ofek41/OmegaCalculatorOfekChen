from abc import ABC, abstractmethod
from math import pow
# Creating an abstract class for all the operands:
class Operand(ABC):
    @abstractmethod
    def priority(self):
        pass
    @abstractmethod
    def position(self):
        pass
    """
    Function that gets the args of the function and checks if they are integers or floats.
    If not, raises a value error.
    """
    def validate(self, *args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError("Invalid operators! Operators must be integers or floats!")

# The operands class - each one contains the operand's priority and position in the equation,
# as well as operating function:
class Add(Operand):
    def priority(self):
        return 1
    def position(self):
        return "middle"
    def operate(self, operator1, operator2):
        self.validate(operator1, operator2)
        return operator1 + operator2

class Sub(Operand):
    def priority(self):
        return 1
    def position(self):
        return "middle"
    def operate(self, operator1, operator2):
        self.validate(operator1, operator2)
        return operator1 - operator2

class Multiply(Operand):
    def position(self):
        return "middle"
    def priority(self):
        return 2
    def operate(self, op1, op2):
        self.validate(op1, op2)
        return op1 * op2

class Division(Operand):
    def position(self):
        return "middle"
    def priority(self):
        return 2
    def operate(self, op1, op2):
        if op2==0:
            raise ZeroDivisionError("Cannot divide by zero.")
        self.validate(op1, op2)
        return op1 / op2

class Power(Operand):
    def position(self):
        return "middle"
    def priority(self):
        return 3
    def operate(self, op1, op2):
        if op1==0 and op2==0:
            raise ValueError("Cannot pow 0 by 0.")
        self.validate(op1, op2)
        return pow(op1, op2)

class Average(Operand):
    def position(self):
        return "middle"
    def priority(self):
        return 5
    def operate(self, op1, op2):
        self.validate(op1, op2)
        return (op1+op2)/2

class Maximum(Operand):
    def priority(self):
        return 5
    def position(self):
        return "middle"
    def operate(self, op1, op2):
        self.validate(op1, op2)
        return op1 if op1>op2 else op2

class Minimum(Operand):
    def priority(self):
        return 5
    def position(self):
        return "middle"
    def operate(self, op1, op2):
        self.validate(op1, op2)
        return op1 if op1<op2 else op2

class Modulo(Operand):
    def priority(self):
        return 4
    def position(self):
        return "middle"
    def operate(self, op1, op2):
        if not isinstance((op1,op2),int) or op1<0 or op2<0:
            raise ValueError("Can only modulo on non-negative integers.")
        return op1%op2

class Negative(Operand):
    def priority(self):
        return 6
    def position(self):
        return "left"
    def operate(self, op):
        self.validate(op)
        return -op

class Factorial(Operand):
    def priority(self):
        return 6
    def position(self):
        return "right"
    def operate(self, op):
        if not isinstance(op, int) or op<0:
            raise ValueError("Can only factorial on non-negative integers.")
        result = 1
        for index in range(1, op+1):
            result*=index
        return result