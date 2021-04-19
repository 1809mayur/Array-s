#!/bin/python3
from itertools import zip_longest
import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count = 0
    ar.sort()
    for i in range(1,n):
        for j,m in zip_longest(ar[:],ar[i:]):
            try:
                if (j+m)%k == 0:
                    count = count + 1
            except:
                pass
    return count
            
            

if __name__ == '__main__':
    

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)
    print(result)
    

    
