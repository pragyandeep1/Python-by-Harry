# Single Inheritance

class Employee: # Base class
    company = 'Google'

    def disp(self):
        print('He is an employee.')
        print(f'Company name is {self.company}')

class Programmer(Employee): # Derived class
    lang = 'Python'
    company = 'Youtube'

    def getName(self):
        print(f'The programming language is {self.lang}')
        print(f'Company name is {self.company}')

    def disp(self):
        print('This is a coder.') # overriding the base class info

# Emloyee e = new Employee() -- This syntax only works in Java
e = Employee()
e.disp()
p = Programmer()
p.disp()
p.getName()
print(p.company)
