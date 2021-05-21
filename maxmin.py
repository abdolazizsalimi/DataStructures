
from random import random

#max function 
def max_num(n):
    max=n[0]
    for i in range( len(n) ):
        if max<n[i]:
            max,n[i]=n[i],max
    return max

#min function
def min_num(n):
    min=n[0]
    for i in range(len(n)):
        if min>n[i]:
            min,n[i]=n[i],min
    return min

a=[random()*100 for i in range(10)]  
print("{:.2f}".format(a))  
print("{:.2f}".format(max_num(a)))  
print("{:.2f}".format(min_num(a)))  


