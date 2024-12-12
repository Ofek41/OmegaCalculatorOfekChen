from .base_operator import Operator
class Hashtag(Operator):
    def priority(self):
        return 6

    def position(self):
        return "left"

    def operate(self, op):
        self.validate(op)
        if op<0:
            raise ValueError("Cannot sum digits of a negative number.")
        str_number = str(op)
        str_number = str_number.replace('.', '')
        sum_digits = 0
        for digit in str_number:
            sum_digits+=int(digit)
        return sum_digits