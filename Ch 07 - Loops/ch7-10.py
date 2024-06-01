print("Print a Right Triangle by using asterics (While Loop)")
i=0
m = int(input('Enter the value: '))
while i<m:
    print("*"*i)
    i+=1

print("Print an Isosceles Triangle by using asterics (While Loop)")
n = int(input('Enter the value: '))
i = 0
while i<n:
    print(" " * (n-i-1), end=" ")
    print("*" * (2*i+1), end=" ")
    print(" " * (n-i-1))
    i+=1