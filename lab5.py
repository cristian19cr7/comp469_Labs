# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:11:54 2020

@author: Cristian Aguilar
"""
import math
class Node():
    def __init__(self, data,cost,x,y):
        self.data = data
        self.cost = cost
        self.children = []
        self.parent = None
        self.x = x
        self.y = y

def outOfboundsCheck(x, y):
    if(x <=-1 or y <= -1 or x >= 6 or y >= 6):
        return True
    else:
        return False

def eucildean_distance(currX, currY, goalX, goalY):
    x = abs(currX - goalX) - 1
    print(x)
    y = abs(currY - goalY) - 1
    print(y)
    z = x**2 + y**2
    z = math.sqrt(z)
    return z

def manhattan_distance(currX, currY, goalX, goalY):
    x = abs(currX - goalX)-1
    y = abs(currY - goalY)-1
    return x + y

def nextInTheFringe(fringeList):
    closestIndex = 0
    closest = fringeList[closestIndex]
    for index in range(0, len(fringeList)):
        if(fringeList[index].cost < closest.cost):
            closestIndex = index
    return fringe.pop(closestIndex)

def successor_fcn(currNode, fringeList, visitedList):
    
    x = currNode.x
    y = currNode.y
    visitedList.append((x,y))
    #left
    if(not outOfboundsCheck(x, y+1) and graph[x][y+1] != 'x'):
        if((x,y+1) not in visitedList):
            child = Node(graph[x][y+1], manhattan_distance(x, y+1, 6, 6),x,y+1)
            child.parent = currNode
            currNode.children.append(child)
            fringeList.append(child)
    #right
    if(not outOfboundsCheck(x, y-1) and graph[x][y-1] != 'x'):
        if((x,y-1) not in visitedList):
            child = Node(graph[x][y-1], manhattan_distance(x, y-1, 6, 6),x,y-1)
            child.parent = currNode
            currNode.children.append(child)
            fringeList.append(child)
    #up
    if(not outOfboundsCheck(x-1, y) and graph[x-1][y] != 'x'):
        if((x-1,y) not in visitedList):
            child = Node(graph[x-1][y], manhattan_distance(x-1, y, 6, 6),x-1,y)
            child.parent = currNode
            currNode.children.append(child)
            fringeList.append(child)
     
    #down
    if(not outOfboundsCheck(x+1, y) and graph[x+1][y] != 'x'):
        if((x+1,y) not in visitedList):
            child = Node(graph[x+1][y], manhattan_distance(x+1, y, 6, 6),x+1,y)
            child.parent = currNode
            currNode.children.append(child)
            fringeList.append(child)
            
#def greedy(currentNode):
    
graph = [['S',2,3,1,1,'x',3],
         [1,1,'x','x',3,'x',1],
         [3,1,'x',1,1,1,1],
         [1,1,3,4,4,1,2],
         [1,4,2,1,'x',1,'G']]

fringe = []
visited = []
root = Node('S', 0, 3,4)



print(eucildean_distance(0,0, 6,6))

print(manhattan_distance(0,0,6,6))
successor_fcn(root, fringe, visited)
nextNode = nextInTheFringe(fringe)







