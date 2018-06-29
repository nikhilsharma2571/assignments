'''#Q1
print("Exception is-ZerodivisionError")
i=3
try:
    if(i<4):
        i=i/(i-3)
except ZeroDivisionError:
    print("Zero division error")
else:
    print(i)'''


'''#Q2
a=[1,2,3]
try:
    print(a[3])
except IndexError:
    print("Element at 3rd index is not present")'''


'''#Q3
print("An exception")'''


'''#Q4
print("-5.0")
print("a/b result in 0")'''


'''#Q5
try:
    import Nikhil_sharma
    a=int(input("Enter any number="))
except ImportError:
    print("No such file exists")
except ValueError:
    print("Enter integer")'''