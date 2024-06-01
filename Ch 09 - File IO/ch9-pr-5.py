words = ['laddu','gadhe','bhendu']

with open('latter.txt') as f:
    content = f.read()

for word in words:
    content = content.replace(word, '$#!t#@!&')
    with open('latter.txt','w') as f:
        f.write(content)