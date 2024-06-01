def inc(num):
    try:
        return int(num)+1

    except:
        raise ValueError("It's very bad - Prag")

a = input('Enter a value: ')
b = inc('a') 
print(b)