try:
    a  = int(input('Enter a number: '))
    c = 1/a
    print(c)
except ValueError as e:
    print('Enter a valid value.')

except ZeroDivisionError as e:
    print('Try to avoid dividing by zero.')
    
print('Thanks for using this snippet.')