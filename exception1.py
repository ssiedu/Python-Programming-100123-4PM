try:
    a=int(input("Enter First Number :"))
    b=int(input("Enter Second Number :"))
    c=a/b
    
except ZeroDivisionError:
    print("Divide by Zero Error")

except TypeError:
    print("Type Error Occured")

except:
    print("Some Error Occured")

else:
    print("Else Block")
    print("result is : ",c)

finally:
    print("Finally Block")
    print("Stop Execution")
    
