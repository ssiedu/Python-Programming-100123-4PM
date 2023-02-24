class Base:
    def getdata(self):
        self.l=int(input("Enter length of retangle :"))
        self.b=int(input("Enter breadth of rectangle :"))



class Derive(Base):
    def calArea(self):
        self.area=self.l*self.b
    def display(self):
        print("Area of rectangle :",self.area)


D=Derive()
D.getdata()
D.calArea()
D.display()
