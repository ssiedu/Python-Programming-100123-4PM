fout=open("Student.txt","a")
for i in range(2):
    name=input("Enter Student Name :")
    s_id=int(input("Enter Student id :"))
    per=eval(input("Enter Student percentage :"))
    res=name+ " " + str(s_id) + " " + str(per) + "\n"
    fout.write(res)

fout.close()
