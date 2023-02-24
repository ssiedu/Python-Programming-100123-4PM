class Base1:
    def __init__(self):
        self.r=int(input("Enter radius :"))


class child1(Base1):
    def calArea(self):
        self.carea=3.14*self.r*self.r


class child2:
    def getdata(self):
        self.l=int(input("Enter length :"))
        self.b=int(input("Enter breadth :"))
    def Area(self):
        self.rarea=self.l*self.b

class child(child1,child2):
    def display(self):
        print("Area of circle :",self.carea)
        print("Area of rectangle :",self.rarea)



c=child()
c.calArea()
c.getdata()
c.Area()
c.display()
