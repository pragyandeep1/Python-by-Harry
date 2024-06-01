try:
    a  = int(input('Enter a number: '))
    i = 1/a
    print(i)

except Exception as e:
    print(f'Exception: {e}')
    exit()

finally:
    print("It's almost done.") # finally statements are executed regardless of any exception.

print('Thanks for watching..')