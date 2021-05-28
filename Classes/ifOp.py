from .Node import Node
from .ConsTable import consTable

class ifOp(Node):

    def evaluate(self):

        print(f"  IF_{self.value}:")
        
        self.children[0].evaluate()

        print("  CMP EBX, False")
        print(f"  JE ELSE_{self.value}")

        self.children[1].evaluate()
        
        print(f"  JMP EXIT_{self.value}")
        print(f"  ELSE_{self.value}:")

        self.children[2].evaluate()

        print(f"  EXIT_{self.value}:")