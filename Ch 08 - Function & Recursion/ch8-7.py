# Write a program to convert temperature from celsius to fahrenheit using function

def fahr(cel):
    return (cel*(9/5))+32

c = int(input("Enter the temperatue in Celcius: "))
f = fahr(c)
print("The temperature in Fahrenheit is",str(f)+"F")