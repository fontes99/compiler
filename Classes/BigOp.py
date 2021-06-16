from .Node import Node

class BigOp(Node):

    def evaluate(self):
        for i in self.children:
            x = i.evaluate()
            if i.value == 'return':
                return x