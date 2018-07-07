#q 1

import numpy as np

abc=np.random.random((10,1))
print(abc)
print("Mean of 10 random no :",abc.mean())
print("Mean of 10 random no :",np.mean(abc))

#q 2

a=np.random.rand(20,1)
print(a)
print("Variance :", a.var())
print("Standard Deviation :",a.std())

#q 3

A=np.random.random((10,20))
B=np.random.random((20,25))
C=np.dot(A,B)
print("Matrix",C)
print("Shape",C.shape)
print("Sum",np.sum(C))

#question4
from math import exp

def show(f):
    return (1/(1+(np.exp(-f))))
A=np.random.rand(10,1)
print("OLD array :",A)
B=show(A)
print("NEW array :",B)