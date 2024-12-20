from .base_operator import Operator
class Negative(Operator):
    def priority(self):
        return 6
    def position(self):
        return "right"  # Prefix operator
    def operate(self, op):
        return -op
    def arity(self):
        return 1