#!/bin/python3

import sys
import math
def solve(a):
    return abs(sum(a[:int(n/2)])-sum(a[int(n/2):]))

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = solve(a)
print(result)
