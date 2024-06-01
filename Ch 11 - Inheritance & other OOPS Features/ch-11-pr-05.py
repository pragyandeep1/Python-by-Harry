'''Write a class 'Vector' representing a vector of n dimension.
Overload the + and * operators which calculate the sum and
 dot product of them.'''

class Vector:
    def __init__(self,vec):
        self.vec = vec

    def __str__(self):
        st = ""
        tmp = 0
        for i in self.vec:
            st += f'{i}a{tmp}+'
            tmp += 1
        return st[:-1]

v1 = Vector([1,4,6])
print(v1)
 # 1a0 + 4a1 + 6a2