class Add:
    def __init__(self,a=0,b=0):
        self.num1=a
        self.num2=b
    def Addition(self):
        self.sum=self.num1+self.num2
    def display(self):
        print("Value of num1 :",self.num1)
        print("value of num2 :",self.num2)
        print("Addition of two numbers : ",self.sum)


#x=int(input("Enter First Number :"))
#y=int(input("Enter Second Number : "))

A=Add()
A.Addition()
A.display()
