myDict = {
    'pace': "in a faster manner",
    'prag': "a runner",
    'marks': [1, 5, 29],
    'moremyDict': {"Bill": 'Swimmer'},
    1:2
}

# Dictionary Methods
print(myDict.keys()) # prints keys of myDictionary
print(type(myDict.keys())) # prints type of myDictionary keys
print(list(myDict.keys())) # prints list of myDictionary keys
print(myDict.values()) # prints values of myDictionary
print(type(myDict.values())) # prints type of myDictionary values
print(list(myDict.values())) # prints list of myDictionary values
print(list(myDict.items())) # prints the (keys, values) for all the contents of the dictionary
print("Present Dictionary - ", myDict)
updateDict = {
    "funsukh": 'friend',
    'Rangeela': "pal",
    "Samlala": "friend",
    'prag': 'disco'
}
myDict.update(updateDict) # updates the dictionary by adding key-value pairs from updateDict
print("Dictionary after updation - ", myDict)
print(myDict)
print(myDict.get("prag"))
print(myDict["prag"])

''' Difference between .get and [] syntaxes in the dictionary
print(myDict.get("prag1")) returns none
print(myDict["prag1"]) throws an error cos prag1 is not present in the dictionary'''