'''Write a program to findout whether a given username is less than 10 characters or not'''

user = input("Enter a username: ")
if(len(user)<10):
    print("Less than 10 characters.")
else:
    print("More than 10 characters.")