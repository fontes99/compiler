from .Node import Node

class TriOp(Node):

    def evaluate(self):

            if self.value == 'if':
                if self.children[0].evaluate():
                    return self.children[1].evaluate()
                else:
                    return self.children[2].evaluate()