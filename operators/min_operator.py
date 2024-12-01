from .base_operator import Operator

class Minimum(Operator):
    def priority(self):
        return 5
    def position(self):
        return "middle"
    def operate(self, op1, op2):
        self.validate(op1, op2)
        return op1 if op1<op2 else op2