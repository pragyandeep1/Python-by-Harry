f = open('D:\Bitan\Python by Harry\Ch9 - File IO\sample.txt')
text = f.readline() # reads first line
print(text)
data = f.readline() # reads second line
print(data)
f.close()