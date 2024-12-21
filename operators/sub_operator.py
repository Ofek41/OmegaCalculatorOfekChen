from .base_operator import Operator

class Sub(Operator):
    def priority(self):
        return 1
    def position(self):
        return "middle"
    def operate(self, operator1, operator2):
        self.validate(operator1, operator2)
        return operator1 - operator2

    def arity(self):
        return 2