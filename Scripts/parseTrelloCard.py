#USE 'urllib2' TO GET THE TRELLO CARD'S JSON VERSION
#PARSE THIS STRING FOR KEYWORDS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#OR LOAD IT INTO A JSON OBJECT
#AND ITERATE THROUGH THAT DICTIONARY
import os
import json
import urllib2
import math

#FUNCTION TO REMOVE ALL UNDESIRED CHARACTERS FROM A STRING
def stripString(s):
    charList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '\n'] #LIST OF ACCEPTABLE CHARACTERS
    returnString = ''

    os.system("cls")
    print s
    os.system("pause")


    if s[0] == '@': #THIS IS A STRING THAT IS UNDESIRED
        return "" #RETURN A EMPTY STRING

    for c in s:
        for CHARACTER in charList: #ITERATE THROUGH THE CHARLIST, IF THE CURRENT CHARACTER FROM THE STRING(s) IS ONE FROM THE CHARLIST,
            if c == CHARACTER:
                returnString += c #ADD THE CHARACTER TO RETURNSTRING

    if len(returnString) < 9: #IF RETURN STRING HAS LESS THAN 9 CHARACTERS, RETURN A EMPTY STRING
        return ""

    if len(returnString) > 9: #TRIM THE END OF ANY STRING THAT HAS MORE THAN 9 CHARACTERS
        trimmedString = ''
        count = 1
        for char in returnString:
            if(count > 9):
                return trimmedString
            trimmedString += char
            count += 1

    return returnString

#FUNCTION TO RETURN A TUPLE REPRENSATION OF CHANGE IN TWO DIFFERENT TIMES (HOURS, MINUTES)
def calculateHours_24(s):
    hours1 = ""
    minutes1 = ""
    hours2 = ""
    minutes2 = ""

    if len(s) < 9:
        
        #print str(s)
        #os.system("pause")

        return
        #print s
        #os.system("pause")
        #return ()

    #BEGIN TIME
    hours1 += s[0]
    hours1 += s[1]
    minutes1 += s[2]
    minutes1 += s[3]

    #END TIME
    hours2 += s[5]
    hours2 += s[6]    
    minutes2 += s[7]
    minutes2 += s[8]


    #os.system("pause")

    #CONVERT THE STRINGS INTO A INTEGERS
    hour1_INT = int(hours1)
    hour2_INT = int(hours2)
    minute1_INT = int(minutes1)
    minute2_INT = int(minutes2)

    dHour = math.fabs(hour1_INT - hour2_INT)
    dMinute = math.fabs(minute1_INT - minute2_INT)

    #os.system("cls")
    #print(hour1_INT, hour2_INT, minute1_INT, minute2_INT)
    #print (dHour, dMinute)
    #os.system("pause")
    
    #return (dHour, dMinute)
    return


#LOAD THE .JSON VERSION OF A TRELLO CARD
cardURL = urllib2.urlopen('https://trello.com/c/G7HhEYxC/4-trent-butler.json')

#DUMP THE JSON TO A STRING REPRESENTATION
rawJSON = cardURL.read()

#CONVERT THE STRING REPRESENTATION OF THE JSON OBJECT TO A DICTIONARY
cardDictionary = json.loads(rawJSON)

#DUMP THE ACTIONS TO A FILE NAMED 'CARDACTIONS'
#ADD A NEW LINE BETWEEN EACH ACTION

cardActions = cardDictionary['actions']

cardActionsFile = open('cardActions.txt', 'w+')

for _Dictionary in cardActions:
    if _Dictionary.has_key('data'):        
        DataDictionary = _Dictionary['data']

        if DataDictionary.has_key('text'):
            
            #PARSE THIS STRING FOR THE TIME
            comment = DataDictionary['text'] #THIS IS THE COMMENT FROM THE CARD, MAY CONTAIN MORE THAN ONE TIMESTAMP
            #NEEDS WORK, MAKE SURE YOU ARE GETTING ALL THE TIMESTAMPS FROM EACH CARD COMMENT

            processTimeStamp = stripString(comment) #CONVERT THE COMMENT INTO A FORMATED TIMESTAMP STRING
            #processTimeStamp = comment

            cardActionsFile.write(processTimeStamp)
            cardActionsFile.write('\n')
            
            #FUNCTION TO PARSE A STRING FOR NUMBERS IN A SPECIFIC FORMAT

            #print calculateHours_24(processTimeStamp)
            #calculateHours_24(processTimeStamp)

            #WRITE THE TOTAL CLOCK HOURS TO A FILE FOR LATE USE
            #cardActionsFile.write(calculateHours_24(processTimeStamp))
            #cardActionsFile.write('\n')

cardActionsFile.close()
print "END OF SCRIPT"