from .Node import Node

class IntVal(Node):

    def evaluate(self):

        print(F"  MOV EBX, {self.value}")