f = open('D:\Bitan\Python by Harry\Ch9 - File IO\sample.txt', 'rb')
text = f.readline() # reads first line
print(text)
data = f.readline() # reads second line
print(data,"\n")
f.close()

f = open('D:\Bitan\Python by Harry\Ch9 - File IO\sample.txt', 'rt')
text = f.readline() # reads first line
print(text)
data = f.readline() # reads second line
print(data)
f.close()

f = open('another.txt', 'w')
f.write("Please Write this to the file.")
f.close()

