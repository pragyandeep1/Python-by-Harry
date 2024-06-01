def readFile(fname):
    try:
        with open(fname, 'r') as b:
            print(b.read())
    except FileNotFoundError:       
        print(f'File "{fname}" is not found.')

readFile('D:/Python by Harry/Ch 12 - Advanced Python/f1.txt')
readFile('D:/Python by Harry/Ch 12 - Advanced Python/f2.txt')
readFile('D:/Python by Harry/Ch 12 - Advanced Python/f3.txt')