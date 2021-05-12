class ConsTable:

    def __init__(self, table):
        self.table = table

    def getCons(self, cons):
        return self.table[cons]

    def setCons(self, cons, value):
        self.table[cons] = value

    def getTable(self):
        return self.table

global consTable 
consTable = ConsTable({})