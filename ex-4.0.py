#! /usr/bin/python3.6


# Aufgabe 4.0 - 1
def getRangeOfNumbers():
    while True:
        try:
            getRange = int(input("Elemente in Liste (ganze Zahl > 2): "))
            if getRange < 2:
                print ("Das war keine ganze Zahl > 2. Nochmal")
                continue
        except ValueError:
            print ("Das war keine ganze Zahl")
            continue
        else:
            break
    return getRange

def makeIterationAndSum(getRange):
    rangeOfNumbers = [i for i in range(getRange)]
    print ("Erzeugte Liste  : {}".format(rangeOfNumbers))
    
    while True:
        try:
            n = int(input("Zahl n eingeben   (1-{})           : ".format(getRange-1)))
            if n < 1 or n > getRange-1:
                print ("Keine gültige Zahl. Nochmal (1-{})".format(getRange-1))
                continue
            iterationList = []
            for i in rangeOfNumbers[n:]:
                iterationList.extend([i])
            sum = rangeOfNumbers[n] + rangeOfNumbers[n-1]
        except ValueError:
            print ("Das war keine ganze Zahl")
            continue
        else:
            break
            
    print ("Restliste         {}".format(iterationList))
    print ("Summe n + n-1     {} = {} + {}".format(sum, rangeOfNumbers[n], rangeOfNumbers[n-1]))

makeIterationAndSum(getRangeOfNumbers())


# Aufgabe 4.0 - 2
getString = str(input("Beliebigen Text eingeben: "))
#print (getString[1::2])
evenString = [char for char in getString[1::2]]
print ("\'" + "\', \'".join(evenString) + "\'")


# Aufgabe 4.0 - 3
givenString = "Given a string and an int n, remove characters from string from zero upto n and return new string"
integerN = 20

newString = givenString[integerN:]
print (newString)


# Aufgabe 4.0 - 4
reverseNumber = 12324542321

if str(reverseNumber) == str(reverseNumber)[::-1]:
    print (reverseNumber)
else:
    print ("Von hinten wie von vorne - NI.C.H.T")
    

# Aufgabe 4.0 - 5
givenStringEmma = "Emma is a good developer. Emma is also a writer"
print (givenStringEmma.count("Emma"))


# Aufgabe 4.0 - 6
listOne = [(x ** 2 + 5) * 3 for x in range(10)]
listTwo = [x for x in range(100, 110)]

listThree = [x for x in listOne if x % 2 == 1] + [x for x in listTwo if x % 2 == 0]


# Aufgabe 4.0 - 7
with open("ataDedok.dat", "r") as f:
    readData = [line.split() for line in f]

with open("ataDedok-numbered.dat", "w") as f:
    for i in range(len(readData)):
        f.write(str(i) + "\t" + str(" ".join(readData[i])) + "\n")


# Aufgabe 4.0 - 8
def hyphenString(n):
    return ("-" * n)

print (hyphenString(100))


# Aufgabe 4.0 - 9
def countVowels(stringToCount):
    vowels = "aeiou"
    vowelsCount = 0
    for char in stringToCount:
        if char in vowels:
            vowelsCount += 1
    return vowelsCount

print (countVowels("Celebration"))
print (countVowels("Palm"))
print (countVowels("Prediction"))


# Aufgabe 4.0 - 10
def mergeArrays(array1, array2):
    mergedArray = ""
    for i in range(max(len(array1), len(array2))):
        if array1:
            mergedArray += str(array1.pop(0))
        if array2:
            mergedArray += str(array2.pop(0))
    return mergedArray

print (mergeArrays(["a", "b", "c", "d", "e"], [1, 2, 3, 4, 5]))
print (mergeArrays([1, 2, 3], ["a", "b", "c", "d", "e", "f"]))
print (mergeArrays(["f", "d", "w", "t"], [5, 3, 7, 8]))

