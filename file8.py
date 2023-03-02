import pickle
class Student:
    def __init__(self,rno=0,name=""):
        self.rollno=rno
        self.name=name
        self.s1,self.s2,self.s3=0.0,0.0,0.0
    def readMarks(self):
        print("Enter Marks of three Subject given below:")
        self.s1=eval(input("Enter Marks of subject1: "))
        self.s2=eval(input("Enter Marks of subject2: "))
        self.s3=eval(input("Enter Marks of subject3: "))
    def display(self):
        print("Name     : ", self.name)
        print("Roll No  : ", self.rollno)
        print("Subject1 : ", self.s1)
        print("Subject2 : ", self.s2)
        print("Subject3 : ", self.s3)

S1=Student(101,"Ram")
S2=Student(102,"Shyam")
S1.readMarks()
S2.readMarks()
file=open("Record","wb")
pickle.dump(S1,file)
pickle.dump(S2,file)
file.close()

S=Student()
f=open("Record","rb")
try:
    while True:
        S=pickle.load(f)
        S.display()
except EOFError:
    file.close()












        
        
        
        
