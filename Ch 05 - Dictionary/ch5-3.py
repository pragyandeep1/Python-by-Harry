a = {1,4,3,5,1,6}
print(a)
print(type(a)) # class set

b = {} # empty dictionary
print(b)
print(type(b)) # class dictionary

# An empty set can be created using below syntax
c = set() # An empty set is created
print(type(c)) # class set

# Adding values to an empty set
c.add(5)
c.add(6)
c.add(6) # adding a value repeatedly doesn't change a set
c.add((5,6,7))
# c.add([5,6,7]) We can't add list here because list is not hashable.
# c.add({5,6,7}) We can't add dictionary here because dictionary is not hashable.
print(c) # A set is a collection of non-repetitive elements.

print(len(c)) # prints the length of set c
c.remove(5) # removes 5 from set c
# c.remove(15) # throws an KeyError while trying to remove 15 which is not present in the set
print(c)
print(c.pop())
print(c)