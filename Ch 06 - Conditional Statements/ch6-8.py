'''Write a program to calculate the grade of a student from his/her marks.'''

mark = int(input("Enter your marks in the exam: "))

def first():
    return "O Grade."
def second():
    return "E Grade."
def third():
    return "A Grade."
def fourth():
    return "B Grade."
def fifth():
    return "C Grade."
def sixth():
    return "D Grade."
def seventh():
    return "Fail."

if(mark>=90 and mark<100):
    print(first())
elif(mark>=80 and mark<90):
    print(second())
elif(mark>=70 and mark<80):
    print(third())
elif(mark>=60 and mark<70):
    print(fourth())
elif(mark>=50 and mark<60):
    print(fifth())
elif(mark>=40 and mark<50):
    print(sixth())
elif(mark<40):
    print(seventh())
else:
    print("Invalid input.")