import math
import os
import random
import re
import sys

# Complete the getWays function below.
def getWays(n, c, x):
    
   
    if n == 0:
        # print("got a match ")
        return 1
    if n<0 :
        # print("its -")
        return 0
    # print("running on:" )
    # print(c, " ")
    if (x <1 and n>0):
        # print("c is none")
        return 0
    
    # print("going on: x= {} and n= {}".format(x-1, n-c[x-1]))
    # sum = getWays(n, c, x-1) + getWays(n-c[x-1], c, x)
    # print(sum)
    return getWays(n, c, x-1) + getWays(n-c[x-1], c, x)


print(getWays(10, [2, 5, 3, 6], 4))


    