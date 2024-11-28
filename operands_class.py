from abc import ABC, abstractmethod
# Creating an abstract class for all the operands:
class Operand(ABC):
    @abstractmethod
    def priority(self):
        pass
    @abstractmethod
    def position(self):
        pass

# The operands class - each one contains the operand's priority and position in the equation:
class Add(Operand):
    def priority(self):
        return 1
    def position(self):
        return "middle"

class Sub(Operand):
    def priority(self):
        return 1
    def position(self):
        return "middle"

class Multiply(Operand):
    def position(self):
        return "middle"
    def priority(self):
        return 2

class Division(Operand):
    def position(self):
        return "middle"
    def priority(self):
        return 2

class Power(Operand):
    def position(self):
        return "middle"
    def priority(self):
        return 3

class Average(Operand):
    def position(self):
        return "middle"
    def priority(self):
        return 5

class Maximum(Operand):
    def priority(self):
        return 5
    def position(self):
        return "middle"

class Minimum(Operand):
    def priority(self):
        return 5
    def position(self):
        return "middle"

class Modulo(Operand):
    def priority(self):
        return 4
    def position(self):
        return "middle"

class Negative(Operand):
    def priority(self):
        return 6
    def position(self):
        return "left"

class Factorial(Operand):
    def priority(self):
        return 6
    def position(self):
        return "right"