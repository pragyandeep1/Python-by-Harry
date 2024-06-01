fruits = ['orange', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'banana'] #fruits list
print("\nNumber of Apples = ", fruits.count('apple')) #number of apple = 2
print("\nNumber of tangerines = ", fruits.count('tangerine')) #number of tangerine = 0
print("\nIndex of the first Banana = ", fruits.index('banana')) #index of first banana = 3
print("\nNext Banana starting from index 4: ", fruits.index('banana', 4)) #finding next banana starting from index 4
fruits.reverse() #reversing the list
print("\nReversed List:\n ", fruits)
fruits.append('grapes') #adding grapes at the end of the list
print("\nGrapes being added in the list:\n ", fruits)
fruits.sort() #rearranging the list in ascending order
print("\nList arranged in ascending order:\n ", fruits)
fruits.insert(4, 'pompkin') #inserting pompkin at index 4 in the list
print("\nPompkin is inserted at 4th index.\n ", fruits)
fruits.pop() #deleting the element at the end of the list
print("\nLast element Pear has been removed.\n ", fruits)
fruits.pop(4) #deleting the element at index 4 from the list
print("\nElement present at index 4 is removed.\n ", fruits)
fruits.remove('apple') #deleting the first apple element from the list
print("\nOne Apple removed.\n ", fruits)
fruits.remove('banana') #deleting the first banana element from the list
print("\nOne Banana removed.\n ", fruits)