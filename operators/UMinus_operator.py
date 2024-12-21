from .base_operator import Operator
class UMinus(Operator):
    def priority(self):
        return 2.5

    def position(self):
        return "right"

    def operate(self, op):
        self.validate(op)
        return -op

    def arity(self):
        return 1