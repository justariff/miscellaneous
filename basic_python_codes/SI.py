p = float(input("enter principle: "))
r = float(input("enter rate of the interest: "))
t = float(input("enter time period in years: "))

si =  ( p*r*t )/100
print("The Simple Interest of given inputs is: ",si)
amount = p + si
print("the amount is: ",amount)
