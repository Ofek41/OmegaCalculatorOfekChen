from .base_operator import Operator
class Factorial(Operator):
    def priority(self):
        return 6

    def position(self):
        return "left"  # Postfix operator

    def operate(self, op):
        if not isinstance(op, (int, float)) or int(op)!=op or op < 0:
            raise ValueError("Factorial is only defined for non-negative integers.")
        op = int(op)
        result = 1
        for i in range(1, int(op) + 1):
            result *= i
        return result

    def arity(self):
        return 1
