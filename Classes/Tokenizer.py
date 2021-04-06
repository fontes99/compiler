from .Token import Token

class Tokenizer:

    def __init__(self, origin, position, actual):
        self.origin = origin
        self.position = position
        self.actual = actual
        self.balance = 0

    def selectNext(self):

        while self.position < len(self.origin) and self.origin[self.position] == ' ':
            self.position += 1

        if self.position == len(self.origin):
            self.actual = Token('EOF', '"')
            if self.balance != 0: raise ValueError
            return

        elif self.origin[self.position] == '/':
            self.actual = Token('DIV', self.origin[self.position])
            self.position += 1

        elif self.origin[self.position] == '*':
            self.actual = Token('MULT', self.origin[self.position])
            self.position += 1
        
        elif self.origin[self.position] == '+':
            self.actual = Token('SUM', 1)
            self.position += 1

        elif self.origin[self.position] == '-':
            self.actual = Token('SUB', -1)
            self.position += 1
            
        elif self.origin[self.position] == '(':
            self.actual = Token('OPN', '(')
            self.position += 1
            self.balance += 1

        elif self.origin[self.position] == ')':
            self.actual = Token('CLS', ')')
            self.position += 1
            self.balance -= 1

            if self.balance < 0:
                raise ValueError


        else: 
            if self.position > 0 and self.actual.tipo == 'INT': raise ValueError

            val = ""

            while(self.position < len(self.origin) and self.origin[self.position].isnumeric()):
                val += self.origin[self.position]
                self.position += 1

            self.actual = Token('INT', int(val))


        # print(self.actual.tipo, self.actual.value)
        # print(self.position, len(self.origin))