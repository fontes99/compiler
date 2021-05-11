from .Node import Node
from .ConsTable import consTable

class BinOp(Node):

    def evaluate(self):

        if self.value == 'SUM':
            return self.children[0].evaluate() + self.children[1].evaluate()

        if self.value == 'SUB':
            return self.children[0].evaluate() - self.children[1].evaluate()
        
        if self.value == 'MULT':
            return self.children[0].evaluate() * self.children[1].evaluate()
        
        if self.value == 'DIV':
            return int(self.children[0].evaluate() / self.children[1].evaluate())
        
        if self.value == 'EQL':
            return self.children[0].evaluate() == self.children[1].evaluate()

        if self.value == 'AND':
            return self.children[0].evaluate() and self.children[1].evaluate()

        if self.value == 'OR':
            return self.children[0].evaluate() or self.children[1].evaluate()

        if self.value == 'GRT':
            return self.children[0].evaluate() > self.children[1].evaluate()

        if self.value == 'LSS':
            return self.children[0].evaluate() < self.children[1].evaluate()

        if self.value == 'atrib':
            consTable.setCons(self.children[0], self.children[1].evaluate())

        if self.value == 'while':
            while  self.children[0].evaluate():
                 self.children[1].evaluate()