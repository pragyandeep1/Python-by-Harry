# Name of fruits and their word size    

fruit = ['brinjal', 'banana', 'pear','guava','apple']
i = 0

# while loop
while i<len(fruit):
    print(fruit[i],"length:",len(fruit[i]))
    i+=1
print("\n")

# for loop
for i in fruit:
    print(i,"length:",len(i))
print("\n")

# range function
for i in range(1,8):
    print(i)
print("\n")

for i in range(1,5):
    print(fruit[i-1],"length:",len(fruit[i-1]))
print("\n")

for i in range(1,5,2):
    print(fruit[i-1],"length:",len(fruit[i-1]))
print("\n")

# else conditional statement with for loop
for i in range(8):
    print(i)
else:
    print("Now the control is inside else of for loop.")
print("\n")

for i in fruit:
    print(i,"length:",len(i))
else:
    print("It's over.")
print("\n")

# break statement (avoid using break statement)
for i in range(10):
    print(fruit[i+1],"length:",len(fruit[i+1]))
    if i == 3:
        break
else:
    print('You are inside else.')
print('\n')

# continue statement
for i in range(10):
    if i == 3:
        continue
    print(i)
print('\n')

for i in range(5):
    if i == 3:
        continue
    print(fruit[i],"length:",len(fruit[i]))
print('\n')

# Pass is null statement
if i>0:
    pass
def run(player):
    pass
print("My name is Prag")