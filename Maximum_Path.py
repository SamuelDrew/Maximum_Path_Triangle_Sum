#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maximum_path' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY node_values as parameter.
#


def maximum_path(node_values):
    a = []
    k = 1
    #reformat input into array of triangle layers
    
    while True:
        sa = []
        x = (k-1)*k//2
        sa = node_values[x:x+k]
        if not sa:
            break
        a.append(sa)
        k+=1   
    #force layers to equal length by adding zero's, forming square matrix
    for j in range(len(a)):
        while len(a[-1]) > len(a[j]):
         a[j].append(0)
    
    #loop from bottom to top   time complexity = O(m*n)
    #for each element check below, and below - right
    for i in range(len(a)-2, -1, -1):
        for j in range(i+1):
    #add max
            if a[i+1][j] > a[i+1][j+1]:
                a[i][j] += a[i+1][j]
            else:
                a[i][j] += a[i+1][j+1]
    #return first element as it is storing max sum
            
    return a[0][0] 
    