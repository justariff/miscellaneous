flag=0
a = 10000
print(a)

while True:
    b = (a) - (a*10)/100
    a = b
    print(int(b))
    flag += 1

    if flag==9:
        break
