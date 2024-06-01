print("Print a Right Triangle by using asterics")
for i in range(4):
    print("*"*(i+1))

print("Print an Isosceles Triangle by using asterics")
n = 3
for i in range(3):
    print(" " * (n-i-1), end=" ")
    print("*" * (2*i+1), end=" ")
    print(" " * (n-i-1))