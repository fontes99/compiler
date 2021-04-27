from .Token import Token

class Tokenizer:

    def __init__(self, origin, position, actual):
        self.origin = origin
        self.position = position
        self.actual = actual
        self.balance = 0

    def selectNext(self):
        
        char = lambda : self.origin[self.position]

        while self.position < len(self.origin) and (char() == ' ' or char() == '\n'):
            self.position += 1

        if self.position == len(self.origin):
            self.actual = Token('EOF', '"')
            if self.balance != 0: raise ValueError
            return

        elif char() == '/':
            self.actual = Token('DIV', char())
            self.position += 1

        elif char() == '*':
            self.actual = Token('MULT', char())
            self.position += 1
        
        elif char() == '+':
            self.actual = Token('SUM', 1)
            self.position += 1

        elif char() == '-':
            self.actual = Token('SUB', -1)
            self.position += 1
            
        elif char() == '(':
            self.actual = Token('OPN', '(')
            self.position += 1
            self.balance += 1

        elif char() == ')':
            self.actual = Token('CLS', ')')
            self.position += 1
            self.balance -= 1

            if self.balance < 0:
                raise ValueError

        elif char().isalpha():
            var_name = char()
            self.position += 1
            while char().isalpha() or char().isnumeric() or char() == "_":
                var_name += char()
                self.position += 1

            self.actual = Token('cons', var_name)

        elif char() == "=":
            self.actual = Token('atrib', '=')
            self.position += 1

        elif char() == ";":
            self.actual = Token('end_line', ";")
            self.position += 1

        else: 
            if self.position > 0 and self.actual.tipo == 'INT': raise ValueError

            val = ""

            while(self.position < len(self.origin) and char().isnumeric()):
                val += char()
                self.position += 1

            self.actual = Token('INT', int(val))


        # print(self.actual.tipo, self.actual.value)
        # print(self.position, len(self.origin))