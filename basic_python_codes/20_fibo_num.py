count = 0
a = 0
b = 1
print(a)
print(b)

while True:
    c = a + b
    a = b
    b = c
    print(c)
    count += 1
    if count == 18:
        break