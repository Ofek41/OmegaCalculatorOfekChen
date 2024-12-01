from .base_operator import Operator
class Factorial(Operator):
    def priority(self):
        return 6
    def position(self):
        return "right"
    @staticmethod
    def operate(self, op):
        if not isinstance(op, int) or op<0:
            raise ValueError("Can only factorial on non-negative integers.")
        if op==0: return 1
        result = 1
        for index in range(1, op+1):
            result*=index
        return result