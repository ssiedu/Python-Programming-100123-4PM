import random
while True:
    ch=input('''
Game Start....
1.Yes('y')
2.No|Exit('n')
''')
    if ch.lower()=='y':
        cinput=random.randrange(1,6)
        uinput=int(input("Enter any number : "))

        if cinput>uinput:
            print("Computer Number :",cinput)
            print("your number is too low")

        elif uinput>cinput:
            print("Computer Number : ",cinput)
            print("your guess number is too high")

        else:
            print("Computer Number :",cinput)
            print("Both are equal")
    else:
        break;
