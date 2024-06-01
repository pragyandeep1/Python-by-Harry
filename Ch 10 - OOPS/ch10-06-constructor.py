class Employee:
    company = "YouTube" # specific to each class
    sal = 1000

    # __init__() is also known as the Constructor in Python as the init method initializes the object.
    def __init__(self, name, sal, company):
        self.name = name
        self.sal = sal
        self.company = company
        print("Employee data is generated.")
        # self.name = name

    def getDetails(self):
        print(f"Name of the employee is {self.name}")
        print(f"Salary of the employee is {self.sal}")
        print(f"Company of the employee is {self.company}")

    @staticmethod
    def greet():
        print("Hey Good Morning Pal")

    @staticmethod
    def time():
        print("The time is 9AM")

# prag = Employee() - missing 3 required positional arguments: 'name', 'sal', and 'company'
prag = Employee("Prag", 3000, "Google")
prag.getDetails()