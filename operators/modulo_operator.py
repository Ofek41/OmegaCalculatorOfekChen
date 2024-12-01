from .base_operator import Operator
class Modulo(Operator):
    def priority(self):
        return 4
    def position(self):
        return "middle"
    @staticmethod
    def operate(self, op1, op2):
        if not isinstance((op1,op2),int) or op1<0 or op2<0:
            raise ValueError("Can only modulo on non-negative integers.")
        if op2==0:
            raise ZeroDivisionError("Tried to modulo on zero.")
        return op1%op2