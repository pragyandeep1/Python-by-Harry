# Create a class Calculator which is capable of finding square, cube, square root and cube root of a number

class Calculator:
    def __init__(self,num):
        self.no = num
    
    def square(self):
        print(f"Suare of {self.no} is {self.no**2}")

    def cube(self):
        print(f"Cube of {self.no} is {self.no**3}")

    def squareroot(self):
        print(f"Square root of {self.no} is {self.no** 0.5}")

    def cuberoot(self):
        print(f"Cube root of {self.no} is {self.no ** (1/3)}")

a = int(input("Enter a number: "))
b = Calculator(a)
b.square()
b.cube()
b.squareroot()
b.cuberoot()