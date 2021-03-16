from Classes.Parser import Parser
from Classes.PrePro import PrePro
import sys

expression = sys.argv[1]

parser = Parser()
prepro = PrePro()

print(parser.run(prepro.filter(expression)))