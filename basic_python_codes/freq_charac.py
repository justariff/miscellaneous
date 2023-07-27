strr  = input("Enter the sentence: ")
kisko_dhundho = input("kisko dhundho: ")
freq = 0
for i in strr:
    if i in kisko_dhundho:
        freq+=1
print(freq)