from .base_operator import Operator

class Average(Operator):
    def position(self):
        return "middle"
    def priority(self):
        return 5
    def operate(self, op1, op2):
        self.validate(op1, op2)
        return (float(op1) + float(op2)) / 2
    def arity(self):
        return 2