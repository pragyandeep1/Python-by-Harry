# Write a function that converts inch to cm

def cm(inch):
    return (inch*2.54)

i = int(input("Enter length in inch: "))
c = cm(i)
print("The length in centimeter is",str(c)+'cm')