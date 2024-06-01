with open('log.txt') as f:
    content = f.read()

if 'python' in content.lower():
    print("There is python")
else:
    print("No python")