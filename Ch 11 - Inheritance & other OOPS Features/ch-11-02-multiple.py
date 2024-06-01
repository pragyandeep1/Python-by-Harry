# Multiple Inheritance

class Employee:
    company = 'eBay'
    code = 120

class Office:
    company = 'codR'
    level = 0

    def upLevel(self):
        self.level = self.level + 1

class Boss(Office, Employee): # codR
    name = 'Prag'

b = Boss()
b.upLevel()
print(b.company)
print(b.name)
print(b.level)
print(b.code)