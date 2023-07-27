num = int(input("enter the number: "))
sum=0
temp=num

while temp>0:
    digit = temp%10
    sum = digit**3 + sum
    temp = temp//10

if num==sum:
    print("Armstrong No.")
else:
    print("No")