with open('letter.txt') as f:
    content = f.read()
content = content.replace('Donkey', '$#!t#@!&')
with open('letter.txt','w') as f:
    f.write(content)