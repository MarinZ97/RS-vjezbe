a=float(input("Unesi prvi broj:"))
b=float(input("Unesi drugi broj:"))
operator=input("Unesi operator (+, -, *, /):")
if operator=='+':
    c=a+b   
elif operator=='-':
    c=a-b
elif operator=='*':
    c=a*b
elif operator=='/':
    if b!=0:
        c=a/b
    else:
        print("Greska: Dijeljenje sa nulom nije dozvoljeno.")
        exit()
print("Rezultat je:",c)

