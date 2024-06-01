a = [3, 45, 23, 56, 32, 21, 50, 53, 24, 52, 59, 22]
'''b = []
for i in a:
    if i % 2 != 0:
        b.append(i)
print(b)'''

# shortcut to write the above
b = [i for i in a if i % 2 is not 0]
print(b) # [3, 45, 23, 21, 53, 59]

s = [3, 5, 12, 24, 57, 39, 43]
t = {i for i in s}
print(t) # {3, 5, 39, 43, 12, 24, 57}