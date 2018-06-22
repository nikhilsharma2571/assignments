#Q1
class Circle():
    def __init__(self,radius):
       self.rad=radius
    def getarea(self):
        print("area of circle is:" +str(3.14*self.rad*self.rad))
    def getcircumference(self):
        print("circumference is :" +str(2*3.14*self.rad))
a=Circle(3)
a.getarea()
a.getcircumference()

#Q2
class Student():
  def __init__(self,name,rollno):
      self.n=name
      self.r=rollno
  def display(self):
      print("the information of students is :Name is "+str(self.n)+ "roll no is "+str(self.r))
a=Student(" NIKHIL ",93)
a.display()

#Q3
class Temperature():
    def __init__(self,celsius,farhenite):
        self.c=celsius
        self.f=farhenite
    def celsius(self):
        print("the temperature in celsius to farhenite is:" +str((self.c*1.8)+32))
    def farhenite(self):
        print("the temperature from farhenite into celsius:" +str((self.f-32)*0.5556))
a=Temperature(12,78)
a.celsius()
a.farhenite()

#Q4
class Moviedetails():
    def __init__(self):
        name=input("Enter movie name=")
        an=input("Enter name of artist=")
        year=int(input("Enter year of release="))
        rat=int(input("Enter ratings of movie"))
        self.name=name
        self.an=an
        self.year=year
        self.rat=rat
    def display(self):
        print("the details of movie, name is:" +str(self.name) + ", artist name is " +str(self.an) + " ,year of release is " + " ratings are " +str(self.r))
    def update(self,n,a,y,r):
        self.name2= n
        self.an2= a
        self.year2= y
        self.rat2= r
        print("the details of movie, name is:" +str(self.moviename2) + ",artist name is" +str(self.an2) + " ,year of release is" +str(self.year2) + " ratings are " +str(self.r2))
c=Moviedetails()
c.display()
name1=input("Enter updated movie name=")
an1=input("Enter name of artist of updated movie=")
year1=int(input("Enter year fo release of updated movie="))
rat1=int(input("Enter ratings of updated movie="))
c.update(name1,an1,year1,rat1)

#Q5
class Expenditure():
    def __int__(self):
        b=int(input("Enter your savings"))
        a=int(input("Enter amount of money you spent="))
        self.a=a
        self.b=b
    def display(self):
        print("Your savings are Rs%d and spent Rs%d"%(self.a,self.b))
    def salary(self):
        self.c=self.a+self.b
    def displaysalary(self):
        print("Total salary=",self.c)
e=Expenditure()
e.display()
e.salary()
e.displaysalary()