#q1
a=int(input("Enter the year"))
if(a%4==0):
    print("Its a leap year")
else:
    print("Its not a leap year")
#q2
a=int(input("Enter the length"))
b=int(input("Enetr the breadth"))
if(a==b):
    print("Its a square")
else:
    print("Its a rectangle")
#q3
a=input("Enter age of person 1")
b=input("Enter age of person 2")
c=input("Enetr age of person 3")
if(a>b):
    if(a>c):
        print("a is oldest")
    else:
        print("c is oldest")
elif(b<c and b<a):
    print("b is youngest")
elif(c<b and c<a):
    print("c is youngest")
elif(b>a and b>c):
    print("b is oldest")
else:
    if(a>c):
        print("a is youngest")
#q4
k=int(input("Enter your points out of 200"))
if(k>=1 and k<=50):
    print("Sorry! No prize this time")
elif(k>=51 and k<=150):
    print("Congratulations! You won Wooden Dog!")
elif(k>=150 and k<=180):
    print("Congratulations! You won Book")
elif(K>=180 and k<=200):
    print("Congratulations! You won Chocolates!")
#q5
j=int(input("enter the no.of units,one unit costs 100"))
sum=j*100
if(sum>=100):
    b=(sum*(sum/10))
    print("Amount :",b)
else:
    print("Amount : ",sum)