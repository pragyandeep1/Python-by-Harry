# Write a comprehension to print a list that contains multiplication table of user entered number

num = int(input('Enter number: '))
tab = [num*i  for i in range (1,11)]
print(tab)