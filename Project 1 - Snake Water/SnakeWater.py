import random

def gameWin(comp, player):
    if comp is player:
        return None
    elif comp is 'snake':
        if player is 'water':
            return False
        elif player is 'gun':
            return True
    elif comp is 'water':
        if player is 'gun':
            return False
        elif player is 'snake':
            return True
    elif comp is 'gun':
        if player is 'snake':
            return False
        elif player is 'water':
            return True

print("Computer Turn: Snake(s), Water(w) or Gun(g)?")
num = random.randint(1,3)
if num is 1:
    comp = 'snake'
elif num is 2:
    comp = 'water'
elif num is 3:
    comp = 'gun'

player = input("Your Turn: Snake(s), Water(w) or Gun(g)? ")
a = gameWin(comp,player)

print(f"Computer chose {comp}")
print(f"You chose {player}")

if a is None:
    print("It's a Tie")
elif a:
    print("You won")
else:
    print("Computer won")

'''SWG = ["Snake", "Water", "Gun"]
computer = random.choice(SWG)
player = False
i = 0
Pscr = 0
Cscr = 0
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
            '''