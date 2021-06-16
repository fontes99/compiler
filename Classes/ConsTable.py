class ConsTable:

    def __init__(self):
        self.return_ = {'value' : None, 'type' : None}
        self.table_func = {}
        self.tipinhos = ["int", "bool", "string"]


    def setCons(self, cons, name):
        self.table_func[name]['params'][cons] = {'value' : None, 'type' : None}

    def setFunc(self, name):
        self.table_func[name] = {'content' : None, 'return_type' : None, 'params' : {}}


    def getConsValue(self, cons, name):
        return self.table_func[name]['params'][cons]['value']

    def getConsType(self, cons, name):
        return self.table_func[name]['params'][cons]['type']

    def getFuncContent(self, name):
        return self.table_func[name]['content']

    def getFuncParams(self, name):
        return self.table_func[name]['params']

    def getFuncReturnType(self, name):
        return self.table_func[name]['return_type']


    def setConsValue(self, cons, value, name):

        if (type(value) == str and self.getConsType(cons, name) != 'string') or (type(value) == int and self.getConsType(cons, name) == 'string') or (type(value) == bool  and self.getConsType(cons, name) != 'bool'):
            raise ValueError(f"Invalid operation for type {self.getConsType(cons, name)}")

        try:
            if (self.getConsType(cons, name) == 'bool' and value != 0) : value = 1
            self.table_func[name]['params'][cons]['value'] = value
        except:
            raise ValueError(f"Constant {cons} not assigned")
    
    def setConsType(self, cons, tipo, name):
        if cons in self.table_func[name]['params'] : raise ValueError("Constant already declared")
        self.setCons(cons, name)
        self.table_func[name]['params'][cons]['type'] = tipo


    def setFuncContent(self, name, content):
        self.table_func[name]['content'] = content

    def setFuncReturnType(self, name, tipo):
        if name in self.table_func : raise ValueError("Function already exists")
        self.setFunc(name)
        self.table_func[name]['return_type'] = tipo

    def setFuncParams(self, name, params):
        self.table_func[name]['params'] = params
        

    def runFunc(self, name):
        return self.getFuncContent(name).evaluate()


    def getTable(self):
        return self.table_func

    def getParams(self, name):
        return list(self.table_func[name]['params'])


global consTable 
consTable = ConsTable()