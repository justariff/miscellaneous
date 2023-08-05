p = int(input("Enter the Principle: "))
r = int(input("Enter the rate of interest: "))
t = int(input("Enter the time period elapsed: "))

a = p*(1 + r / 100)**t
print("Your amount is: ",a)

ci = a - p
print(ci)
