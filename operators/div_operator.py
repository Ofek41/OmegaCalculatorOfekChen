from .base_operator import Operator
class Division(Operator):
    def position(self):
        return "middle"
    def priority(self):
        return 2
    def operate(self, op1, op2):
        if op2==0:
            raise ZeroDivisionError("Cannot divide by zero.")
        self.validate(op1, op2)
        return op1 / op2
