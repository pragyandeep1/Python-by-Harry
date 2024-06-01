myDict = {
    'balak': 'boy',
    'paani': 'water',
    'pankha': 'fan'
}
print("Options: ", myDict.keys())
a = input("Enter an Odia word: ")
print("The meaning of the word is ", myDict.get(a)) #doesn't throw error if key is absent