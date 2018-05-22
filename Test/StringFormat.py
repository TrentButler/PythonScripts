import os

aFile = open('data.txt', 'r+')
dump = open('dump.txt', 'w+')

data = list(aFile)

for line in data:
    convert = line.lower()
    new_convert = convert.replace(" ", "_")
    s = '"{}",'.format(new_convert.strip())
    dump.write(s + "\n")

dump.close()
aFile.close()