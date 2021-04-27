from .Token import Token

class Tokenizer:

    def __init__(self, origin, position, actual):
        self.origin = origin
        self.position = position
        self.actual = actual
        self.balance = 0
        self.builtIns = ["println"]

    def selectNext(self):
        
        def next_():
            self.position += 1

        char = lambda : self.origin[self.position]

        while self.position < len(self.origin) and (char() == ' ' or char() == '\n'):
            next_()

        if self.position == len(self.origin):
            self.actual = Token('EOF', '"')
            if self.balance != 0: raise ValueError
            return

        elif char() == '/':
            self.actual = Token('DIV', char())
            next_()

        elif char() == '*':
            self.actual = Token('MULT', char())
            next_()
        
        elif char() == '+':
            self.actual = Token('SUM', 1)
            next_()

        elif char() == '-':
            self.actual = Token('SUB', -1)
            next_()
            
        elif char() == '(':
            self.actual = Token('OPN', '(')
            self.balance += 1
            next_()

        elif char() == ')':
            self.actual = Token('CLS', ')')
            self.balance -= 1
            next_()

            if self.balance < 0:
                raise ValueError

        elif char().isalpha():
            name = char()
            next_()
            while char().isalpha() or char().isnumeric() or char() == "_":
                name += char()
                next_()

            if name in self.builtIns: self.actual = Token('bultin', name)

            else : self.actual = Token('cons', name)

        elif char() == "=":
            self.actual = Token('atrib', '=')
            next_()

        elif char() == ";":
            self.actual = Token('end_line', ";")
            next_()

        else: 
            if self.position > 0 and self.actual.tipo == 'INT': raise ValueError

            val = ""

            while(self.position < len(self.origin) and char().isnumeric()):
                val += char()
                next_()

            self.actual = Token('INT', int(val))