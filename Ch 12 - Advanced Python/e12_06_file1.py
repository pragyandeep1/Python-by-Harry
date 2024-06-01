def welcome(name):
    print(f'Back home, {name}')

# print(__name__)

if __name__ is '__main__':
    a = input('Enter the name: ')
    welcome(a)