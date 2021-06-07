from Classes.ConsTable import ConsTable
from .Tokenizer import Tokenizer
from .Token import Token
from .TriOp import TriOp
from .BinOp import BinOp
from .VarOp import VarOp
from .FuncOp import FuncOp
from .BigOp import BigOp
from .TypeOp import TypeOp
from .UnOp import UnOp
from .IntVal import IntVal
from .StringVal import StringVal
from .NoOp import NoOp

class Parser:

    def __init__(self):
        self.tokenizer = None
        self.token_tipo = lambda : self.tokenizer.actual.tipo
        self.token_valor = lambda : self.tokenizer.actual.value


    def parseFactor(self):
        self.tokenizer.selectNext()

        if self.token_tipo() == 'INT' or self.token_tipo() == 'BOOL':
            tmp = IntVal(self.token_valor(), [])
            self.tokenizer.selectNext()
            return tmp

        elif self.token_tipo() == 'STR':
            tmp = StringVal(self.token_valor(), [])
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
            tmp = VarOp(self.token_valor(), [])
            self.tokenizer.selectNext()
            return tmp

        elif self.token_valor() == "readln":
            self.tokenizer.selectNext()

            if self.token_tipo() != "OPN" : raise ValueError("need ( before readln")
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
        print_valor = self.token_valor()
        self.tokenizer.selectNext()

        if self.token_tipo() != 'OPN' : raise ValueError('need ( before println')

        tree = self.OREXPR()
        self.tokenizer.selectNext()

        return UnOp(print_valor, [tree])

    def identifier(self):
        cons_name = self.token_valor()

        self.tokenizer.selectNext()

        if self.token_tipo() != 'atrib' : raise ValueError(f'need = after variable name {cons_name}')

        tree = self.OREXPR()

        return BinOp('atrib', [str(cons_name), tree])

    def FuncDefBlock(self):
        params = {}
        self.tokenizer.selectNext()

        while self.token_tipo() != 'CLS':

            print(self.token_tipo())
            
            if self.token_tipo() != 'TYP' : raise ValueError("must declare parameter Type")
            tip = self.token_valor()
            self.tokenizer.selectNext()
            
            if self.token_tipo() != 'cons' : raise ValueError("must declare parameter name")
            nam = self.token_valor()
            self.tokenizer.selectNext()

            params[nam] = {'tipo' : tip, 'value' : None}


            if self.token_tipo() != 'SEP' : raise ValueError("must separate params with ','")
        
        self.tokenizer.selectNext()

        cont = self.block()



    def ifEXPR(self):
        self.tokenizer.selectNext()
        if self.token_tipo() != 'OPN' : raise ValueError('need ( before if')

        condition = self.OREXPR()
        
        if type(condition) == StringVal : raise ValueError("can't use string in if statement")

        self.tokenizer.selectNext()

        iftrue = self.command()

        if self.token_valor() == 'else':
            self.tokenizer.selectNext()
            elsee = self.command()

        elif self.token_tipo() == 'END':
            elsee = NoOp('nop', [])

        else: 
            elsee = self.command()
        
        return TriOp('if', [condition, iftrue, elsee])

    def whileEXPR(self):
        self.tokenizer.selectNext()
        if self.token_tipo() != 'OPN' : raise ValueError('need ( before while')

        condition = self.OREXPR()
        self.tokenizer.selectNext()

        instru = self.command()

        return BinOp('while', [condition, instru])
        

    def command(self):

        if self.token_tipo() == 'builtin':

            if self.token_valor() == 'println':
                tree = self.println()
                
                if self.token_tipo() != 'end_line' : raise ValueError('need ;')
                self.tokenizer.selectNext()
                
                return tree

            elif self.token_valor() == 'if':
                return self.ifEXPR()

            elif self.token_valor() == 'while':
                return self.whileEXPR()

            else : raise ValueError("builtin not valid")

        elif self.token_tipo() == 'cons':
            tree = self.identifier()

            if self.token_tipo() != 'end_line' : raise ValueError('need ;')
            self.tokenizer.selectNext()
           
            return tree

        elif self.token_tipo() == 'TYP':
            tipo = self.token_valor()
            self.tokenizer.selectNext()

            if self.token_tipo() != 'cons' : raise ValueError(f"Invalid constant name {self.token_valor()}")
            
            name = self.token_valor()
            self.tokenizer.selectNext()


            if self.token_tipo() == 'end_line' : return TypeOp(tipo, [name])
            elif self.token_tipo() == 'OPN' : return self.FuncDefBlock(tipo, name)


        elif self.token_tipo() == 'end_line':
            self.tokenizer.selectNext()
            return NoOp('pass', [])

        elif self.token_tipo() == 'BEG':
            return self.block()
        
        else : raise ValueError(f"Syntax error : {self.token_tipo()} token {self.tokenizer.tokenPosition}")


    def block(self):
        if self.token_tipo() != 'BEG' : raise ValueError('need { at start of block')
        self.tokenizer.selectNext()

        commands_in_block = []

        while self.token_tipo() != 'END':
            commands_in_block.append(self.command())
        
        self.tokenizer.selectNext()
        return BigOp('block', commands_in_block)


    def run(self, code):
        self.tokenizer = Tokenizer(code, 0, Token('INIT', '-'))
        self.tokenizer.selectNext()

        compiled = self.block()
        compiled.evaluate()

