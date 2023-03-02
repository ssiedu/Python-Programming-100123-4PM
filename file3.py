n=int(input("Enter number of employee in ur company :"))
f=open("Employee.txt","w")
for i in range(n):
    name=input("Enter Employee Name :")
    sal=eval(input("Enter salary of Employee:"))
    res=name+ "  " + str(sal) + "\n"
    f.write(res)


f.close()
