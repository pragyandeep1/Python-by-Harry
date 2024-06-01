''' Write a program to find out whether a student is pass or fail if it requires total 40% and at least 33% in each subject to pass.
Assume 3 subjects and take marks as input from the user. '''

sub1 = int(input("Enter marks of subject1: "))
sub2 = int(input("Enter marks of subject2: "))
sub3 = int(input("Enter marks of subject3: "))
tot = sub1+sub2+sub3;

if (sub1<33 or sub2<33 or sub3<33):
    print("You're fail due to less than 33% in one of the subjects.")
elif (tot)/3 <40:
    print("You're fail due to total percentage is less than 40%")
else:
    print("Congrats! You have succefully passed the exam and you secured", tot, "marks.")