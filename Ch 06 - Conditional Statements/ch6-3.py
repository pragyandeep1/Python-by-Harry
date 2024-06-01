a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

if a>b and a>c and a>d:
            print("a is greatest.")
elif b>c:
    if b>d:
        print("b is greatest.")
elif c>d:
    print("c is greatest.")
else:
    print("d is greatest.")
    