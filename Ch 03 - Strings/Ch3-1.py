a = '''Prag's   and Prag"s'''
print(a)
b = "Good Morning, "
c = 'Prag'
d = b+c
print(d)
print(d[5])
print(d[1:6])
print(d[1:])
print(d[-4:-1]) #same as [1:4]
print(d[1:4])
print(d[1:6:2])
print(d[0::2])
print(d[:6])
print(len(d))
print(d.endswith("Prag"))
print(d.count('a'))
print(d.capitalize())
print(d.find("Prag"))
print(d.replace("Prag", "Coding Prag"))

story = 'Prag is a good man. \nHe likes fishing.\tBesides this, \\he too \' likes gardening.'
print(story)