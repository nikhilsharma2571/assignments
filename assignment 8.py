#Q1
print("Time tuple is used to represen time in a way it is easy to understand.And it is stored in tuple.And also that these tuples are")
print("eg:index:0->year...index:1->Month...index:2->Day...index:3->hour...index:4->Minute...index:5->Sec...index:6->Day of week")

#Q2
import time
print(time.strftime("%H:%M:%S"))

#Q3
import time
print(time.strftime("%b"))

#Q4
import time
print(time.strftime("%d"))
print(time.strftime("%A"))

#Q5
import datetime
year=int(input("Enter year="))
mon=int(input("Enter month="))
date=int(input("Enter date="))
date1=datetime.date(year,mon,date)
print(date1)
print(date1.strftime("%b"))

#Q6
import time,datetime
a=time.localtime()
print(a)
print("Time using localtime-%d:%d:%d"%(a[3],a[4],a[5]))

#Q7
import math
a=int(input("Enter a number="))
print(math.factorial(a))

#Q8
a=int(input("Enter 1 numbers"))
b=int(input("Enter 2 numbers"))
print("gcd is:"+str(math.gcd(a, b)))

#Q9
print("Current Working Directory"+str(os.getcwd()))
print("User environment"+str(os.environ))