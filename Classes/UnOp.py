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
            self.children[0].evaluate()
            print("  PUSH EBX")
            print("  CALL print")
            print("  POP EBX")