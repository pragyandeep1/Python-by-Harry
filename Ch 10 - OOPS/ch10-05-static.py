class Employee:
    company = "YouTube" # specific to each class
    sal = 1000
    def getSal(self, sign): # self is used to avoid 'getSal() takes 0 positional arguments but 1 was given'
        # print("Salary is 10k.")
        print(f"Average salary of an employee who works in {self.company} is {self.sal} \n {sign}")

    @staticmethod
    def greet():
        print("Hey Good Morning Pal")

    @staticmethod
    def time():
        print("The time is 9AM")

prag = Employee()
prag.sal = 9000
prag.greet()
prag.time()
prag.getSal("Thanks a lot!")