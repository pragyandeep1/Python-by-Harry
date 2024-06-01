# Property Decorator (getter method)

class Employee:
    org  = "Indane Gas"
    sal  = 4000
    bonus = 100
    # totSal = 4100

    @property # getter method
    def totSal(self):
        print(f'Total Salary = {self.sal + self.bonus}')
        return self.sal + self.bonus

    @totSal.setter # setter method
    def totSal(self, val):
        self.bonus = val - self.sal

e = Employee()
print(e.totSal) # totSal became a property; generating value by internally running the function
e.totSal = 7800
print(f'Present Salary = {e.sal}')
print(f'Total Bonus = {e.bonus}')