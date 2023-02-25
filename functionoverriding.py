class Base:
    def __init__(self):
        print("this is Base class Function")


class derive(Base):
    def __init__(self):
        Base.__init__(self)
        #super().__init__()
        print("THis is derive class Function")



d=derive()
#d.getdata()
#d.getdata()
