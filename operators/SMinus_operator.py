
from .base_operator import Operator
class SMinus(Operator):
    def priority(self):
        # Highest priority
        return 10

    def position(self):
        return "right"

    def operate(self, op):
        self.validate(op)
        return -op

    def arity(self):
        return 1