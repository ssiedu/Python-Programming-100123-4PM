number=int(input("Enter any Number : "))
if number%5==0 and number%7==0:
    print("Number is divisible by both")
elif number%7==0:
    print("Number is divisible by 7")
elif number%5==0:
    print("Number is divisible by 5")
else:
    print("Number is not divisible by both ")
