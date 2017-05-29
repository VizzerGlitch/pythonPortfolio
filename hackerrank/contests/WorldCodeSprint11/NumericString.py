#!/bin/python3

import sys

def getMagicNumber(s, k, b, m):
    
    sumResult = 0
    
    n = len(s)
    
    for i in range(0,n - k + 1):
        sumResult += int(s[i:i+k], b)%m         
    return(sumResult)

s = input().strip()
k, b, m = input().strip().split(' ')
k, b, m = [int(k), int(b), int(m)]
result = getMagicNumber(s, k, b, m)
print(result)
