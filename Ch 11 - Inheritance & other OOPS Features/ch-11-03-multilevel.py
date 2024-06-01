# Multilevel Inheritance

class Human:
    state = 'Odisha'
    pay = 500

    def brTime(self):
        print('Tea Time')

    def gender(self):
        print('Male')

class Job(Human):
    org = 'Hero'

    def getPay(self):
        print(f'Payment is {self.pay}')

    def brTime(self):
        print('I am taking a short break now.')

class House(Job):
    org = 'Ferera'

    def getPay(self):
        print('Clients did not pay for this month.')

h = Human()
# h.getPay() -- throws an error 'Human' object has no attribute 'getPay'
j = Job()
ho = House()
ho.getPay()
ho.brTime()
print(ho.state)
print(ho.org)
print(j.org)
j.getPay()
j.brTime()
h.brTime()
ho.gender()