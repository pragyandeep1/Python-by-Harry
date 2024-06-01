# Write a Python program to rename a file to 'renamedByPython.txt'

import os

oName = 'sample.txt'
nName = 'renamedByPython.txt'

with open(oName) as f:
    content = f.read()

with open(nName, 'w') as f:
    f.write(content)

os.remove(oName)