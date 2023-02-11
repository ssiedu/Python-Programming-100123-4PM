print("1.Addition(+) \n2.Subtraction(-) \n3.Multiplication(*) \n4.Division(/)")
ch=input("Enter your choice : ")
num1=eval(input("Enter First Number : "))
num2=eval(input("Enter Second Number : "))
match ch:
    case '+':
        print("Addition : ", num1+num2)
    case '-':
        print("Subtraction : ", num1-num2)
    case '*':
        print("multiplication : ", num1*num2)
    case '/':
        print("Division : ", num1/num2)
    case _:
        print("invalid choice")
