from .base_operator import Operator

class Average(Operator):
    def position(self):
        return "middle"
    def priority(self):
        return 5
    def operate(self, op1, op2):
        self.validate(op1, op2)
        return (op1+op2)/2