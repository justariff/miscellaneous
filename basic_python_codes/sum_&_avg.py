n = int(input("enter the length of the numbers: "))
sum = 0
avg = 0
for i in range(1,n+1):
    num = int(input("Enter your numbers: "))
    sum = sum + num
print("Sum of the given numbers is: ",sum)
avg = sum/n
print("Average of the given numbers is: ",avg)