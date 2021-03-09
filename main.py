from Parser import Parser
import sys

expression = sys.argv[1]

parser = Parser()

print(parser.run(expression))