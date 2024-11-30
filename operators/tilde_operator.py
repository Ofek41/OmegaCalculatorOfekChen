from base_operator import Operator
class Negative(Operator):
    def priority(self):
        return 6
    def position(self):
        return "left"
    def operate(self, op):
        self.validate(op)
        return -op