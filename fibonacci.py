n=int(input("Enter any number : "))
x=0
y=1
print(x,end=" ")
print(y,end=" ")
for i in range(1,n-1):
    z=x+y
    print(z,end=" ")
    x=y
    y=z
