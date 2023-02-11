number=int(input("Enter Any Number : "))

if number==0:
    print("Zero")
    
elif number>0:
    print("Positive Number")
    if number%2==0:
        print("Even Number")
    else:
        print("Odd Number ")

else:
    print("Negative Number ")
    if number%2==0:
        print("Even Number")
    else:
        print("Odd Number")
