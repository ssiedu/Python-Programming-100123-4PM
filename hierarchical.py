class Base:
    def __init__(self):
        self.num1=int(input("Enter first Number :"))
        self.num2=int(input("Enter Second Number :"))


class child1(Base):
    def getAddition(self):
        self.sum=self.num1+self.num2
        print("Addition :",self.sum)


class child2(Base):
    def getMul(self):
        self.mul=self.num1*self.num2
        print("Multiplicationb :",self.mul)


class child3(Base):
    def getDiv(self):
        self.div=self.num1/self.num2
        print("Division :",self.div)


c1=child1()
c1.getAddition()
c2=child2()
c2.getMul()
c3=child3()
c3.getDiv()
        




        
