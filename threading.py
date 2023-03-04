import threading
import time
def square(num):
    for n in num:
        time.sleep(0.3)
        print("Square :",n*n)


def cube(num):
    for n in num:
        time.sleep(0.4)
        print("cube : ",n*n*n)


l1=[2,3,4]
t1=threading.Thread(target=square,args=(l1,))
t2=threading.Thread(target=cube,args=(l1,))
t1.start()
time.sleep(0.3)
t2.start()
t1.join()
t2.join()
print("thread1 and thread2 are executed")
