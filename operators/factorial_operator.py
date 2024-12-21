from .base_operator import Operator
from custom_exceptions import MathematicsError
class Factorial(Operator):
    def priority(self):
        return 6

    def position(self):
        # Postfix operator
        return "left"

    def operate(self, op):
        if not isinstance(op, (int, float)) or int(op)!=op or op < 0:
            raise MathematicsError("Factorial is only defined for non-negative integers.")
        op = int(op)
        result = 1
        for i in range(1, int(op) + 1):
            result *= i
        return result

    def arity(self):
        return 1
