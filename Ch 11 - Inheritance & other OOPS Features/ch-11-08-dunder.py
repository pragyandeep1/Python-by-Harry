# Dunder Methods

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

    def __str__(self):
        return f'Decimal Number: {self.num}'

    def __len__(self):
        if self.num>100:
            return 3
        elif self.num>10 and self.num<100:
            return 2
        else:
            return 1

m = int(input("Enter a decimal number: "))
n = Number(m)
print(n)
print(f'Length of the number is {len(n)}')