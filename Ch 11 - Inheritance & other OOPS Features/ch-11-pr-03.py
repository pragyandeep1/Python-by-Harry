'''Create a class 'Employee' and add salary and increment properties to it.
Write a method salAfterIncrement with a @property decorator with a setter
method which changes the value of increment based upon the salary.'''

class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salAfterIncrement(self):
        return self.salary * self.increment

    @salAfterIncrement.setter
    def salAfterIncrement(self,sal):
        self.increment = sal/self.salary

e = Employee()
print(f'Salary after increment: {e.salAfterIncrement}') # 1500.0
print(f'Previous Increment: {e.increment}')
e.salAfterIncrement = 2000
print(f'Current Salary:{e.salAfterIncrement}')
print(f'Current Increment: {e.increment}')