from .Node import Node
from .ConsTable import consTable

class whileOp(Node):

    def evaluate(self):

        print(f"  LOOP_{self.value}:")
        
        self.children[0].evaluate()

        print("  CMP EBX, False")
        print(f"  JE EXIT_{self.value}")

        self.children[1].evaluate()
        
        print(f"  JMP LOOP_{self.value}")
        print(f"  EXIT_{self.value}:")