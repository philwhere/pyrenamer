import os
from pprint import pprint
import re

def showme(directory):
    return pprint(directory)

def removeRegexFromString(regex, string):
    return re.sub(rf"({regex})", "", string)

def formatSlashes(directory):
    directory = "//".join(directory.split("/"))
    directory.replace("\\", "\\\\")
    return directory

def removeStringFromFilenames(query):
    files = os.listdir()
    newfilenames = []
    for filename in files:
        if bool(re.search(query, filename)):
            newfilenames.append(removeRegexFromString(query, filename))
    pprint(newfilenames)
    allgood = input("Is this correct? [Y / N]\n")
    if allgood == "Y" or allgood == "y":
        for filename in files:
            if bool(re.search(query, filename)):
                os.rename(filename, removeRegexFromString(query, filename))
    else:
        print("Cancelled")

def appendToFilename(query, stringToAppend, appendBefore):
    if appendBefore == "":
        appendBefore = "."
    files = os.listdir()
    newfilenames = []
    for filename in files:
        if bool(re.search(query, filename)) and bool(re.search(appendBefore, filename)):
            indexOfDot = filename.rindex(appendBefore)
            nameAsList = list(filename)
            nameAsList.insert(indexOfDot, stringToAppend)
            newName = "".join(nameAsList)
            newfilenames.append(newName)
            #os.rename(filename, newName)
    pprint(newfilenames)
    allgood = input("Is this correct? [Y / N]\n")
    if allgood == "Y" or allgood == "y":
        for filename in files:
            if bool(re.search(query, filename)) and bool(re.search(appendBefore, filename)):
                indexOfDot = filename.rindex(appendBefore)
                nameAsList = list(filename)
                nameAsList.insert(indexOfDot, stringToAppend)
                newName = "".join(nameAsList)
                os.rename(filename, newName)
    else:
        print("Cancelled")

def replaceCharacters(oldString, newString):
    files = os.listdir()
    newfilenames = []
    for filename in files:
        newfilenames.append(filename.replace(oldString, newString))
    pprint(newfilenames)
    allgood = input("Is this correct? [Y / N]\n")
    if allgood == "Y" or allgood == "y":
        for filename in files:
            if oldString in filename:
                os.rename(filename, filename.replace(oldString, newString))
    else:
        print("Cancelled")

def tryGetDir():
    print("Phil's Renamer\nBecareful that you don't \
end up with 2 files the same name\n---------------------")
    try:
        directory = formatSlashes(input("Enter directory that contains your files\n"))
        os.chdir(directory)
        pprint(os.listdir())
        print()
        foundDirectory = True
    except FileNotFoundError:
        print("You screwed up\n")
        pass

def main():
    pprint(os.listdir())
    desire = input("Do you want to remove, replace or append to filename? [Remove / Replace / Append]: ")
    if desire.lower() == "remove":
        print("You picked remove")
        query = input("Enter filename query (case sensitive)\n")
        removeStringFromFilenames(query)
        print("Done!")
        
    elif desire.lower() == "append":
        print("You picked append")
        query = input("Enter filename query (case sensitive), leave blank for all files\n")
        toAdd = input("What should be appended?\n")
        appendBefore = input("Insert before what string (case sensitive)? Leave blank for end of filename\n")
        appendToFilename(query, toAdd, appendBefore)
        print("Done!")
        
    elif desire.lower() == "replace":
        print("You picked replace")
        query = input("Find what string? (case sensitive)\n")
        newString = input("What should be replaced with?\n")
        replaceCharacters(query, newString)
        print("Done!")
    elif desire.lower() == "exit":
        exit();
        
tryGetDir()
while True:
    main()
