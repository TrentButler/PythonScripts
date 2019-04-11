#Create a function 'A' that will validate expected output of a tuple 'B' in the form (function, args).
#The expected output 'C' will be given to 'A' to validate testing

#I WANTED THE FUNCTIONALITY OF JUST ADDING ARGUMENTS IN THE TUPLE SIMILAR TO HOW WE WOULD USE THE 'params' OPERATOR IN C#
#public void doIt(params object[] args);
def _Args(*args):
    return list(args)

#NOT SURE WHAT THE FUNCTION 'function' WAS SUPPOSED TO DO SO I JUST KICK OUT A STRING FROM ALL OF THE ARGUMENTS
def Function(Args):
    myString = ""
    for x in Args:
        myString += str(x)
    return myString

#I THINK THIS LOOKS COOL, DONT KNOW IF ITS RIGHT AS FAR AS VALIDATING THE FUNCTION
#RETURN WHATEVER THE FUNCTION KICKS OUT WITH THESE ARGUMENTS
def Validate(Tuple):
    return Tuple[0](Tuple[1])

#MAKE A TUPLE TO BE 'VALIDATED'
myTuple = (Function, _Args(0, "stuff", "foobar", "hello ", "world", "i dont think this is right but its like past 12 in the morning and I have work at 8"))

#IM TIRED, JUST PRINT IT
print(Validate(myTuple))