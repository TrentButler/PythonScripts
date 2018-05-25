import os

#INPUT THE REPOSITORY YOU WOULD LIKE TO CLONE
#FORMAT = "https://github.com/UserName/RepositoryName"

#IF REPO ALREADY EXISTS, DELETE THE DIRECTORY, AND RE-CLONE

print "INPUT THE REPOSITORY YOU WOULD LIKE TO CLONE"
print "FORMAT = https://github.com/UserName/RepositoryName"

rawRepository = raw_input()

stringRepo = rawRepository
rawDirName = ""
directoryName = ""

for x in range(len(stringRepo), 0, -1):
    if rawRepository[x-1] == '/': #ITERATE UNTIL '/'
        break
    rawDirName += rawRepository[x-1]

for x in range(len(rawDirName), 0, -1):
    directoryName += rawDirName[x-1]
    
currentDirectory = os.getcwd()

def checkDirectory():
    for dir in os.listdir(currentDirectory):
        if dir == directoryName:
            return True

    return False

if(checkDirectory()):
    os.system("rmdir /s " + directoryName) #DELETE THIS DIRECTORY
    
    os.system("git clone " + rawRepository) #RE-CLONE THE REPOSITORY
else:
    os.system("git clone " + rawRepository) #CLONE THE REPOSITORY