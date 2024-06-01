# Write a function to remove a given word from a list and strip it at the same time

def remove_and_split(string,word):
    newStr = string.replace(word, "")
    # return newStr.split() -> ['is', 'a', 'good']
    return newStr.strip() # is a good

this = " Prag is a good "
n = remove_and_split(this, "Prag")
print(n)