import pickle
file=open("binary","wb")
x=[10,20,30,40,50]
pickle.dump(x,file)
file.close()
with open("binary","rb") as file:
    data=pickle.load(file)
    print(data)
file.close()
