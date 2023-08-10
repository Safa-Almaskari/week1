import pandas as pd
import numpy as np


l1=[7,8,6,100,7,9]
print("The list is: ",l1)
avg=np.average(l1)
print("Average is: ", avg)
std=np.std(l1)
print("Std is: ", std)

for i in l1:
    z=(i-avg)/std
    print("z-score is: ", z)
    
#converting list to set then back to list
#for duplicates
l2=[7,8,7,9,7,8]
s= set(list(l2))
print("Set/list", list(s))

l3=[85,94,2,46,47,3,5,47,50,43]
x=min(l3)
y=max(l3)
print("Minmum is: ", x , " Maximum is: ", y)

for i in l3:
    l=(i-x)/(y-x)
    print("Normalization of ",i, "is: ", l)

