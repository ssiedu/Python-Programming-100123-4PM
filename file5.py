list1=[]
fout=open("listdata.txt","w")
for i in range(5):
    name=input("Enter Name :")
    list1.append(name+"\n")

fout.writelines(list1)
fout.close()
    
