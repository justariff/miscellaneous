n = int(input("Enter the number: "))
i = 1
if n > 0:
    while n >= 1 :
        i = i * n
        n = n - 1
    print("Factorial of the given number: ",i)

else:
    print("Factorial is not possible")