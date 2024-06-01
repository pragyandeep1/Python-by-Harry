class Emp:
    com = "Caramel"
    sal = 200
    loc = "bbsr"

    def chSal(self, s):
        print(f"Salary is {self.sal}")
        self.__class__.sal = s
        print(f"Salary is {self.sal}")

    @classmethod # decorator
    def changeSal(cls, s):
        cls.sal = s
        # print(f"Salary is {self.sal}") -- NameError: name 'self' is not defined

e = Emp()
print(e.sal)
e.chSal(789)
e.changeSal(673)
print(e.sal)
print(Emp.sal)