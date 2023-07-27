cp = float(input("enter your cost price: "))
sp = float(input("enter your selling price: "))

if sp>cp:
    amount = sp - cp
    print("profit",amount)
else:
    amount = cp - sp
    print("loss",amount)