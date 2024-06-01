letter =  ''' Dear <name>
Greetings! XYZ Solutions appoints you as a web developer.
You are selected! Join us immidiately.
Have a great day ahead.
Thanks and regards
Mr Bill
Date: <date>
'''
name = input("Enter the name: ")
date = input("Enter today's date: ")
letter = letter.replace("<name>", name)
letter = letter.replace("<date>", date)
print(letter)