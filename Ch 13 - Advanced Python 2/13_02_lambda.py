'''def func(a):
    return a+5'''

func = lambda a: a+5
square = lambda x: x*x
sum = lambda a, b, c: a+b+c

x = 5
print(func(x)) # 10
print(sum(x, 1, 3)) # 9
print(square(x)) # 25