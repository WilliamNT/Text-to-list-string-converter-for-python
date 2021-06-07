import re
import string

strName = input("What should we call this string? > ")
inputText = input("Please type or paste your text here you wish to convert to a list string. > ")

convertedString = re.sub('['+string.punctuation+']', '', inputText).split()
a = set(convertedString)
b = list(a)
outputString = strName + " = " + str(b)

with open(strName + ".txt", 'w') as outputTxt:
    outputTxt.write(outputString)
print("Your output is:", outputString)