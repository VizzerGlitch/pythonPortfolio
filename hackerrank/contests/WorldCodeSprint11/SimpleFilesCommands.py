#!/bin/python3

import sys

def deleteName(dictName, fileName):
    startN, endN = None,None
        
    for i in range(len(fileName)):
        if(fileName[i] == '('):
            startN = i
        elif(fileName[i] == ')'):    
            endN = i
    if(startN!=None and endN!=None):            
            
        freeIndex = dictName.get(fileName[:startN])
        freeIndex.append(int(fileName[startN+1:endN]))
        dictName[fileName[:startN]] = freeIndex
            
    else:
        freeIndex = dictName.get(fileName)
        if(freeIndex==None):
            freeIndex = [0]
        else:
            freeIndex.append(0)
        dictName[fileName] = freeIndex
    

    return dictName

def createName(dictName, fileName):
    freeIndex = dictName.get(fileName)
    if(freeIndex == None ):
        print('+ '+fileName)
        freeIndex = [1];
    else:
        if(min(freeIndex) == 0):
            print('+ '+fileName)
        else:
            print('+ '+fileName+'('+str(min(freeIndex))+')')
        if(len(freeIndex)!=1):
            freeIndex.pop(freeIndex.index(min(freeIndex)))
        else:
            freeIndex[0] += 1
    dictName[fileName] = freeIndex

    return dictName

filenames = {}

q = int(input().strip())
# Process each command
for a0 in range(q):
    # Read the first string denoting the command type
    command = input().strip()
    # Write additional code to read the command's file name(s) and process the command
    # Print the output string appropriate to the command
    if(command[:3] == 'crt'):
        filenames = createName(filenames, command[4:])
    elif(command[:3] == 'del'):
        
        filenames = deleteName(filenames, command[4:])
        print('- '+command[4:])
    elif(command[:3] == 'rnm'):
        
        for i in range(4,len(command)):
            if(command[i] == ' '):
                firstWord = command[4:i]
                secWord = command[i+1:]
                
        filenames = deleteName(filenames, firstWord)
        freeIndex = filenames.get(secWord)

        if(freeIndex == None ):
            print('r '+firstWord+' -> '+secWord)
            freeIndex = [1];
        else:
            if(min(freeIndex) == 0):
                print('r '+firstWord+' -> '+secWord)
            else:
                print('r '+firstWord+' -> '+secWord+'('+str(min(freeIndex))+')')
            if(len(freeIndex)!=1):
                freeIndex.pop(freeIndex.index(min(freeIndex)))
            else:
                freeIndex[0] += 1
        filenames[secWord] = freeIndex
