from .Node import Node
from .ConsTable import consTable

class FuncOp(Node):

    def evaluate(self):

        if self.value == 'def':
            consTable.setFuncReturnType(self.func, self.children[0])
            consTable.setFuncContent(self.func, self.children[1])
            consTable.setFuncParams(self.func, self.children[2])

        elif self.value == 'call':
            consTable.runFunc(self.children[0])
            return consTable.return_

        elif self.value == 'param': 
            for i in range(len(self.children[0])):
                consTable.setConsValue(consTable.getParams(self.children[1])[i], self.children[0][i], self.func)

            consTable.runFunc(self.children[1])
            return consTable.return_