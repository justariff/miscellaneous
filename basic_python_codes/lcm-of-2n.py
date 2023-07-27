n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
a = n1
b = n2

while n1 % n2 != 0 :
    rem = n1 % n2
    n1 = n2
    n2 = rem
hcf = n2

lcm = (a * b) / hcf

print("lcm is : ",lcm)