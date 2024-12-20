from .base_operator import Operator
from math import pow

class Power(Operator):
    def position(self):
        return "middle"
    def priority(self):
        return 3
    def operate(self, op1, op2):
        if op1==0 and op2<=0:
            raise ValueError("Cannot pow 0 by non-positive number.")
        if op1<0 and isinstance(op2,float):
            raise ValueError("Cannot pow a negative number by a non-integer number.")
        self.validate(op1, op2)
        return pow(op1, op2)

    def arity(self):
        return 2