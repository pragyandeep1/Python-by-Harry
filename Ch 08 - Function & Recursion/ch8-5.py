# Factorial of a number using recursion
# n! = n * (n-1)!

def factIter(num):
    fact = 1
    for i in range(num):
        fact*=(i+1)
    print("Factorial of",num,"is",fact)

def factRec(num):
    if num is 0 or num is 1:
        return 1
    else:
        return num * factRec(num-1)

prod = factIter(4)
prod = factRec(5)
print("Factorial of this number is",prod)