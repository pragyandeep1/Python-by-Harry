def game():
    return 94

score = game()
with open('D:\Python by Harry\Ch9 - File IO\highscore.txt') as n:
    high = n.read()

if int(high)<score:
    with open('D:\Python by Harry\Ch9 - File IO\highscore.txt', 'w') as n:
        n.write(str(score))
elif high is '':
    with open('D:\Python by Harry\Ch9 - File IO\highscore.txt', 'w') as n:
        n.write(str(score))
