L1=[4,5,7,34,221]
L1.sort()
print(L1[-1])


L = [3,5,6,31]
rev = []
for i in range(len(L)-1,-1,-1):
    rev.append(L[i])
print(rev)

L2 = [4,5,33,53,22,43,23]
a = int(input("kisko nikalu: "))
for i in L2:
    if i==a:
        print('True')
        break
    else:
        print('False')
        break
