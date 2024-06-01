try:
    a  = int(input('Enter a number: '))
    i = 1/a
    print(i)

except Exception as e:
    print(f'Exception: {e}')

else:
    print("It's almost done.")