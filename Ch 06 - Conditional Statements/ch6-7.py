'''Write a program to check if a name present in the list or not.'''
names = ['radhe','prag','shyam','golu','gabbar']
name = input("Enter your name: ")

if name not in names:
    print("Your name is not present in the list.")
else:
    print("Your name is present in the list.")