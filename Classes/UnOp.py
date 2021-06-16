from Classes.ConsTable import consTable
from .Node import Node

class UnOp(Node):

    def evaluate(self):

        if self.value == 'SUM':
            return self.children[0].evaluate()

        elif self.value == 'SUB':
            return -self.children[0].evaluate()

        elif self.value == 'NEG':
            return not self.children[0].evaluate()

        elif self.value == 'println':
            print(self.children[0].evaluate())
        
        elif self.value == 'return':
            consTable.return_ = self.children[0].evaluate()