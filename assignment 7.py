#Q1
def area(r):
    a=3.14*r*r
    print(a)
r=float(input("Enter the radius of the circle"))
area(r)

#Q2
def perfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum= sum + i
    if(sum==n):
        return True
    else:
        return False
for i in range(1,1001):
    if (perfect(i)==True):
        print("perfect number is:" +str(i))
    else:
        pass

#Q3
def multt(i):
    n=12
    if(i==11):
        return
    else:
        print(n,"*",i,"=",n*i)
        multt(i+1)
i=1
multt(i)

#Q4
def poww(a,b):
    if(b==0):
        return 1
    else:
        return(a*poww(a,b-1))
a=int(input("Enter numbder="))
b=int(input("Enter power"))
P=poww(a,b)
print(P)

#Q5
A={}
def factt(i):
    if(i==1):
        return 1
    else:
        F=i*factt(i-1)
        return(F)
a=int(input("Enter number="))
FF=factt(a)
A[a]=FFprint("Dictionary-",A)