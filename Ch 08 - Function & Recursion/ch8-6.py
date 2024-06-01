# Write a program using function to findout the greatest among 3 numbers 

def maxi(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            return n1
        else:
            return n3
    else:
        if n2>n3:
            return n2
        else:
            return n3

high = maxi(34,45,29)
print("The greatest number is",str(high))