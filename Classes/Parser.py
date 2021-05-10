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

        elif self.token_tipo() == 'SUM' or self.token_tipo() == 'SUB':
            tmp = self.token_tipo()
            return UnOp(tmp, [self.parseFactor()]) 

        elif self.token_tipo() == 'OPN':

            tmp = self.parseExpression()
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
            
            tmp = IntVal(int(input("input: ")), [])
            self.tokenizer.selectNext()
            return tmp

        else:
            raise ValueError(f'{self.token_tipo()}')


    def parseTerm(self):

        res = self.parseFactor()

        while self.token_tipo() == 'DIV' or self.token_tipo() == 'MULT':
            
            if self.token_tipo() == 'DIV' or self.token_tipo() == 'MULT':
                res = BinOp(self.token_tipo(), [res, self.parseFactor()])
            
            else: raise ValueError('b')
            
        return res



    def parseExpression(self):

        res = self.parseTerm()

        while self.token_tipo() == 'SUM' or self.token_tipo() == 'SUB':
            
            if self.token_tipo() == 'SUM' or self.token_tipo() == 'SUB':
                res = BinOp(self.token_tipo(), [res, self.parseTerm()])

            else: raise ValueError('c')
            
        return res


    def println(self):
        self.tokenizer.selectNext()

        if self.token_tipo() != 'OPN' : raise ValueError('não abriu parenteses no println')

        tree = self.parseExpression()

        print(tree.evaluate())

        self.tokenizer.selectNext()

    def cons(self):
        cons_name = self.token_valor()

        self.tokenizer.selectNext()

        if self.token_tipo() != 'atrib' : raise ValueError('não tem = depois de variavel')

        tree = self.parseExpression()

        self.cons_table[cons_name] = tree.evaluate()

    def command(self):

        if self.token_tipo() == 'builtin':

            if self.token_valor() == 'println':

                self.println()

        elif self.token_tipo() == 'cons':
            self.cons()

        elif self.token_tipo() == 'end_line':
            pass

        else : raise ValueError("Syntax error :(")



    def run(self, code):
        self.tokenizer = Tokenizer(code, 0, Token('INIT', '-'))
        self.tokenizer.selectNext()

        while self.token_tipo() != 'EOF':
            self.command()
            if self.token_tipo() != 'end_line' : raise ValueError('não tem ;')
            self.tokenizer.selectNext()