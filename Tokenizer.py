from Token import Token

class Tokenizer:

    def __init__(self, origin, position, actual):
        self.origin = origin
        self.position = position
        self.actual = actual

    def selectNext(self):
    
        val = ""

        while(True):
            if self.origin[self.position].isnumeric():
                val += self.origin[self.position]
                self.position += 1
                if self.position == len(self.origin): break
            else: break

        if self.origin[self.position] == '+':
            self.actual = Token('SUM', self.origin[self.position])

        elif self.origin[self.position] == '-':
            self.actual = Token('SUB', self.origin[self.position])

        elif self.position == len(self.origin):
            self.actual = Token('EOF', '"')

        else: self.actual = Token('INT', int(self.origin[self.position]))

        print(f'({self.actual.value}, {self.actual.tipo})')






