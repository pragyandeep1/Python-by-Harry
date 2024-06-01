# Write a program to find the maximum number of numbers in a list using reduce function

l1 = [1,34,55,23,34,68,89,25,58,56,32,92,45]
a = filter(lambda a: a%5==0, l1)
print(list(a))