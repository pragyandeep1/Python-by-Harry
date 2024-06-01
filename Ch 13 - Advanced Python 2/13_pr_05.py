# Write a program to find the maximum of numbers in a list using reduce function

from functools import reduce
l0 = [3,56,24,28,45]
a = reduce(max,l0)
print(a)