x = int(input("enter the value of x: "))
n = int(input("enter your number: "))
sum = 1
for i in range(2,n+1):
    sum = sum + ((x**i)/i)
print(sum)