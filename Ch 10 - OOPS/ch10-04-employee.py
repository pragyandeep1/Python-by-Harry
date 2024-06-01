class Employee:
    company = "YouTube" # specific to each class
    sal = 1000
    def getSal(self): # self is used to avoid 'getSal() takes 0 positional arguments but 1 was given'
        # print("Salary is 10k.")
        print(f"Average salary of an employee who works in {self.company} is {self.sal}")

prag = Employee() # object is instatiated
raju = Employee() # object is instatiated
Employee.getSal(raju)

prag.sal = 9000
Employee.getSal(prag) # getSal gets a parameter 'prag'

# Creating instance attribute name for both objects
prag.name = "Prag"
raju.name = "Raju"
print(f"The employee name is {prag.name}")
prag.getSal() # It is same as 'Employee.getSal(prag)'

print(f"The employee name is {raju.name}")
raju.getSal() # It is same as 'Employee.getSal(raju)'

# Creating instance attribute sal for both objects
prag.sal = 5000
# raju.sal = 2000
print(f"Prag's company name is {prag.company}")
print(f"Raju's company name is {raju.company}")

prag.sal = 400 # overwriting sal value
print(f"Prag's current salary is {prag.sal}")
print(f"Raju's current salary is {raju.sal}")
Employee.company = "Google" # changing class attribute
print(f"Prag's new company name is {prag.company}")
print(f"Raju's new company name is {raju.company}")

# The line below throws an error as the address is absent in the instance of the class 
# print(raju.address)
