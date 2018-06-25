'''#Q1
class Animal():
    def animal_attribute(self):
        print("Animal Attribute calling")
class Tiger(Animal):
    def show1(self):
        self.animal_attribute()
A=Tiger()
A.show1()

#Q2
print("a.f(),b.f() --AB")
print("a.f(),b.f() --AB")

#Q3
class Cop():
    def __init__(self):
        self.name=input("name=")
        self.age=int(input("age="))
        self.we=input("work experience=")
        self.d=input("designation=")
    def display(self):
        print("Name=%s\tAge=%d\twork experience=%s\tdesignation=%s"%(self.name,self.age,self.we,self.d))
    def update(self):
        self.name = input("name=")
        self.age = int(input("age="))
        self.we = input("work experience=")
        self.d = input("designation=")
class Mission(Cop):
    def add__mission_details(self):
        self.md=input("details of mission of %s ="%(self.name))
    def mission_display(self):
        print("name=%s\tage=%d\twork experience=%s\tdesignation=%s\tmission=%s" % (self.name, self.age, self.we, self.d, self.md))
A=Mission()
A.display()
A.update()
A.display()
A.add_mission_details()
A.mission_display()
'''
#Q4
class shape:
    def show2(self):
        self.l=int(input("enter length"))
        self.b=int(input("enter breadth"))
class rectangle(shape):
    def area(self):
        self.show2()
        self.a=self.l*self.b
    def show1(self):
        print("area of rectangle :",self.a)
class square(shape):
    c=0
    def area(self):
        self.show2()
        if(self.l==self.b):
            self.a=self.l*self.l
            self.c=1
        else:
            print("enter same length and breadth")
    def show1(self):
        if(self.c==1):
            print("area of square is : ",self.a)
        else:
            pass
r=rectangle()
a=square()
r.area()
r.show1()
s.area()
s.show1()
