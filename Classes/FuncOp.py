from .Node import Node
from .ConsTable import consTable

class FuncOp(Node):

    def evaluate(self):

        if self.value == 'def':
            consTable.setFuncReturnType(self.func, self.children[0])
            consTable.setFuncContent(self.func, self.children[1])
            consTable.setFuncParams(self.func, self.children[2])

        elif self.value == 'call':
            return consTable.runFunc(self.children[0])

        elif self.value == 'param':
            pass