# Write a program to greet a person with best wishes
def wish(name='Stranger'):
    print("Best of Luck",name)
    call = "Hi " + name
    return call
a = wish("Prag")
b = wish() # Default parameter value
print(a+"\n"+b)