a = 'arif ansari btech'
y = a.split()
print(y)
r = ''
for i in y:
    r = r + i[0].upper() + i[1:].lower() + ' '
print(r)