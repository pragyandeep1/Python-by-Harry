# Write a program to calculate the percentage of marks of 2 students in an exam
def percent(marks):
    per = (sum(marks)/500)*100
    return per

marks0 = [78,45,67,90,88]
# percentage0 = (sum(marks0)/400)*100
percentage0 = percent(marks0)

marks1 = [88,65,47,98,79]
# percentage1 = ((marks1[0]+marks1[1]+marks1[2]+marks1[3])/400)*100
percentage1 = percent(marks1)

print(percentage0,percentage1)