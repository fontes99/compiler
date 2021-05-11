from .Tokenizer import Tokenizer
from .Token import Token
from .BinOp import BinOp
from .UnOp import UnOp
from .IntVal import IntVal
from .NoOp import NoOp

class Parser:


    def __init__(self):
        self.tokenizer = None
        self.cons_table = {}
        self.token_tipo = lambda : self.tokenizer.actual.tipo
        self.token_valor = lambda : self.tokenizer.actual.value

    def parseFactor(self):
        self.tokenizer.selectNext()

        if self.token_tipo() == 'INT':
            tmp = IntVal(self.token_valor(), [])
            self.tokenizer.selectNext()
            return tmp

        elif self.token_tipo() == 'SUM' or self.token_tipo() == 'SUB' or self.token_tipo() == 'NEG':
            tmp = self.token_tipo()
            return UnOp(tmp, [self.parseFactor()]) 

        elif self.token_tipo() == 'OPN':

            tmp = self.OREXPR()
            self.tokenizer.selectNext()
            
            return tmp

        elif self.token_tipo() == 'cons':
            tmp = IntVal(self.cons_table[self.token_valor()], [])
            self.tokenizer.selectNext()
            return tmp

        elif self.token_valor() == "readln":
            self.tokenizer.selectNext()

            if self.token_tipo() != "OPN" : raise ValueError("sem ( depois de readln")
            self.tokenizer.selectNext()
            
            tmp = IntVal(int(input()), [])
            self.tokenizer.selectNext()
            return tmp

        else:
            raise ValueError(f'{self.token_tipo()}')


    def parseTerm(self):

        res = self.parseFactor()

        while self.token_tipo() == 'DIV' or self.token_tipo() == 'MULT':
            
            if self.token_tipo() == 'DIV' or self.token_tipo() == 'MULT':
                res = BinOp(self.token_tipo(), [res, self.parseFactor()])
            
            else: raise ValueError('not DIV or MULT')
            
        return res



    def parseExpression(self):

        res = self.parseTerm()

        while self.token_tipo() == 'SUM' or self.token_tipo() == 'SUB':
            
            if self.token_tipo() == 'SUM' or self.token_tipo() == 'SUB':
                res = BinOp(self.token_tipo(), [res, self.parseTerm()])

            else: raise ValueError('not SUM or SUB')
            
        return res


    def RELEXPR(self):

        res = self.parseExpression()

        while self.token_tipo() == 'GRT' or self.token_tipo() == 'LSS':
            
            if self.token_tipo() == 'GRT' or self.token_tipo() == 'LSS':
                res = BinOp(self.token_tipo(), [res, self.parseTerm()])

            else: raise ValueError('not GRT or LSS')
            
        return res


    def EQEXPR(self):

        res = self.RELEXPR()

        while self.token_tipo() == 'EQL':
            
            if self.token_tipo() == 'EQL':
                res = BinOp(self.token_tipo(), [res, self.parseTerm()])

            else: raise ValueError('not EQL')
            
        return res


    def ANDEXPR(self):

        res = self.EQEXPR()

        while self.token_tipo() == 'AND':
            
            if self.token_tipo() == 'AND':
                res = BinOp(self.token_tipo(), [res, self.parseTerm()])

            else: raise ValueError('not AND')
            
        return res


    def OREXPR(self):

        res = self.ANDEXPR()

        while self.token_tipo() == 'OR':
            
            if self.token_tipo() == 'OR':
                res = BinOp(self.token_tipo(), [res, self.parseTerm()])

            else: raise ValueError('not OR')
            
        return res


    def println(self):
        self.tokenizer.selectNext()

        if self.token_tipo() != 'OPN' : raise ValueError('não abriu parenteses no println')

        tree = self.OREXPR()

        print(tree.evaluate())

        self.tokenizer.selectNext()

    def identifier(self):
        cons_name = self.token_valor()

        self.tokenizer.selectNext()

        if self.token_tipo() != 'atrib' : raise ValueError(f'não tem = depois de variavel {cons_name}')

        tree = self.OREXPR()

        self.cons_table[cons_name] = tree.evaluate()

    def command(self):

        if self.token_tipo() == 'builtin':

            if self.token_valor() == 'println':
                self.println()
                if self.token_tipo() != 'end_line' : raise ValueError('não tem ;')
                self.tokenizer.selectNext()

        elif self.token_tipo() == 'cons':
            self.identifier()
            if self.token_tipo() != 'end_line' : raise ValueError('não tem ;')
            self.tokenizer.selectNext()

        elif self.token_tipo() == 'end_line':
            self.tokenizer.selectNext()

        elif self.token_tipo() == 'BEG':
            self.block()

        else : raise ValueError("Syntax error :(")


    def block(self):
        if self.token_tipo() != 'BEG' : raise ValueError('bloco não começa com {')
        self.tokenizer.selectNext()

        while self.token_tipo() != 'END':
            self.command()

        self.tokenizer.selectNext()


    def run(self, code):
        self.tokenizer = Tokenizer(code, 0, Token('INIT', '-'))
        self.tokenizer.selectNext()

        while self.token_tipo() != 'EOF':
            self.block()
            