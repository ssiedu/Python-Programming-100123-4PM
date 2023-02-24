class First:
    def getdata(self):
        self.num1=eval(input("Enter First Number :"))
        self.num2=eval(input("Enter Second number :"))


class Second(First):
    def Addition(self):
        self.sum=self.num1+self.num2



class Third(Second):
    def display(self):
        print("Addition of two numbers :",self.sum)


T=Third()
T.getdata()
T.Addition()
T.display()
