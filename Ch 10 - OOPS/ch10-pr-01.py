class Programmer:
    company = 'Microsoft'
    def __init__(self, name, product):
        self.name = name
        self.product = product
        print("Employee data is generated.")

    def getDetails(self):
        print(f"Name of the programmer is {self.name}")
        print(f"Product of {self.name} is {self.product}")

prag = Programmer("Prag", "Skype")
lisa = Programmer("Lisa", "Laravel")
prag.getDetails()
lisa.getDetails()
