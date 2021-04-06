from .Node import Node

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