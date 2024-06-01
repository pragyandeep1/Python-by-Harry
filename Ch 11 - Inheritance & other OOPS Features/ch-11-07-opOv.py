# Operator Overloading

class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num1):
        print('Time to add numbers...')
        return self.num + num1.num

    def __mul__(self, num1):
        print('Time to multiply numbers...')
        return self.num * num1.num

    def __sub__(self, num1):
        print('Time to subtract numbers...')
        return self.num - num1.num

n1 = Number(8)
n2 = Number(6)
sum = n1+n2
print(sum)
mul = n1*n2
print(mul)
sub = n1-n2
print(sub)