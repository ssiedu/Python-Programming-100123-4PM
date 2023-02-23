import math
class Area:
    def getdata(self,a):
        self.r=a
    def calArea(self):
        self.area=math.pi*self.r*self.r
        print("Area of Circle : %.2f" %self.area)


A=Area()
n=eval(input("enter Radius of circle : "))
A.getdata(n)
A.calArea()
#A.display()
