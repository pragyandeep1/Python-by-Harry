'''Write a class 'Complex' to represent complex numbers along with overloaded operators
 + which adds them and * which multiples them'''

class Complex:
    def __init__(self,r,i):
        self.real = r
        self.imaginary = i

    def __add__(self,c):
        return Complex(self.real + self.imaginary + c.imaginary)

    def __mul__(self,c):
        mulReal = self.real * c.real - self.imaginary * c.imaginary
        mulImg = self.real * c.imaginary - self.imaginary * c.real
        return Complex(mulReal,mulImg)

    def __str__(self):
        return f'{self.real}+{self.imaginary}i'

c1 = Complex(1,4)
c2 = Complex(8,5)
print(c1+c2) # 9+9i
print(c1*c2) # -12-27i