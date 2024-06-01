# Multiplication Table of the given number using for loop

num = int(input("Enter a number: "))
for i in range(1,11):
    # print(num,'X',i,'=',(num*i))
    # print(str(num)+" X "+str(i)+" = "+str(num*i)) This one is same as the above.
    print(f'{num} X {i} = {num*i}')