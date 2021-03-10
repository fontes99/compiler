from .Token import Token

class Tokenizer:

    def __init__(self, origin, position, actual):
        self.origin = origin
        self.position = position
        self.actual = actual

    def selectNext(self):

        while self.position < len(self.origin) and self.origin[self.position] == ' ':
            self.position += 1

        if self.position == len(self.origin):
            self.actual = Token('EOF', '"')
            self.position += 1
            return

        elif self.origin[self.position] == '+':
            self.actual = Token('SUM', self.origin[self.position])
            self.position += 1

        elif self.origin[self.position] == '-':
            self.actual = Token('SUB', self.origin[self.position])
            self.position += 1

        else: 
            if self.position > 0 and self.actual.tipo == 'INT': raise ValueError

            val = ""

            while(self.position < len(self.origin) and self.origin[self.position].isnumeric()):
                val += self.origin[self.position]
                self.position += 1

            self.actual = Token('INT', int(val))

