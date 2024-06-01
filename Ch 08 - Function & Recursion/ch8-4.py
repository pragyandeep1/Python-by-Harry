# n! = n * (n-1) * ... * 2 * 1 [Factorial of a number]
num = int(input("Enter a number: "))
fact = 1
for i in range(num):
    fact*=(i+1)
print(fact)