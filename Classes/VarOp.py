from .Node import Node
from .ConsTable import consTable

class VarOp(Node):

    def evaluate(self):
        return consTable.getCons(self.value)