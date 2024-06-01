# Railway_OOPS

import pandas as pd

pd.DataFrame()

class RailwayForm:
    fType = "RailForm"
    def wData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

pragApp = RailwayForm()
pragApp.name = "Prag"
pragApp.train = "Garib Rath"
pragApp.wData()

'''
PascalCase --> EmployeeName
camelCase --> isNumeric, isFloatOrInt
'''