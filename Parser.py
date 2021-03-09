from Tokenizer import Tokenizer

class Parser:
    def __init__(self):
        self.tokenizer = None

    def parseExpression(self):

        if self.tokenizer.actual.tipo == 'INT':
            res = self.tokenizer.actual.value
            self.tokenizer.selectNext()

            while self.tokenizer.actual.tipo == 'SUM' or self.tokenizer.actual.tipo == 'SUB':
                
                if self.tokenizer.actual.tipo == 'SUM':
                    self.tokenizer.selectNext()

                    if self.tokenizer.actual.tipo == 'INT':
                        res += self.tokenizer.actual.value
                    else: raise ValueError
                
                if self.tokenizer.actual.tipo == 'SUB':
                    self.tokenizer.selectNext()

                    if self.tokenizer.actual.tipo == 'INT':
                        res -= self.tokenizer.actual.value
                    else: raise ValueError
                
                self.tokenizer.selectNext()

            return res

        else: raise ValueError


    def run(self, code):
        self.tokenizer = Tokenizer(code, 0, None)
        return self.parseExpression()

