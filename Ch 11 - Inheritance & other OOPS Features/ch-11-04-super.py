class Human:
    state = 'Odisha'
    pay = 500

    def __init__(self):
        print('Initializing the human being.\n')

    def brTime(self):
        print('Tea Time')

    def gender(self):
        print('Male')

class Job(Human):
    org = 'Hero'

    def __init__(self):
        super().__init__()
        print('Start doing a job.')

    def getPay(self):
        print(f'Payment is {self.pay}')

    def brTime(self):
        super().brTime() # Tea Time
        print('I am taking a short break now.')

class House(Job):
    org = 'Ferera'

    def __init__(self):
        super().__init__()
        print('Construction site is running.')

    def getPay(self):
        print('Clients did not pay for this month.')

    def brTime(self):
        super().brTime() # I am taking a short break now.
        print('Coffee Time')

h = Human()
j = Job()
ho = House()
ho.getPay() # Clients did not pay for this month.
ho.brTime() # Tea Time I am taking a short break now. Coffee Time
j.getPay() # Payment is 500
j.brTime() # Tea Time I am taking a short break now.
h.brTime() # Tea Time