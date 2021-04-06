from .Tokenizer import Tokenizer
from .Token import Token
from .BinOp import BinOp
from .UnOp import UnOp
from .IntVal import IntVal
from .NoOp import NoOp

class Parser:
    def __init__(self):
        self.tokenizer = None

    def parseFactor(self):
        self.tokenizer.selectNext()

        if self.tokenizer.actual.tipo == 'INT':
            tmp = IntVal(self.tokenizer.actual.value, [])
            self.tokenizer.selectNext()
            return tmp

        elif self.tokenizer.actual.tipo == 'SUM' or self.tokenizer.actual.tipo == 'SUB':
            tmp = self.tokenizer.actual.tipo
            return UnOp(tmp, [self.parseFactor()]) 

        elif self.tokenizer.actual.tipo == 'OPN':

            tmp = self.parseExpression()
            self.tokenizer.selectNext()
            
            return tmp

        else:
            raise ValueError(f'{self.tokenizer.actual.tipo}')


    def parseTerm(self):

        res = self.parseFactor()

        while self.tokenizer.actual.tipo == 'DIV' or self.tokenizer.actual.tipo == 'MULT':
            
            if self.tokenizer.actual.tipo == 'DIV' or self.tokenizer.actual.tipo == 'MULT':
                res = BinOp(self.tokenizer.actual.tipo, [res, self.parseFactor()])
            
            else: raise ValueError('b')
            
        return res



    def parseExpression(self):

        res = self.parseTerm()

        while self.tokenizer.actual.tipo == 'SUM' or self.tokenizer.actual.tipo == 'SUB':
            
            if self.tokenizer.actual.tipo == 'SUM' or self.tokenizer.actual.tipo == 'SUB':
                res = BinOp(self.tokenizer.actual.tipo, [res, self.parseTerm()])

            else: raise ValueError('c')
            
        return res



    def run(self, code):
        self.tokenizer = Tokenizer(code, 0, Token('INIT', '-'))
        tree = self.parseExpression()
        return int(tree.evaluate())

