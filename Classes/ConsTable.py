class ConsTable:

    def __init__(self, table):
        self.table = table
        self.tipinhos = ["int", "bool", "string"]
        self.count_variable = 0

    def setCons(self, cons):
        self.table[cons] = {'value' : None, 'type' : None, 'EBP' : 4*self.count_variable}


    def getConsValue(self, cons):
        return self.table[cons]['value']

    def getConsType(self, cons):
        return self.table[cons]['type']

    def setConsValue(self, cons, value):

        if (type(value) == str and self.getConsType(cons) != 'string') or (type(value) == int and self.getConsType(cons) == 'string') or (type(value) == bool  and self.getConsType(cons) != 'bool'):
            raise ValueError(f"Invalid operation for type {self.getConsType(cons)}")

        try:
            self.table[cons]['value'] = value
            print(f"  MOV EBX, {value}")
            print(f"  MOV [EBP-{self.table[cons]['EBP']}], EBX")
        except:
            raise ValueError(f"Constant {cons} not assigned")
    
    def setConsType(self, cons, tipo):
        self.count_variable += 1
        self.setCons(cons)
        self.table[cons]['type'] = tipo
        print("  PUSH DWORD 0")

    def getTable(self):
        return self.table


global consTable 
consTable = ConsTable({})