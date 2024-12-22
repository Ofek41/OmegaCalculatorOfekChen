from .base_operator import Operator
from custom_exceptions import MathematicsError

class Hashtag(Operator):
    def priority(self):
        return 6

    def position(self):
        return "left"

    def operate(self, op):
        self.validate(op)
        if op < 0:
            raise MathematicsError("Cannot sum digits of a negative number.")
        str_op = str(op)
        if 'e+' in str_op:
            raise MathematicsError("Too large number for # operator.")
        str_op = str_op.replace('.', '')
        sum_digits = sum(int(digit) for digit in str_op)
        return sum_digits

    def arity(self):
        return 1