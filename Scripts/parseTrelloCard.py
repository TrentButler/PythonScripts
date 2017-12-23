import os
import json
import urllib2
import math

#USE 'urllib2' TO GET THE TRELLO CARD'S JSON VERSION
#PARSE THIS STRING FOR KEYWORDS
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#OR LOAD IT INTO A JSON OBJECT
#AND ITERATE THROUGH THAT DICTIONARY

#FUNCTION TO REMOVE ALL UNDESIRED CHARACTERS FROM A STRING
def stripString(s):
    charList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '\n'] #LIST OF ACCEPTABLE CHARACTERS
    returnString = ''

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
        return (0.0, 0.0)

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
    
    return (dHour, dMinute)


cardURL = urllib2.urlopen('https://trello.com/c/G7HhEYxC/4-trent-butler.json') #LOAD THE .JSON VERSION OF A TRELLO CARD

#DUMP THE JSON TO A STRING REPRESENTATION/FILE
rawJSON = cardURL.read()
rawJSONFile = open('rawJSON.txt', 'w+')
rawJSONFile.write(rawJSON)
rawJSONFile.close() #CLOSE THE OPEN FILE

cardDictionary = json.loads(rawJSON) #CONVERT THE STRING REPRESENTATION OF THE JSON OBJECT TO A DICTIONARY

cardActions = cardDictionary['actions'] #RETRIEVE THE LIST OF ACTIONS FROM THIS CARD

cardCommentDump = open('allComments.txt', 'w+')

for _Dictionary in cardActions:
    if _Dictionary.has_key('data'):        
        DataDictionary = _Dictionary['data']

        if DataDictionary.has_key('text'):
            
            #PARSE THIS STRING FOR THE TIME
            RAWcomment = DataDictionary['text'] #THIS IS THE COMMENT FROM THE CARD, MAY CONTAIN MORE THAN ONE TIMESTAMP            

            cardCommentDump.write(RAWcomment) #DUMP ALL COMMENTS TO A FILE,
            cardCommentDump.write('\n') #SEPERATED BY A NEW LINE

cardCommentDump.close() #CLOSE THE OPEN FILE
print "DUMPED ALL COMMENTS TO: (allComments.txt)"

allComments = open('allComments.txt', 'r')
comments = list(allComments) #STORE ALL THE COMMENTS IN A LIST
allComments.close() #CLOSE THE OPEN FILE

commentsWithCalcTime = open('formattedTimestamps.txt', 'w+')
allTimeStamps = open('allTimeStamps.txt', 'w+')

totalTime = [] #LIST OF CONVERTED TIMESTAMPS

for comment in comments:
    processTimeStamp = stripString(comment) #CONVERT THE COMMENT INTO A FORMATED TIMESTAMP STRING
    allTimeStamps.write(processTimeStamp)
    allTimeStamps.write('\n')

    calculatedTime = calculateHours_24(processTimeStamp) #CONVERT THE FORMATED TIMESTAMP STRING INTO A TUPLE REPRESENTING CHANGE IN TIME (HOURS, MINUTES)
    totalTime.append(calculatedTime) #STORE EACH CHANGE IN TIME IN A LIST

    #FORMAT AND WRITE THE TOTAL CLOCK HOURS TO A FILE
    commentsWithCalcTime.write(comment)
    commentsWithCalcTime.write('\n')
    commentsWithCalcTime.write("CALCULATED TIME " + str(calculatedTime))
    commentsWithCalcTime.write('\n')
    commentsWithCalcTime.write('\n')

commentsWithCalcTime.close() #CLOSE THE OPEN FILE
print "DUMPED FORMATTED TIMESTAMPS TO: (formattedTimestamps.txt)"

hours = 0
RAWminutes = 0
minutes = 0

#ADD UP ALL THE HOURS AND MINUTES FROM THE CONVERSIONSS
for time in totalTime:
    hours += time[0]
    RAWminutes += time[1]

if RAWminutes > 60:
    convertedMinutes = divmod(RAWminutes, 60)
    hours += convertedMinutes[0] #ADD THE EXCESS HOURS TO 'hours'
    minutes = convertedMinutes[1] #ASSIGN 'minutes' THE REMAINDER MINUTES
    print "TOTAL TIME: " + str(hours) + " HOURS, " + str(minutes) + " MINUTES"
    
else:
    print "TOTAL TIME: " + str(hours) + " HOURS, " + str(RAWminutes) + " MINUTES"