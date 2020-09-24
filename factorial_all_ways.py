#!/usr/bin/python3

import numpy as np

imp=int(input("Insert number\n"))
 

#The Python way
fac=np.prod(range(imp,1,-1))                                                



#Iterative way
def iterative(n):
    p=1
    for f in range(n,1, -1): 
        p=p*f 
    return p 
               
#Recursive

def recursive(n):
    if n==1:
        return n
    elif n==0:
        return 1
    else:
        return n*recursive(n-1)

  
if imp>=1:
    print (recursive(imp))
    print (iterative(imp))
    print (fac)
elif imp<0:
    print ("Insert a positive number")
    quit
