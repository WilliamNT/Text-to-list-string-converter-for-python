import re
import string

# Asking for string name and our base text
strName = input("What should we call this string? > ").lower()
inputText = input("Please type or paste your text here you wish to convert to a list string. > ").lower()

# Converting our data to a list string
convertedString = re.sub('['+string.punctuation+']', '', inputText).split()
a = set(convertedString)
b = list(a)
outputString = strName + " = " + str(b)

# Generating a file with the name of the string, then creating it's content
with open(strName + ".txt", 'w') as outputTxt:
    outputTxt.write(outputString)
print("Your output is:", outputString)