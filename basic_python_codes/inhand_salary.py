ctc = float(input("Enter the salary amount: "))

if ctc > 500000 and ctc<1000000:
    tax = (10/100)*ctc
    temp_sal = ctc - tax
elif ctc>=1000000 and ctc<1500000:
    tax = (20/100)*ctc
    temp_sal = ctc - tax
else:
    tax = (30/100)*ctc
    temp_sal = ctc - tax

print("After salary reduction: ",temp_sal)

hra = (10/100) * temp_sal
da = (5/100) * temp_sal
pf = (3/100) * temp_sal

inhand_sal = (temp_sal - hra - da - pf)/12
print("In-hand salary is: ",inhand_sal)

if inhand_sal <= 999:
    print(inhand_sal)
elif inhand_sal>=1000 and inhand_sal<=9999:
    print(inhand_sal/1000,'k')
elif inhand_sal>=100000 and inhand_sal<=9999999:
    print(inhand_sal/100000,'l')
else:
    print(inhand_sal/10000000,'Cr')