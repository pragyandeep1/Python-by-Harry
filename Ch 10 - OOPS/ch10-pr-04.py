# Add a static method to Q2 and greet the user with 'hello'

class Calculator:
    def __init__(self,num):
        self.no = num

    @staticmethod
    def greet():
        print("Welcome to the best calculator in the world.")
    
    def square(self):
        print(f"Square of {self.no} is {self.no**2}")

    def cube(self):
        print(f"Cube of {self.no} is {self.no**3}")

    def squareroot(self):
        print(f"Square root of {self.no} is {self.no** 0.5}")

    def cuberoot(self):
        print(f"Cube root of {self.no} is {self.no ** (1/3)}")

x = Calculator(0)
x.greet()
a = int(input("Enter a number: "))
b = Calculator(a)
b.square()
b.cube()
b.squareroot()
b.cuberoot()