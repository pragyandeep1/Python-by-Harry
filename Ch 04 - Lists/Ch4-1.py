a = [1,2, 45,56, 3,6]
print(a)
print("First index: ", a[0])
print("Third index: ", a[2])
print("Fifth index: ", a[4])
a[1] = 98 #change the value in the list
print("Modified Sequence: ", a)

# We can create a list with items of different types
b = ['a', 12, "Prag", True, 9.45]
print("List with different data types-\n", b)

# List Slicing
friends =  ['Prag', 'Tom', 'Dick', 'Saga', 'Kalu', 67]
print("\nList Slicing:\n", friends[0:4])
print(friends[-4:])
print(friends[:4])
print(friends[4:])
print(friends[:-4])

# x = [23, 12, 43, 56, 87, 2]
a.sort() #sorts the list
print("\nSorting the First Homogenous List:\n", a)
a.reverse() #reverses the list
print("\nReversing the List:\n", a)
a.append(74) #adds at the end of the list
print("\nAppending the list:\n", a)
a.insert(1, 437) #inserts into list
print("\nInserting an element at index 1:\n", a)
a.pop(2) #Removes element at index 2
print("\nRemoving index at 2nd Index:\n", a)
a.remove(1) #Removes a particular element from the list
print("\nRemoving 1 from the list:\n", a)
a.remove(437) #Removes a particular element from the list
print("\nRemoving 437 from the list:\n", a)