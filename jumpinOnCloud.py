#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count = 0
    i = 0 
    while i < len(c):
        if c[i] == 0:
            if i == len(c)-2:
                i = i + 1
            else:
                i = i + 2
            if i < len(c):

                count = count + 1
        else:
            if c[i] == n -1:
                count = count -1
                break
            else:
                i = i -1
           
            
             
    return count
        
            
            

if __name__ == '__main__':
    n = int(input())
    c = list(map(int,input().rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)


