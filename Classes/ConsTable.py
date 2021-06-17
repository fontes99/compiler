class ConsTable:

    def __init__(self):
        self.return_ = {'value' : None, 'type' : None}
        self.table_func = {}
        self.tipinhos = ["int", "bool", "string"]


    def setCons(self, cons, function, table):
        self.table_func[function][table][cons] = {'value' : None, 'type' : None}

    def setFunc(self, function):
        self.table_func[function] = {'content' : None, 'return_type' : None, 'params' : {}, 'atrib' : {}}


    def getConsValue(self, cons, function, table):
        return self.table_func[function][table][cons]['value']

    def getConsType(self, cons, function, table):
        # print(self.table_func)
        return self.table_func[function][table][cons]['type']

    def getFuncContent(self, function):
        return self.table_func[function]['content']

    def getFuncParams(self, function):
        return self.table_func[function]['params']

    def getFuncReturnType(self, function):
        return self.table_func[function]['return_type']


    def setConsValue(self, cons, value, function, table):

        if (type(value) == str and self.getConsType(cons, function, table) != 'string') or (type(value) == int and self.getConsType(cons, function, table) == 'string') or (type(value) == bool  and self.getConsType(cons, function, table) == 'string'):
            raise ValueError(f"Invalid operation for type {self.getConsType(cons, function, table)} {cons} and {type(value)} {value}")

        try:
            if (self.getConsType(cons, function, table) == 'bool' and value != 0) : value = 1
            elif (self.getConsType(cons, function, table) == 'int' and value == False) : value = 0
            elif (self.getConsType(cons, function, table) == 'int' and value == True) : value = 1
            self.table_func[function][table][cons]['value'] = value
        except:
            raise ValueError(f"Constant {cons} not assigned")
    
    def setConsType(self, cons, tipo, function, table):
        if cons in self.table_func[function][table] : raise ValueError(f"Constant {cons} already declared")
        self.setCons(cons, function, table)
        self.table_func[function][table][cons]['type'] = tipo


    def setFuncContent(self, function, content):
        self.table_func[function]['content'] = content

    def setFuncReturnType(self, function, tipo):
        if function in self.table_func : raise ValueError("Function already exists")
        self.setFunc(function)
        if tipo == 'string' : self.table_func[function]['return_type'] = str
        if tipo == 'int' : self.table_func[function]['return_type'] = int
        if tipo == 'bool' : self.table_func[function]['return_type'] = bool

    def setFuncParams(self, function, params):
        self.table_func[function]['params'] = params
    
    def setFuncAtribs(self, function, atrib):
        self.table_func[function]['atrib'] = atrib

    def removeCons(self, function, qt0, qt1):
        prms = self.getParams(function)

        for i in range(qt0, qt1):
            del self.table_func[function]['params'][prms[i]]
        

    def runFunc(self, function):
        self.getFuncContent(function).evaluate()


    def getTable(self):
        return self.table_func

    def getParams(self, function):
        return list(self.table_func[function]['params'])


global consTable 
consTable = ConsTable()