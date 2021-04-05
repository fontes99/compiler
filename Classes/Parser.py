from .Tokenizer import Tokenizer
from .Token import Token

class Parser:
    def __init__(self):
        self.tokenizer = None

    def parseFactor(self):

        if self.tokenizer.actual.tipo == 'INT':
            tmp = self.tokenizer.actual.value
            self.tokenizer.selectNext()
            return tmp

        if self.tokenizer.actual.tipo == 'SUM' or self.tokenizer.actual.tipo == 'SUB':
            tmp = self.tokenizer.actual.value
            self.tokenizer.selectNext()
            return tmp * self.parseFactor()

        else:
            raise ValueError


    def parseTerm(self):

        res = self.parseFactor()

        while self.tokenizer.actual.tipo == 'DIV' or self.tokenizer.actual.tipo == 'MULT':
            
            if self.tokenizer.actual.tipo == 'DIV':
                self.tokenizer.selectNext()
                res /= self.parseFactor()
            
            elif self.tokenizer.actual.tipo == 'MULT':
                self.tokenizer.selectNext()
                res *= self.parseFactor()
            
            else: raise ValueError
            
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
        self.tokenizer.selectNext()
        return self.parseExpression()

