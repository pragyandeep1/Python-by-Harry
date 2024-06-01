f1 = 'log.txt'
f2 = 'senso.txt'

with open(f1) as f:
    fi = f.read()

with open(f2) as f:
    fj = f.read()

if fi in fj:
    print("Identical files")
else:
    print("Different ones")