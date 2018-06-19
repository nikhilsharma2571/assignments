#Q1
l=[]
for a in range(10):
    a=int(input("Enter 10 increase"))
    l.append(a)
print(l)

#Q2
while(true):
    print(infinite)

#Q3
l=[]
j=[]
for a in range(10):
    a=int(input("Enter 10 integers"))
    l.append(a)
    j.append(a*a)
    print(l)
    print(j)

#Q4
l=[]
j=[]
k=[]
for i in range(10):
    a=input("Enter integer strings and float")
    if(isinstance(a,int)):
        l.append(a)
    elif(isinstance(a,str)):
        j.append(a)
    else:
        k.append(a)
print("integer",l)
print("string",j)
print("fload",k)

#Q5
even=[]
odd=[]
for i in range(1,101):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even" + str(even) +"odd" + str(odd))

#Q6
for i in range(0,4):
    print("")
    for j in range(0,i+1):
        print("*",end="")

#Q7
d={"name": "nikhil", "age":20}
for i in d:
    d.get(i)
    print(i)

#Q8
l=[]
for i in range(0,5):
    n=int(input("enter the number"))
    l.append(n)
print(l)
i=[]
a=int(input("Enter the value"))
x=1.index(2)
x=1.remove(2)
print(l)