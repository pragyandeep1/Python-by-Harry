# f = open('D:\Bitan\Python by Harry\Ch9 - File IO\sample.txt', 'r') # use open function to read the content of the file
f = open('D:\Bitan\Python by Harry\Ch9 - File IO\sample.txt') # By default the mode is read mode
# text = f.read() # data = f.read()
text = f.read(5) # reads first five characters from the existing file
print(text) # print(data)
f.close()
