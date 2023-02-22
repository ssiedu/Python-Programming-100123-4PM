class Add:
    def getdata(self):
        self.num1=eval(input("Enter First Number : "))
        self.num2=eval(input("Enter Second Number : "))
    def calculate(self):
        self.sum=self.num1+self.num2
    def display(self):
        print("Sum of two numbers : ",self.sum)


obj=Add()
obj.getdata()
obj.calculate()
obj.display()

a=Add()
a.getdata()
a.calculate()
a.display()
