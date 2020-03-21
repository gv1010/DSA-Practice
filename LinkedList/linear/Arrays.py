# -*- coding: utf-8 -*-
"""
Created on Fri May 17 05:39:13 2019

@author: citrix
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    count = len(a)
    b=a
    if count%2 == 0:
        for i in range(count/2):
            temp = b[i]
            b[i] = b[count-i-1]
            b[count-i-1] = temp
        return b
    else:
        for i in range(int((count+1)/2)):
            temp = b[i]
            b[i] = b[count-i-1]
            b[count-i-1] = temp
        return b
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    print(' '.join(map(str, res)))
  
