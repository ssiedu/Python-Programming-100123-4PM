class Add:
    def __init__(self):
        self.num1=int(input("Enter First Number : "))
        self.num2=int(input("Enter First Number : "))
    def Addition(self):
        self.sum=self.num1+self.num2
    def display(self):
        print("Addition of two numbers : ",self.sum)


A=Add()
A.Addition()
A.display()
