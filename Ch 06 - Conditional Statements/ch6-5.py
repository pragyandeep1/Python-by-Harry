# Spam Detector

text = input("Enter the text here: ")

if("make money" in text):
    spam = True
elif('buy now' in text):
    spam = True
elif('click' in text):
    spam = True
elif('subscribe' in text):
    spam = True
else:
    spam = False

if(spam):
    print('This text is spam.')
else:
    print('This text is not spam.')