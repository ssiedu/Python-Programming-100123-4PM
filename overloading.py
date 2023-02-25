from multipledispatch import dispatch

@dispatch(int,int)
def sum(first,second):
    result=first+second
    print("Sum of two integer Number : ", result)


@dispatch(int,int,int)
def sum(first,second,third):
    result=first+second+third
    print("sum of three integer numbers : ", result)

@dispatch(float,int)
def sum(first,second):
    result=first+second
    print("Sum of two different value : ",result)

sum(10.33,12)
sum(100,200)
sum(100,200,300)
