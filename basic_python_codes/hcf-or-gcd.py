n1 = int(input("enter the first number: "))
n2 = int(input("nter the second number: "))

while n1%n2 != 0:
    rem = n1 % n2
    n1 = n2
    n2 = rem
print("The highest common factor, HCF: ",n2)