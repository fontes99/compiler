from .Node import Node
from .ConsTable import consTable

class FuncOp(Node):

    def evaluate(self):
        consTable.setFuncReturnType(self.value, self.children[0])
        consTable.setFuncContent(self.value, self.children[1])
        consTable.setFuncParams(self.value, self.children[2])