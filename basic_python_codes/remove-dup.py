L1 = [2,3,2,3,4,5,5,5,5,5,55,5,5,4,5,2]
L2 = []
for i in L1:
    if i not in L2:
        L2.append(i)
print(L2)