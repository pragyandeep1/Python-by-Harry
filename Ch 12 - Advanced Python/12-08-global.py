a = 12

def func():
    global a
    print(f'Print statement 1: {a}')  
    a = 8
    print(f'Print statement 2: {a}')

func()
print(f'Print statement 3: {a}') 