# Sum of n natural numbers
sum = 0
num = int(input("Enter the number: "))
target = num
while num>0:
    sum = num + sum
    num-=1
print("Sum till",target,"=",sum)

sum = 0
num = target
for i in range(0,num):
    sum = num + sum
    num-=1
print(f"Sum till {target} = {sum}")