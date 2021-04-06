from .Node import Node

class UnOp(Node):

    def evaluate(self):

            if self.value == 'SUM':
                return self.children[0].evaluate()

            if self.value == 'SUB':
                return -self.children[0].evaluate()