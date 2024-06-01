# Write a program to check if given post is talking about something or not

post = "Prag is a good person."
name = input("Enter the name: ")
if name in post:
    print("The post is talking about",name)
else:
    print(name,"is absent")