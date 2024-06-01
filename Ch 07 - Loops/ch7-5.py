# Check whether a number is prime or not
num = int(input('Enter a number: '))
prime = True
for i in range(2,num):
    if num%i is 0:
        prime = False
        break
if prime:
    print("Number is Prime.")
else:
    print("Number is not Prime.")