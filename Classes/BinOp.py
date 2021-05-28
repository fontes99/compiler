from .Node import Node
from .ConsTable import consTable

class BinOp(Node):

    def start_binop(self):

        self.children[0].evaluate()
        print("  PUSH EBX")
        self.children[1].evaluate()
        print("  POP EAX")

        # self.children[0] is in EAX 
        # self.children[1] is in EBX 

    def evaluate(self):

        if self.value == 'SUM':

            self.start_binop()
            print("  ADD EAX, EBX") 
            print("  MOV EBX, EAX")

        if self.value == 'SUB':

            self.start_binop()
            print("  SUB EAX, EBX") 
            print("  MOV EBX, EAX")

        if self.value == 'MULT':

            self.start_binop()
            print("  MUL EBX")
            print("  MOV EDX, EBX")

        if self.value == 'DIV':

            self.start_binop()
            print("  MOV EDX, 0")
            print("  DIV EBX")
            print("  MOV EBX, EAX")

        if self.value == 'EQL':

            print("")

            # if type(self.children[0].evaluate()) != type(self.children[1].evaluate()) : raise ValueError(f"Invalid operation between {type(self.children[0].evaluate())} and {type(self.children[1].evaluate())}")
            # return self.children[0].evaluate() == self.children[1].evaluate()

        if self.value == 'AND':

            print("")

            # if type(self.children[0].evaluate()) != type(self.children[1].evaluate()) : raise ValueError(f"Invalid operation between {type(self.children[0].evaluate())} and {type(self.children[1].evaluate())}")
            # return self.children[0].evaluate() and self.children[1].evaluate()

        if self.value == 'OR':
            
            print("")

            # if type(self.children[0].evaluate()) != type(self.children[1].evaluate()) : raise ValueError(f"Invalid operation between {type(self.children[0].evaluate())} and {type(self.children[1].evaluate())}")
            # return self.children[0].evaluate() or self.children[1].evaluate()

        if self.value == 'GRT':

            print("")

            # if type(self.children[0].evaluate()) != type(self.children[1].evaluate()) : raise ValueError(f"Invalid operation between {type(self.children[0].evaluate())} and {type(self.children[1].evaluate())}")
            # return self.children[0].evaluate() > self.children[1].evaluate()

        if self.value == 'LSS':

            print("")

            # if type(self.children[0].evaluate()) != type(self.children[1].evaluate()) : raise ValueError(f"Invalid operation between {type(self.children[0].evaluate())} and {type(self.children[1].evaluate())}")
            # return self.children[0].evaluate() < self.children[1].evaluate()

        if self.value == 'atrib':

            consTable.setConsValue(self.children[0], self.children[1])

        if self.value == 'while':

            print("")

            # while  self.children[0].evaluate():
            #      self.children[1].evaluate()