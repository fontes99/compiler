class ConsTable:

    def __init__(self):
        self.table_cons = {}
        self.table_func = {}
        self.tipinhos = ["int", "bool", "string"]


    def setCons(self, cons):
        self.table_cons[cons] = {'value' : None, 'type' : None}

    def setFunc(self, name):
            self.table_func[name] = {'content' : None, 'return_type' : None}


    def getConsValue(self, cons):
        return self.table_cons[cons]['value']

    def getConsType(self, cons):
        return self.table_cons[cons]['type']

    def getFuncContent(self, name):
        return self.table_func[name]['content']

    def getFuncReturnType(self, name):
        return self.table_func[name]['return_type']


    def setConsValue(self, cons, value):

        if (type(value) == str and self.getConsType(cons) != 'string') or (type(value) == int and self.getConsType(cons) == 'string') or (type(value) == bool  and self.getConsType(cons) != 'bool'):
            raise ValueError(f"Invalid operation for type {self.getConsType(cons)}")

        try:
            if (self.getConsType(cons) == 'bool' and value != 0) : value = 1
            self.table_cons[cons]['value'] = value
        except:
            raise ValueError(f"Constant {cons} not assigned")
    
    def setConsType(self, cons, tipo):
        if cons in self.table_cons : raise ValueError("Constant already declared")
        self.setCons(cons)
        self.table_cons[cons]['type'] = tipo


    def setFuncContent(self, name, content):
        pass

    def setFuncReturnType(self, name, tipo):
        pass



    def getTable(self, var = 1):
        if var == 1 : return self.table_cons
        elif var == 0 : return self.table_func
        else : raise ValueError("Invalid var value")


global consTable 
consTable = ConsTable()