# Write a Python program to wipe out the contents of a file

fname = 'sample.txt'
with open(fname, 'w') as f:
    f.write("")