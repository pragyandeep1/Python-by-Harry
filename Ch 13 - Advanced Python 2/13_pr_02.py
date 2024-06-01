# Write a program to input name, marks and phone number of a student and format it using the format function as below:
# The name of the student is Prag, his marks is 72 and his phone number is 8249675334

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
mob = input("Enter your phone number: ")

temp = "The name of the student is {}, his marks is {} and his phone number is {}"
out = temp.format(name, marks,mob)
print(out)