#!/bin/python3

import sys

def getPoints(month1, month2, month3):
    if(month1>10):
        month1 = 10
    if(month2>10):
        month2 = 10
    if(month3>10):
        month3 = 10
    return 10*(month1+month2+month3)
    
    
month1,month2,month3 = input().strip().split(' ')
month1,month2,month3 = [int(month1),int(month2),int(month3)]
pointsEarned = getPoints(month1, month2, month3)
print(pointsEarned)
