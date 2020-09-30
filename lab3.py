# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 10:05:53 2020

@author: Cristian Aguilar
@Title: Lab3
"""
import string
def childernFinder(str1, dictList):
    alpha = string.ascii_lowercase
    result = []
    for i in range(0, len(str1)):
        for j in range(0, len(alpha)):
            temp = list(str1)
            temp[i] = alpha[j]
            strTemp = "".join(temp)
            if(strTemp in dictList and str1 != strTemp):
                result.append(strTemp)
                dictList.pop(dictList.index(strTemp))
    return result


startState = "boy"
goalState = "bay"
key = []
graph = {
    startState: []
}
dictonary = ["try","tim","tom","com","toy","cop","cuz","cob","cup","coy"
             ,"fry","cry","bay","lay","boo","bow","cow","fey","key","lop"]#removed boy
visited = set() # Set to keep track of visited nodes.
fringe = [startState]

def path(start, end, child):
    for i in range(0, len(child)):
        temp.append(child[i])
        if(temp[0] == start and temp[len(temp) - 1] == end):
            return temp
        else:
            path(start, end, graph[child])

# Driver Code
done = False
fringe.pop()
key.append(startState)
graph[startState] = childernFinder(startState, dictonary)
for item in graph[startState]:
    fringe.append(item)
node = startState
while True:
    node = fringe.pop()
    key.append(node)
    graph[node] = childernFinder(node,dictonary)
    for item in graph[node]:
        fringe.append(item)
    if node == goalState:
        break

print(key)

temp = [startState]
#path(startState, goalState, graph[startState])



