num =int(input("enter the number: "))
sum_sq=0

while num!=0:
    temp = num%10
    sum_sq = temp**2 + sum_sq
    num=num//10

print(sum_sq)
