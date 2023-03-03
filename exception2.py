try:
    number=int(input("Enter any number upto 100 :"))
    if number>100:
        raise ValueError

except ValueError:
    print("Invalid Number ")

else:
    print("Valid Number")

finally:
    print("Thank You")
