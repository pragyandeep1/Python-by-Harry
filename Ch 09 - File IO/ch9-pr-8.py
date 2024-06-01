with open('that.txt') as f:
    content = f.read()

with open('senso.txt', 'w') as f:
    f.write(content)