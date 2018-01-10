import os

class aObject(object):
    def __init__(self, expression):
        self.data = []
        self.expression = expression.lower()
        self.pairs = []
        self.variables = []
        self.clauses = []

    def GetVariables(self):
        #FIND THE VARIABLES FROM 'expression'
        #NO DUPLICATES
        #TESTCASE = (A + B) * (B + C) * (!D + E + F)
        rawVariables = []
        
        for char in self.expression:
            if(ord(char) >= 97 and ord(char) <= 122):
                #VALID VARIABLE
                rawVariables.append(char)


        self.variables = list(set(rawVariables)) #REMOVES DUPLICATES
        return self.variables
    
    def GetPairs(self):
        #FIND THE PAIRS FROM 'expression'
        #NO DUPLICATES
        #TESTCASE = (A + B) * (B + C) * (!D + E + F)
        rawPairs = self.GetVariables()
        pairs = []
        for var in rawPairs:
            pair = (str(var), None)
            pairs.append(pair)
        
        self.pairs = pairs
        return self.pairs

    #def GetClause(self):
        

def main():
    testObject = aObject('(A + B) * (B + A) * (!D + E + F)')
    print 'expression: ' + testObject.expression
    print 'variables: ' + str(testObject.GetVariables())
    print 'pairs:' + str(testObject.GetPairs())


main()