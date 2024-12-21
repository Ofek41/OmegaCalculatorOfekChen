from .base_operator import Operator
class Modulo(Operator):
    def priority(self):
        return 4

    def position(self):
        return "middle"

    def operate(self, op1, op2):
        if op2 == 0:
            raise ZeroDivisionError("Cannot modulo by zero.")
        self.validate(op1, op2)
        return op1 % op2

    def arity(self):
        return 2
