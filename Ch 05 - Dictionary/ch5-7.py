'''Create an empty dictionary.
Allow 4 friends to enter their favorite languages as values and use keys as their names.
Assume that names are unique'''

favLang = {}
a = input("Enter Aman's favorite language: ")
b = input("Enter Baman's favorite language: ")
c = input("Enter Chaman's favorite language: ")
d = input("Enter Daman's favorite language: ")
e = input("Enter Baman's favorite language: ")
favLang['Aman'] = a
favLang['Baman'] = b
favLang['Chaman'] = c
favLang['Daman'] = d
favLang['Baman'] = e
print(favLang)