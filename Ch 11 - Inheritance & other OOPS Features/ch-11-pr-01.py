# Create a class C2d vector and use it to create another class representing a 3d vector

class C2dVec:
    def __init__(self,i,j):
        self.iCap = i
        self.jCap = j

    def __str__(self):
        return f'{self.iCap}i+{self.jCap}j'

class C3dVec:
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kCap = k

    def __str__(self):
        return f'{self.iCap}i+{self.jCap}j+{self.kCap}k' 

v2d = C2dVec(1,3)
v3d = C3dVec(1,9,7)
print(v2d) # 1i + 3j
print(v3d) # 1i + 9j + 7k