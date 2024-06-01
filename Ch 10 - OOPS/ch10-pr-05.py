# Write a class called 'Train' which has methods to book a ticket, get seat status and fare info of trains running under Indian Railways.

class Train:
    seat = int(input("Enter the seat number you want: "))
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"Seats available in the train is {self.seats}")
        
    def fareInfo(self):
        print(f"Ticket fare per person is Rs{self.fare}")

    def bookTicket(self):
        if self.seats>0:
            print(f"\nYour train ticket has been booked and the seat number is {self.seat}")
            self.seats -= 1
            self.seat += 1
        else:
            print("Sorry, no seat available! Please try for Tatkal.")

    def cancelTicket(self, seat):
        print(f'Your reservation has been cancelled for seat number {self.seat}')
        self.seats += 1

m = Train("'Intercity Express:14015'", 2, 300)

# seatNo = Train(seat)
# seatNo.getStatus()
m.getStatus()
m.fareInfo()
m.bookTicket()
m.getStatus()
m.cancelTicket(1)
m.getStatus()
m.bookTicket()
m.getStatus()