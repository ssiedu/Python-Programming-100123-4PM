for i in range(ord('a'),ord('e')):#row 1 2 3 4 5 
    for j in range(i,ord('e')):#column 1 2 3 4 5
        print(chr(i),end=" ")
    print(end="\n")
print("===============================================")


for i in range(1,6):
    j=1
    while j<6:
        print("#",end=" ")
        j=j+1
    print()
print("===============================================")

i=1
while i<6:
    for j in range(1,6):
        print("@",end=" ")
    i=i+1
    print()
print("==================================================")

i=1
while i<6:
    j=1
    while j<6:
        print("$",end=" ")
        j=j+1
    i=i+1
    print()







