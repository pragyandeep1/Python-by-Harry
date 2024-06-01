# DRY = Don't Repeat Yourself

class Sum:
    def add(self):
        return self.a +self.b

num = Sum()
num.a = 12
num.b = 34
s = num.add()
print(s)