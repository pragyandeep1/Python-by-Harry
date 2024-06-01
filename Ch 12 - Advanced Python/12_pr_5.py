# write a program to store multiplication tables in a file named tables.txt

num = int(input('Enter number: '))
tab = [num*i  for i in range (1,11)]
print(f'Multiplication table of {num} = {tab}')

with open ('D:/Python by Harry/Ch 12 - Advanced Python/tables.txt', 'a') as f:
    f.write(str(f'Multiplication table of {num} = {tab}'))
    f.write('\n')