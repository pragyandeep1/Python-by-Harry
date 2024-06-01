import random
randomNum = random.randint(1,100)
useGuess = None
guess = 0

while useGuess != randomNum:
    useGuess = int(input('Enter the guess: '))
    guess += 1
    if useGuess == randomNum:
        print('Your guess is right.')
    else:
        if useGuess < randomNum:
            print('You guessed wrong. Enter a greater number.')
        else:
            print('You guessed wrong. Enter a smaller number.')
    
print(f'The number is {randomNum}')

with open('topScore.txt','r') as f:
    top = int(f.read())

if(guess<top):
    print('New record!')
    with open('topScore.txt','w') as f:
        f.write(str(guess))

print(f'You guessed the number in {guess} guesses.')