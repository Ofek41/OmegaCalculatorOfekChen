from .base_operator import Operator
class Factorial(Operator):
    def priority(self):
        return 6
    def position(self):
        return "left"
    @staticmethod
    def operate(op):
        if not isinstance(op, int) or op < 0:
            raise ValueError("Factorial is only defined for non-negative integers.")
        if op == 0:
            return 1
        result = 1
        for i in range(1, op + 1):
            result *= i
        return result
