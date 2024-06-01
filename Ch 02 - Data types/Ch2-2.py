a = 3
b = 4

print("Arithmetic Operators")
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("\nAssignment Operators")
a += 2
print("a += 2")
print(a)
a -= 2
print("a -= 2")
print(a)
a *= 2
print("a *= 2")
print(a)
a /= 2
print("a /= 2")
print(a)

a += 12
a -= 12
a *= 12
a /= 12
print('New Value = ', a)

print("\nComparison Operators")
b = (14>=7)
c = (14<=7)
d = (14==7)
e = (14!=7)
print(b, c, d, e)

print("\nLogical Operators")
b1 = True
b2 = False
print("Value of Bool1 and Bool2 = ", (b1 and b2))
print("Value of Bool1 or Bool2 = ", (b1 or b2))
print("Value of not Bool2 = ", (not b2))
