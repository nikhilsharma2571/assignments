#Q1
'''import time
import threading
class Mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        print("Hello World")
T1=Mythread()
time.sleep(5)
T1.start()


#Q2
import time
import threading
class Mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        for a in range(1,11):
            print(a)
            time.sleep(1)
T2=Mythread()
T2.start()


#Q3
import time
import threading
class Mythread(threading.Thread):
    def __init__(self,l,t):
        threading.Thread.__init__(self)
        self.l=l
        self.t=t
    def run(self):
        for a,b in zip(l,t):
            time.sleep(b)
            print(a)
l=[1,2,3,4,5]
t=[2,4,6,8,10]
T3=Mythread(l,t)
T3.start()


#Q4
import time
import threading
import math
class Mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.i=i
    def run(self):
        print("factorial of %d = %d"%(self.i,math.factorial(self.i)))
i=int(input("Enter the number="))
T4=Mythread(i)
T4.start()'''

