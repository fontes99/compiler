from .Tokenizer import Tokenizer
from .Token import Token

class Parser:
    def __init__(self):
        self.tokenizer = None

    def parseFactor(self):
        self.tokenizer.selectNext()

        if self.tokenizer.actual.tipo == 'INT':
            return self.tokenizer.actual.value

        if self.tokenizer.actual.tipo == 'SUM' or self.tokenizer.actual.tipo == 'SUB':
            return self.tokenizer.actual.value * self.parseFactor()

        else:
            raise ValueError


    def parseTerm(self):

        res = self.parseFactor()
        self.tokenizer.selectNext()

        while self.tokenizer.actual.tipo == 'DIV' or self.tokenizer.actual.tipo == 'MULT':
            
            if self.tokenizer.actual.tipo == 'DIV':
                res /= self.parseFactor()
            else: raise ValueError
            
            if self.tokenizer.actual.tipo == 'MULT':
                res *= self.parseFactor()
            else: raise ValueError
            
            self.tokenizer.selectNext()


        return res



    def parseExpression(self):

        res = self.parseTerm()

        while self.tokenizer.actual.tipo == 'SUM' or self.tokenizer.actual.tipo == 'SUB':
            
            if self.tokenizer.actual.tipo == 'SUM':
                self.tokenizer.selectNext()


                if self.tokenizer.actual.tipo == 'INT':
                    res += self.parseTerm()
                else: raise ValueError
            
            if self.tokenizer.actual.tipo == 'SUB':
                self.tokenizer.selectNext()

                if self.tokenizer.actual.tipo == 'INT':
                    res -= self.parseTerm()
                else: raise ValueError
            
        return res



    def run(self, code):
        self.tokenizer = Tokenizer(code, 0, Token('INIT', '-'))
        return self.parseExpression()

