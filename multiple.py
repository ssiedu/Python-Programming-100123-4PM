class Base1:
    def getFirstNumber(self):
        self.num1=eval(input("Enter First Number :"))


class Base2:
    def getSecondNumber(self):
        self.num2=eval(input("Enter Second Number :"))


class Base3:
    def getThirdNumber(self):
        self.num3=eval(input("Enter third Number :"))


class Child(Base1,Base2,Base3):
    def calProduct(self):
        self.res=self.num1*self.num2*self.num3
        print("Product of three numbers : ",self.res)


C=Child()
C.getFirstNumber()
C.getSecondNumber()
C.getThirdNumber()
C.calProduct()




        
