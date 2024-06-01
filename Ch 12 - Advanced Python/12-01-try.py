while(True):
    # print('Press q to quit')
    a = input('Enter a number: ')
    if a is 'q' or 'quit':
        break
    try:
        print("Testing...")
        a = int(a)
        if a>6:
            print("You've entered a number greater than 6")
    except Exception as e:
        print(f'Exception occurred: {e}')

print('Thanks for playing this game!')