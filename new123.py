import string
data = open('new.txt', 'r').read()
print len(data.splitlines()), len(string.split(data)), len(data)