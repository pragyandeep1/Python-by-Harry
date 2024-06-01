# Write a program to display a/b where a and b are integers. If b = 0, display infinite by handling ZeroDivisionError

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

try:
    print(a/b)

except:
    print('Infinite')