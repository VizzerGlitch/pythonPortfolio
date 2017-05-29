#!/bin/python3

import sys
import math
import time

def solve(a):

    start = time.time()
    
    testX = 0
    
    result = 0
    
    minOnes = math.inf
    
    while True:
        
        testX += 1
        
        flag = True
        for i in range(len(a)):
            if(testX&a[i] == 0):
                flag = False
                break
                
        if(flag):
            strBin = "{0:b}".format(testX)
            counter = 0
            for j in range(len(strBin)):
                if(strBin[j] == '1'):
                    counter += 1
            if(counter < minOnes):
                result = testX
                minOnes = counter
    
        if((time.time()-start) >= 3.91):
            return result
    
            
            
            
    
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = solve(a)
print(result)
