import sys

def minimumDeletions(a):
    
    i = 2
    if(len(a)<3):
        return 0
    dellen = len(a)

    while True:
        
        if i >= len(a):
            break
        
        if(a[i-2] > a[i-1] and a[i-1] > a[i]):
            a.pop(i-1)
        elif(a[i-2] < a[i-1] and a[i-1] < a[i]):
            a.pop(i-1)        
        else:
            i += 1
        
    return dellen - len(a)

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = minimumDeletions(a)
print(result)
