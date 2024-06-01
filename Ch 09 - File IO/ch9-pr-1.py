f = open('D:\Bitan\Python by Harry\Ch9 - File IO\poem.txt')
t = f.read()
if 'twinkle' in t:
    print("Twinkle is present in the poem")
else:
    print("Twinle is absent")
f.close()
