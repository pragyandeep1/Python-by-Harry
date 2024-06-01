import random
SWG = ["Snake", "Water", "Gun"]
computer = random.choice(SWG)
player = False
i = 0
Pscr = 0
Cscr = 0
'''Player is False because when program runs then
status changes from False to True'''
while (i<10):
    player = input("Snake, Water, Gun?")
    if player == computer:
        print("Tie!")
    elif player == "Snake":
        if computer == "Gun":
            print("You lose!", computer, "Killed", player, "Em.")
            Pscr = Pscr-1
            Cscr = Cscr+1
        else:
            print("You win!", player, "Swam and escaped.", computer, "in." )
            Pscr = Pscr + 1
            Cscr = Cscr - 1
    elif player == "Water":
        if computer == "Snake":
            print("You lose!", computer, "Swam and escaped.", player, "in" )
            Pscr = Pscr - 1
            Cscr = Cscr + 1
        else:
            print("You win!", player, "Drowned.", computer, "em" )
            Pscr = Pscr + 1
            Cscr = Cscr - 1
    elif player == "Gun":
        if computer == "Water":
            print("You lose...", computer, "Sunk!", player, "em")
            Pscr = Pscr - 1
            Cscr = Cscr + 1
        else:
            print("You win!", player, "Killed", computer, "em.")
            Pscr = Pscr + 1
            Cscr = Cscr - 1
    else:
        print("Check your spelling!")
    computer = random.choice(SWG)
    i= i+1
    if (i==10):
        print("Your Final Score Is")
        print(Pscr)
        print("And Computer's Final Score Is")
        print(Cscr)
        if Pscr == Cscr:
            print("Match Drawn")
        elif Pscr>Cscr:
            print('You Win')
        else:
            print("You Lose")