class Mul:
    def getdata(self):
        self.num1=int(input("Enter First number : "))
        self.num2=int(input("Enter Second Number : "))
    def multiply(self):
        self.res=self.num1*self.num2
    def display(self):
        print("Result is : ", self.res)


M=Mul()
M.getdata()
M.multiply()
M.display()

n=Mul()
n.getdata()
n.multiply()
n.display()
