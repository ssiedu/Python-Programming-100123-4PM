a=int(input("Enter First Number : "))
b=int(input("Enter Second Number : "))

if a!=b:
    print(a," is not equal to ",b)
    if a>b:
        print(a ," is greater than ",b)
    else:
        print(b," is greater than ",a)
else:
    print(a," is equal to",b)
