user_input = input('''
Hi! This is Arif Ansari
What would you like to do?

1. Convert cm to inches
2. Convert km to miles
3. Convert USD to INR
4. Exit

''')

if user_input=='1':
    cm = float(input("Enter value in cm: "))
    inches = cm*0.394
    print("Value in inches: ",inches)

elif user_input=='2':
    km = float(input("enter value in km: "))
    miles = km * 0.621
    print("Value in miles: ",miles)

elif user_input=='3':
    USD = float(input("Enter the usd amount: "))
    inr = USD * 82.71
    print("Amount in inr: ",inr)

else:
    print("EXIT")